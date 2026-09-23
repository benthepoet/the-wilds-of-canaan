# The Wilds of Canaan
## Settings & Options Document

---

## 1. Philosophy

Settings are not an afterthought. They are **respect for the player.** A player who cannot read small text, who is sensitive to flashing lights, or who prefers inverted controls is not a edge case. They are a player. Every setting must have a clear purpose and a sensible default.

---

## 2. Settings Categories

### 2.1 Graphics

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Viewport Size** | Dynamic / 80x30 / 100x45 / 120x60 | Dynamic | Browser window determines size. |
| **Cell Size** | 10x12 (Far) / 14x18 (Normal) / 20x24 (Close) | Normal | Affects text readability. |
| **Font** | Monospace / Serif / Dyslexic-friendly | Monospace | Dyslexic font for accessibility. |
| **Color Palette** | Default / High Contrast / Deuteranopia / Protanopia / Tritanopia | Default | Simulates colorblindness for testing. |
| **Blight Animation** | On / Slow / Off | On | Slow = pulse every 4s instead of 2s. Off = static. |
| **Screen Shake** | On / Reduced / Off | On | Reduced = 50% intensity. |
| **Fullscreen** | On / Off | Off | Browser fullscreen API. |
| **FPS Limit** | 30 / 60 / Unlimited | 60 | Lower for battery saving. |

### 2.2 Audio

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Master Volume** | 0-100% | 80% | Affects all audio. |
| **Ambient Volume** | 0-100% | 60% | Wind, water, forest. |
| **SFX Volume** | 0-100% | 80% | Footsteps, combat, building. |
| **Music/Chanting Volume** | 0-100% | 40% | Religious chanting, Manifestation drones. |
| **UI Sounds** | 0-100% | 50% | Menu clicks, confirmations. |
| **Subtitles** | On / Off | Off | Shows [sound descriptions] in message log. |
| **Subtitle Size** | Small / Medium / Large | Medium | |
| **Audio Cues for Visual Events** | On / Off | On | Plays sound when visual-only event occurs (e.g., blight surge). |

### 2.3 Controls

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Input Mode** | Keyboard / Mouse / Both | Both | Mouse-only disables keyboard hints. |
| **Movement Keys** | Vi-keys (hjklyubn) / Numpad / Arrows / Custom | Vi-keys | |
| **Sprint Modifier** | Shift / Ctrl / Alt / Toggle | Shift | Toggle = press once to sprint until pressed again. |
| **Auto-Repeat** | On / Off | On | Holding `G` gathers continuously. |
| **Keybinds** | [Customizable grid] | Default | Every action rebindable. |
| **One-Handed Mode** | On / Off | Off | Preset: arrows + number row + function keys. |
| **Mouse Sensitivity** | 1-10 | 5 | For click-to-path precision. |
| **Right-Click Behavior** | Context Menu / Quick Action | Context Menu | Quick Action = right-click performs most likely action. |

### 2.4 Gameplay

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Difficulty** | Pilgrim / Settler / Exile / Martyr | Settler | See Tutorial doc. |
| **Ironman Mode** | On / Off | On | One save. Death = delete. Off = multiple saves. |
| **Autosave Interval** | Every turn / Every 10 turns / Every day / Off | Every 10 turns | |
| **Permadeath** | On / Off | On | Off = reload from last save after death. |
| **Tutorial Hints** | Full / Context Only / Off | Context Only | Full = all hints. Context = only new mechanics. |
| **Ghost Mode** | On / Off | On | Show tutorial ghost on first run. |
| **Day Length (Real Time)** | 5 min / 10 min / 20 min / 30 min | 10 min | Affects pacing. 10 min = relaxed. 5 min = frantic. |
| **Pause on Focus Loss** | On / Off | On | Auto-pause when tab is not active. |
| **Seed Input** | Random / Manual | Random | Manual = player types seed string. |

### 2.5 Accessibility

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Colorblind Mode** | Off / Deuteranopia / Protanopia / Tritanopia / Patterns | Off | Patterns = shapes instead of colors for all critical info. |
| **High Contrast** | On / Off | Off | Pure black/white, no greys. |
| **Large Text** | On / Off | Off | 150% font size for all UI text. |
| **Screen Reader Mode** | On / Off | Off | Optimizes for screen readers: more verbose descriptions, slower auto-advance. |
| **Reduce Motion** | On / Off | Off | Disables all animations: no pulse, no shake, no fade. |
| **Flashing Lights** | On / Reduced / Off | On | Off = Blood Moon and Manifestation spawns do not flash. |
| **Dyslexia Font** | On / Off | Off | OpenDyslexic for all text. |
| **Cognitive Load Reduction** | On / Off | Off | Simpler UI, fewer simultaneous messages, longer hint display. |

### 2.6 Interface

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| **Message Log Size** | 3 lines / 5 lines / 7 lines | 5 lines | |
| **Sidebar Position** | Right / Left / Hidden | Right | Hidden = minimal HUD, immersive. |
| **Mini-Map Size** | Small / Medium / Large | Medium | |
| **Show Coordinates** | On / Off | Off | Debug/tooltip feature. |
| **Show FPS** | On / Off | Off | Debug feature. |
| **Show Seed** | On / Off | On | Display seed in top bar. |
| **Compact Mode** | On / Off | Off | Reduces UI chrome, maximizes viewport. |

---

## 3. Settings Persistence

All settings are saved to `localStorage`:

```typescript
const DEFAULT_SETTINGS = {
    graphics: {
        viewportSize: 'dynamic',
        cellSize: 'normal',
        font: 'monospace',
        colorPalette: 'default',
        blightAnimation: 'on',
        screenShake: 'on',
        fullscreen: false,
        fpsLimit: 60
    },
    audio: {
        masterVolume: 0.8,
        ambientVolume: 0.6,
        sfxVolume: 0.8,
        musicVolume: 0.4,
        uiVolume: 0.5,
        subtitles: false,
        subtitleSize: 'medium',
        audioCues: true
    },
    controls: {
        inputMode: 'both',
        movementKeys: 'vi',
        sprintModifier: 'shift',
        autoRepeat: true,
        keybinds: {},  // Empty = use defaults
        oneHandedMode: false,
        mouseSensitivity: 5,
        rightClickBehavior: 'context'
    },
    gameplay: {
        difficulty: 'settler',
        ironmanMode: true,
        autosaveInterval: 10,
        permadeath: true,
        tutorialHints: 'context',
        ghostMode: true,
        dayLength: 10,
        pauseOnFocusLoss: true,
        seedInput: 'random'
    },
    accessibility: {
        colorblindMode: 'off',
        highContrast: false,
        largeText: false,
        screenReaderMode: false,
        reduceMotion: false,
        flashingLights: 'on',
        dyslexiaFont: false,
        cognitiveLoadReduction: false
    },
    interface: {
        messageLogSize: 5,
        sidebarPosition: 'right',
        miniMapSize: 'medium',
        showCoordinates: false,
        showFPS: false,
        showSeed: true,
        compactMode: false
    }
};

function loadSettings(): Settings {
    const saved = localStorage.getItem('canaan_settings');
    if (saved) {
        return mergeDeep(DEFAULT_SETTINGS, JSON.parse(saved));
    }
    return DEFAULT_SETTINGS;
}

function saveSettings(settings: Settings) {
    localStorage.setItem('canaan_settings', JSON.stringify(settings));
}
```

**Settings are synced across runs.** Change font size in run 1, it persists in run 2.

---

## 4. Settings UI

### 4.1 In-Game Menu

Press `Esc` to open:

```
+------------------------------------------------------------------+
| Menu                                                [Esc] Resume |
+------------------------------------------------------------------+
|                                                                  |
|  [G]raphics    [A]udio    [C]ontrols    [G]ameplay              |
|  [H]elp    [S]ave & Quit    [Q]uit Without Saving               |
|                                                                  |
+------------------------------------------------------------------+
```

### 4.2 Graphics Tab

```
+------------------------------------------------------------------+
| Graphics                                                         |
+------------------------------------------------------------------+
|                                                                  |
|  Viewport Size      [Dynamic v]                                  |
|  Cell Size          [Normal v]                                   |
|  Font               [Monospace v]                                |
|  Color Palette      [Default v]                                  |
|  Blight Animation   [On v]                                       |
|  Screen Shake       [On v]                                       |
|  Fullscreen         [ ]                                          |
|  FPS Limit          [60 v]                                       |
|                                                                  |
|  [Preview]  [Reset to Default]  [Apply]                          |
+------------------------------------------------------------------+
```

**Preview button:** Opens a mini-demo viewport showing current settings in action (blight pulsing, text rendering).

### 4.3 Controls Tab

```
+------------------------------------------------------------------+
| Controls                                                         |
+------------------------------------------------------------------+
|                                                                  |
|  Movement:  [h] West  [j] South  [k] North  [l] East            |
|             [y] NW    [u] NE     [b] SW     [n] SE              |
|                                                                  |
|  [Click to rebind]  [Reset All]  [Load Preset: One-Handed]      |
|                                                                  |
|  Sprint Modifier:  [Shift v]                                     |
|  Auto-Repeat:      [X] On                                        |
|                                                                  |
+------------------------------------------------------------------+
```

**Rebinding:** Click a key, press new key. Conflicts are highlighted in red.

---

## 5. Presets

### 5.1 One-Handed Preset

```typescript
const ONE_HANDED_PRESET = {
    controls: {
        movementKeys: 'arrows',
        keybinds: {
            'gather': '1',
            'attack': '2',
            'build': '3',
            'rite': '4',
            'craft': '5',
            'inventory': 'F1',
            'map': 'F2',
            'help': 'F3',
            'wait': 'Enter',
            'sprint': 'Shift'
        }
    }
};
```

### 5.2 Streamer Preset

```typescript
const STREAMER_PRESET = {
    graphics: {
        cellSize: 'close',
        showFPS: true,
        showSeed: true,
        compactMode: true
    },
    interface: {
        messageLogSize: 7,
        sidebarPosition: 'right'
    },
    gameplay: {
        dayLength: 20  // Slower for commentary
    }
};
```

### 5.3 Accessibility Preset

```typescript
const ACCESSIBILITY_PRESET = {
    graphics: {
        cellSize: 'close',
        font: 'dyslexic'
    },
    accessibility: {
        highContrast: true,
        largeText: true,
        reduceMotion: true,
        flashingLights: 'off',
        dyslexiaFont: true,
        cognitiveLoadReduction: true
    },
    audio: {
        subtitles: true,
        subtitleSize: 'large'
    }
};
```

---

## 6. Command-Line / URL Parameters

Settings can be overridden via URL for sharing:

```
https://canaan.game/?seed=7f3a9c&difficulty=settler&ironman=on&dayLength=10
```

| Parameter | Values | Overrides |
|-----------|--------|-----------|
| `seed` | Any string | Game seed |
| `difficulty` | pilgrim, settler, exile, martyr | Difficulty preset |
| `ironman` | on, off | Ironman mode |
| `dayLength` | 5, 10, 20, 30 | Day length in minutes |
| `vocation` | priest, woodsman, craftsman | Starting vocation |
| `ghost` | on, off | Ghost mode |
| `hints` | full, context, off | Tutorial hints |
| `font` | monospace, serif, dyslexic | Font |
| `cellSize` | far, normal, close | Zoom |

---

## 7. Summary

| Category | Settings Count | Key Feature |
|----------|---------------|-------------|
| **Graphics** | 8 | Colorblind palettes, dynamic viewport, dyslexic font |
| **Audio** | 9 | Per-layer volume, subtitles, audio cues for visuals |
| **Controls** | 8 | Full rebindability, one-handed preset, auto-repeat |
| **Gameplay** | 9 | Difficulty presets, Ironman toggle, day length |
| **Accessibility** | 8 | Reduce motion, flashing lights off, cognitive load reduction |
| **Interface** | 7 | Compact mode, sidebar position, mini-map size |
| **Total** | **49** | Every setting has a purpose and a default |

The settings screen is not a dumping ground. It is a **statement of values:** this game is for everyone who wants to play it.

---

Document Version 1.0
The Wilds of Canaan - Settings & Options Document
