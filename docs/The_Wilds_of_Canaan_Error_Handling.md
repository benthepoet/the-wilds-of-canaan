# The Wilds of Canaan
## Error Handling & Recovery Document

---

## 1. Philosophy

A survival game that kills the player is expected. A game that crashes and loses progress is unforgivable. Error handling in Canaan is not about preventing failure — it is about **recovering gracefully** and **never blaming the player.**

**Principles:**
- **Save early, save often.** The game should never lose more than 10 seconds of progress.
- **Fail soft.** A broken animation should not crash the game. A missing sound file should not silence all audio.
- **Tell the truth.** Error messages explain what happened in plain language, not stack traces.
- **Offer a path forward.** Every error state has a recovery action.

---

## 2. Save System Resilience

### 2.1 Auto-Save Strategy

```typescript
// Auto-save every 10 turns AND every 30 seconds
const AUTO_SAVE_INTERVAL_TURNS = 10;
const AUTO_SAVE_INTERVAL_MS = 30000;

class SaveManager {
    private saveSlots: string[] = ['save_a', 'save_b', 'save_c'];
    private currentSlot = 0;

    autoSave(engine: Engine) {
        const slot = this.saveSlots[this.currentSlot];
        const data = engine.serialize();

        try {
            localStorage.setItem(slot, JSON.stringify(data));
            this.currentSlot = (this.currentSlot + 1) % 3;  // Rotate slots
        } catch (e) {
            this.handleSaveError(e, data);
        }
    }

    private handleSaveError(error: Error, data: object) {
        if (error.name === 'QuotaExceededError') {
            // localStorage full - purge old Chronicles
            this.purgeOldChronicles();
            // Retry
            try {
                localStorage.setItem(this.saveSlots[0], JSON.stringify(data));
            } catch (e2) {
                // Still failing - warn player
                showWarning('Storage full. Please export your save.');
            }
        }
    }
}
```

**Three rotating save slots:** If the most recent save is corrupted, the previous two are intact. Maximum loss: 20 turns (or 60 seconds).

### 2.2 Save Corruption Detection

```typescript
function validateSave(data: unknown): boolean {
    // Schema validation
    if (!data || typeof data !== 'object') return false;
    if (!data.seed || typeof data.seed !== 'string') return false;
    if (!data.day || typeof data.day !== 'number') return false;
    if (data.day < 0 || data.day > 10000) return false;
    if (!data.player || typeof data.player !== 'object') return false;
    if (data.player.health < 0 || data.player.health > 100) return false;

    // Checksum validation (simple)
    const storedChecksum = data._checksum;
    const computedChecksum = hash(JSON.stringify(data, (k, v) => k === '_checksum' ? undefined : v));
    if (storedChecksum !== computedChecksum) {
        console.warn('Save checksum mismatch. Possible corruption.');
        return false;
    }

    return true;
}
```

**On corruption:**
1. Try previous save slot.
2. If all slots corrupted: "Your save could not be loaded. Starting a new pilgrimage. Your Chronicle entries are preserved."
3. Chronicle entries (separate storage) are NOT lost. The story continues even if the world resets.

### 2.3 Export / Import

```typescript
function exportSave(): string {
    const save = localStorage.getItem('canaan_save_a');
    const compressed = btoa(save);  // Base64 for safe text transport
    return `CANAAN:${compressed}`;
}

function importSave(data: string): boolean {
    if (!data.startsWith('CANAAN:')) {
        showError('Invalid save format.');
        return false;
    }

    try {
        const decompressed = atob(data.substring(7));
        const parsed = JSON.parse(decompressed);

        if (!validateSave(parsed)) {
            showError('Save file is corrupted or from an incompatible version.');
            return false;
        }

        localStorage.setItem('canaan_save_a', decompressed);
        return true;
    } catch (e) {
        showError('Could not read save file.');
        return false;
    }
}
```

**Export formats:**
- **Text:** `CANAAN:base64string` — paste into any text field, email, Discord.
- **File:** `.canaan` file download — double-click to import (via file picker).
- **QR Code:** For mobile transfer (future).

---

## 3. Engine Crash Recovery

### 3.1 The Unhandled Exception

If the TypeScript engine throws an uncaught exception:

```typescript
// engine.worker.ts
self.onerror = (error) => {
    // 1. Log to console (for debugging)
    console.error('Engine crash:', error);

    // 2. Emit crash protocol line
    self.postMessage({
        type: 'CRASH',
        error: {
            message: error.message,
            stack: error.stack,
            tick: engine?.tick,
            seed: engine?.seed
        }
    });

    // 3. Attempt emergency save
    try {
        const emergencySave = engine.serialize();
        localStorage.setItem('canaan_emergency_save', JSON.stringify(emergencySave));
    } catch (e) {
        // If even emergency save fails, we've done all we can
    }

    // 4. Terminate worker (clean shutdown)
    self.close();
};
```

**Client response to CRASH:**
```
+------------------------------------------------------------------+
|                                                                  |
|           The world has fractured.                               |
|                                                                  |
|           An unexpected error occurred in the game engine.       |
|           Your progress has been saved to an emergency file.     |
|                                                                  |
|           Seed: 7f3a9c                                           |
|           Day: 14                                                |
|           Tick: 3421                                             |
|                                                                  |
|           [R]estart from Emergency Save                          |
|           [N]ew Pilgrimage (Chronicle preserved)                 |
|           [E]xport Save (for bug report)                         |
|           [B]ug Report (copies error to clipboard)               |
|                                                                  |
+------------------------------------------------------------------+
```

### 3.2 Recovery Options

| Option | Action | Result |
|--------|--------|--------|
| **Restart from Emergency Save** | Load `canaan_emergency_save` | Resume from last tick before crash. May re-trigger crash if bug is deterministic. |
| **New Pilgrimage** | Start fresh, same seed | Chronicle entries preserved. New world state. |
| **Export Save** | Download `.canaan` file | Can be imported later, or sent to developers. |
| **Bug Report** | Copy error + save to clipboard | Player can paste into GitHub issue, Discord, email. |

### 3.3 Deterministic Replay

Because the game is deterministic (same seed + same inputs = same output), crashes are reproducible:

```typescript
// replay.ts
function replayCrash(seed: string, inputs: string[]): void {
    const engine = new Engine({ seed, headless: true });

    for (const input of inputs) {
        engine.input(input);
        engine.tick();
    }

    // If we reach here without crash, the bug is fixed
}

// Usage: replay from crash report
replayCrash('7f3a9c', crashReport.inputHistory);
```

**Every crash report includes:**
- Seed
- Day and tick
- Last 50 inputs
- Engine version
- Browser version
- Error message and stack trace

---

## 4. Browser-Specific Errors

### 4.1 localStorage Unavailable

**Cause:** Private browsing mode, disabled cookies, storage quota exceeded.

**Detection:**
```typescript
function isStorageAvailable(): boolean {
    try {
        const test = '__storage_test__';
        localStorage.setItem(test, test);
        localStorage.removeItem(test);
        return true;
    } catch (e) {
        return false;
    }
}
```

**Response:**
```
+------------------------------------------------------------------+
| Warning: Cannot Save Progress                                    |
|                                                                  |
| Your browser is blocking local storage. The game will still      |
| play, but progress will be lost when you close the tab.          |
|                                                                  |
| [How to Fix]  [Play Anyway]  [Export Save Now]                   |
+------------------------------------------------------------------+
```

**Fallback:** Keep save in memory only. Offer "Export Save" button prominently. Warn on page close.

### 4.2 Web Audio API Unavailable

**Cause:** Browser blocks autoplay, user has not interacted with page yet.

**Detection:**
```typescript
function isAudioAvailable(): boolean {
    return typeof AudioContext !== 'undefined' && 
           new AudioContext().state !== 'suspended';
}
```

**Response:**
- Audio initializes on first user interaction (click/keypress), not on page load.
- If AudioContext is suspended, show: "Click to enable audio."
- If Web Audio API is not supported (rare), silently disable audio. Game is fully playable without it.

### 4.3 Canvas Not Supported

**Cause:** Very old browser, headless environment, accessibility tool.

**Detection:**
```typescript
function isCanvasSupported(): boolean {
    const canvas = document.createElement('canvas');
    return !!(canvas.getContext && canvas.getContext('2d'));
}
```

**Response:**
```
+------------------------------------------------------------------+
| Your browser does not support HTML5 Canvas.                      |
|                                                                  |
| The Wilds of Canaan requires a modern browser with Canvas        |
| support. Please use Chrome, Firefox, Safari, or Edge.            |
|                                                                  |
| [Download Chrome]  [Download Firefox]                            |
+------------------------------------------------------------------+
```

### 4.4 Web Worker Not Supported

**Cause:** Very old browser, restricted environment.

**Fallback:** Run engine in main thread. Performance is worse (frame drops during world-gen), but game is playable.

```typescript
if (typeof Worker === 'undefined') {
    console.warn('Web Workers not supported. Running engine in main thread.');
    engine = new Engine({ useWorker: false });
}
```

### 4.5 Out of Memory

**Cause:** Large world, many entities, memory leak.

**Detection:**
```typescript
function checkMemory(): void {
    if (performance.memory && performance.memory.usedJSHeapSize > 500 * 1024 * 1024) {
        // 500MB threshold
        showWarning('Memory usage is high. Consider saving and refreshing.');
    }
}
```

**Mitigation:**
- Unload distant world chunks (keep only viewport + buffer in memory).
- Compress save data before storing.
- Limit Chronicle history (keep last 100 entries, archive older ones).

---

## 5. Network Errors (Future Backend)

When the backend is added, these errors become relevant:

### 5.1 WebSocket Disconnect

```
+------------------------------------------------------------------+
| Connection Lost                                                  |
|                                                                  |
| The connection to the server was interrupted.                    |
| Your progress has been saved locally.                            |
|                                                                  |
| [Reconnect]  [Continue Offline]  [Save & Quit]                   |
+------------------------------------------------------------------+
```

**Behavior:**
- Auto-reconnect with exponential backoff (1s, 2s, 4s, 8s... max 30s).
- If reconnect fails: switch to offline mode (local engine, localStorage saves).
- When reconnect succeeds: sync local save to server.

### 5.2 Server Overload

```
+------------------------------------------------------------------+
| Server Busy                                                      |
|                                                                  |
| The server is experiencing high load.                            |
| You are in queue: Position 3 / Estimated wait: 45 seconds.       |
|                                                                  |
| [Wait]  [Play Offline]  [Cancel]                                 |
+------------------------------------------------------------------+
```

### 5.3 Version Mismatch

```
+------------------------------------------------------------------+
| Update Required                                                  |
|                                                                  |
| The server is running version 1.2.0. You have 1.1.0.            |
| Please refresh the page to update.                               |
|                                                                  |
| [Refresh]  [Play Offline (1.1.0)]                                |
+------------------------------------------------------------------+
```

---

## 6. User Error Prevention

### 6.1 Destructive Actions

| Action | Confirmation Required | Method |
|--------|----------------------|--------|
| **Quit without saving** | Yes | "You have unsaved progress. Save before quitting?" |
| **Delete Chronicle** | Yes + type "DELETE" | Prevents accidental deletion |
| **Overwrite save** | Yes | "A save exists for this seed. Overwrite?" |
| **Import corrupted save** | Validation + warning | "This save appears corrupted. Import anyway?" |
| **Change difficulty mid-run** | No | Allowed, but disables achievements |

### 6.2 Ironman Protection

In Ironman mode:
- **No "Load Save" button.** Only "Continue" and "New Pilgrimage."
- **Auto-save is mandatory.** Cannot be disabled.
- **Export is allowed.** But the exported file is marked "IRONMAN" and cannot be imported into non-Ironman runs.

### 6.3 Accidental Input Prevention

- **Pause on focus loss:** Game auto-pauses when tab is not active. Prevents "I alt-tabbed and died."
- **Confirm on dangerous tiles:** Stepping into high blight (`>80`) or water in winter requires `Shift + direction` or a click confirmation.
- **Undo last action:** In non-Ironman mode, `Ctrl+Z` undoes the last action (only if no hostile has acted since).

---

## 7. Error Logging & Telemetry

### 7.1 What We Log (Opt-In)

```typescript
interface TelemetryEvent {
    type: 'error' | 'performance' | 'gameplay';
    timestamp: number;
    seed?: string;
    day?: number;
    tick?: number;
    vocation?: string;
    data: object;
}

// Error event
{
    type: 'error',
    timestamp: 1694275200000,
    seed: '7f3a9c',
    day: 14,
    tick: 3421,
    vocation: 'priest',
    data: {
        message: 'Cannot read property blight of undefined',
        stack: '...',
        action: 'move_east',
        browser: 'Chrome 116',
        os: 'Windows 10'
    }
}
```

**Opt-in:** On first crash, ask: "Send anonymous error report to help improve the game?" Default: No.

### 7.2 What We Do NOT Log

- Player name
- IP address
- Any text input by player
- Chronicle content (personal)
- Exact world state (reproducible from seed + inputs anyway)

### 7.3 Self-Hosted Telemetry

```typescript
const TELEMETRY_ENDPOINT = 'https://telemetry.canaan.game/collect';

async function sendTelemetry(event: TelemetryEvent) {
    if (!settings.telemetryEnabled) return;

    try {
        await fetch(TELEMETRY_ENDPOINT, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(event),
            // No cookies, no credentials
            credentials: 'omit'
        });
    } catch (e) {
        // Silently fail. Telemetry is not critical.
    }
}
```

**GDPR compliant:** No PII. No cookies. IP is not stored (server discards it). User can disable anytime.

---

## 8. Summary

| Error Type | Prevention | Recovery | User Impact |
|-----------|-----------|----------|-------------|
| **Save corruption** | Checksums, 3 rotating slots | Load previous slot | Max 20 turns lost |
| **localStorage full** | Auto-purge old Chronicles | Export save prompt | No progress lost |
| **Engine crash** | try/catch in worker | Emergency save + restart | Resume from crash point |
| **Browser no Canvas** | Feature detection | Graceful degradation message | Cannot play (rare) |
| **Browser no localStorage** | Feature detection | In-memory + export | Progress lost on close |
| **WebSocket disconnect** | Auto-reconnect | Offline mode | Seamless fallback |
| **Accidental quit** | Confirm dialog | Auto-save | None |
| **Destructive action** | Confirm + type-to-delete | Undo (non-Ironman) | None |

**The golden rule:** The player should never lose more than 60 seconds of progress, and should always understand why something went wrong.

---

Document Version 1.0
The Wilds of Canaan - Error Handling & Recovery Document
