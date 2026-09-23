# The Wilds of Canaan
## Technical Architecture Document

---

## 1. Philosophy

The game engine is a **headless simulation** that outputs a stream of logical rendering commands. It does not draw pixels, ASCII characters, or sprites. It describes the world state in a simple text protocol, and **clients** render it however they choose.

This architecture enables:
- A **web-based prototype** from day one
- **SSH playability** (the engine runs as a server; any terminal connects)
- **Future tile packs** without engine changes
- **Mod support** via mapping overrides
- Multiple simultaneous clients viewing the same world

---

## 2. The Pseudoterminal (Pty) Architecture

```
+-------------------------------------------------------------+
|                    THE GAME ENGINE                            |
|  (Python, headless, no drawing code)                        |
|                                                             |
|  + World Sim (blight, weather, AI, combat)                |
|  + Save/Load (JSON or SQLite)                             |
|  + Protocol Emitter (writes to pty master)                |
+-------------------------------------------------------------+
                           |
                           |  Text stream (custom protocol)
                           v
+-------------------------------------------------------------+
|                    PTY SLAVE / SOCKET                         |
|  (Unix pseudoterminal or TCP/WebSocket)                     |
+-------------------------------------------------------------+
                           |
            +--------------+--------------+
            |                             |
            v                             v
+---------------------+         +---------------------+
|  TERMINAL CLIENT    |         |  WEB CLIENT         |
|  (ANSI renderer)    |         |  (Canvas/WebGL)     |
|  - Local terminal   |         |  - Browser          |
|  - SSH session      |         |  - Mobile           |
+---------------------+         +---------------------+
```

### 2.1 Why Pty Instead of Direct Terminal Control

Traditional roguelikes use `ncurses` or `blessed` to take over the terminal directly. This is wrong for this project because:

- **ncurses assumes a local terminal.** It cannot serve multiple clients over a network.
- **ncurses fights with ptys.** It wants to control the terminal buffer directly, not emit a clean stream.
- **ncurses is ASCII-only.** There is no clean path from `ncurses` to a sprite-based renderer.

The pty approach inverts this: the engine is a **server**, and every display is a **client**.

### 2.2 The Pty as a First-Class Feature

The engine creates a Unix pseudoterminal pair (`os.openpty()`):
- **Master fd:** The engine writes protocol lines here.
- **Slave fd:** Clients read from here.

For local play, a thin Python wrapper opens the slave and renders ANSI.

For network play, a WebSocket bridge reads the master fd and forwards lines to browsers.

For SSH play, the engine binary is the login shell. The user SSHs in and immediately sees the game.

---

## 3. The Rendering Protocol

The game engine never thinks about characters or sprites. It thinks about **glyphs**.

A glyph is a logical tile type with state. The engine emits one line per frame per changed cell.

### 3.1 Protocol Format

```
DRAW <x> <y> <tile_type> <state_flags> <fg_color> <bg_color> <variant>
```

**Example stream:**
```
CLEAR
DRAW 14 22 forest blight_3 dark_green black 0
DRAW 15 22 forest blight_3 dark_green black 0
DRAW 16 22 holy_ground none gold black 1
DRAW 16 22 holy_ground none gold black 2
DRAW 10 5 player none white black 0
DRAW 10 5 player none white black 0
STATUS Faith:80 Warmth:60 Hunger:40 Corrupt:15 Blight:20
MSG You are hungry. The blight creeps.
```

### 3.2 Command Reference

| Command | Args | Description |
|---------|------|-------------|
| `CLEAR` | none | Full screen redraw incoming. Client should clear buffer. |
| `DRAW` | x y tile state fg bg variant | Draw a single cell. |
| `STATUS` | key:value pairs | Sidebar stat update. |
| `MSG` | text | Message log line. |
| `SOUND` | id | Audio cue (ignored by terminal client). |
| `MODE` | ascii / tileset | Client should switch rendering mode. |
| `VIEWPORT` | w h | Viewport size changed. |
| `SEASON` | name | Season changed (for ambient effects). |
| `TIME` | hour | In-game hour (for day/night tint). |

### 3.3 Tile Types (Logical, Not Visual)

The engine only knows these logical types:

| Tile Type | States | Description |
|-----------|--------|-------------|
| `empty` | `unexplored`, `explored` | Plains / ground |
| `forest` | `clean`, `tainted`, `blighted`, `corrupted`, `hell` | The Black Pines |
| `water` | `open`, `ice`, `cracking`, `broken` | The Frozen Straits |
| `holy_ground` | `dim`, `bright`, `pulse` | Consecrated land |
| `blight_fog` | `low`, `high` | Blight overlay |
| `structure` | `wall`, `door`, `brazier`, `altar` | Player-built |
| `item` | `loot`, `food`, `tool`, `corrupted` | Dropped items |
| `creature` | `player`, `wolf`, `wendigo`, `shadow`, `drowned`, `stag`, `eye` | Living things |
| `elevated` | `slope`, `ridge`, `peak` | The Bluffs |

**Note:** The engine never says `^` or `pine_tree.png`. It says `forest` + `clean`. The client decides what that looks like.

### 3.4 State Flags

State flags modify the tile without changing its type:

| Flag | Meaning |
|------|---------|
| `none` | Default state |
| `blight_1` to `blight_5` | Blight intensity (maps to 0-100 range) |
| `consecrated` | Tile is on holy ground |
| `frozen` | Water is ice |
| `cracking` | Ice is unstable |
| `lit` | Tile has a light source |
| `hidden` | FoW: tile is explored but not currently visible |
| `unknown` | FoW: tile is unexplored |

### 3.5 Colors

Colors are named, not ANSI codes. The client maps them:

| Named Color | ANSI (Terminal) | Tileset (Future) |
|-------------|-----------------|------------------|
| `black` | 0 | `#000000` |
| `dark_grey` | 8 | `#333333` |
| `light_grey` | 7 | `#aaaaaa` |
| `white` | 15 | `#ffffff` |
| `dark_green` | 2 | `#228b22` |
| `light_green` | 10 | `#90ee90` |
| `dark_cyan` | 6 | `#008b8b` |
| `light_cyan` | 14 | `#e0ffff` |
| `dark_red` | 1 | `#8b0000` |
| `light_red` | 9 | `#ff4500` |
| `dark_purple` | 5 | `#4b0082` |
| `light_purple` | 13 | `#da70d6` |
| `dark_yellow` | 3 | `#b8860b` |
| `light_yellow` | 11 | `#ffd700` |
| `dark_blue` | 4 | `#00008b` |
| `light_blue` | 12 | `#87ceeb` |
| `brown` | 130 | `#8b4513` |
| `orange` | 208 | `#ff8c00` |

### 3.6 Variant

The `variant` field is an integer 0-3 used for animation frames.

- `0`: Default / frame 1
- `1`: Frame 2
- `2`: Frame 3
- `3`: Frame 4

The engine increments variant on a per-tile timer. The client cycles through its animation frames for that variant index. This keeps animation state out of the protocol (no need to send the same cell 30 times per second).

---

## 4. The Glyph Mapping Table

This is the **critical bridge** between engine and display. It lives in a JSON file that ships with the game and can be overridden by mods or tile packs.

### 4.1 Default Mapping (ASCII Mode)

```json
{
  "mode": "ascii",
  "glyphs": {
    "empty:unexplored":    { "char": " ",  "fg": "black", "bg": "black" },
    "empty:explored":      { "char": ".",  "fg": "light_grey", "bg": "black" },
    "forest:clean":        { "char": "^",  "fg": "dark_green", "bg": "black" },
    "forest:tainted":      { "char": ";",  "fg": "dark_green", "bg": "black" },
    "forest:blighted":     { "char": "\"", "fg": "dark_purple", "bg": "black" },
    "forest:corrupted":    { "char": "=",  "fg": "dark_purple", "bg": "black" },
    "forest:hell":         { "char": "%",  "fg": "light_red", "bg": "dark_purple" },
    "water:open":          { "char": "~",  "fg": "dark_cyan", "bg": "black" },
    "water:ice":           { "char": "=",  "fg": "light_cyan", "bg": "black" },
    "water:cracking":      { "char": "-",  "fg": "dark_yellow", "bg": "black" },
    "water:broken":        { "char": "~",  "fg": "dark_cyan", "bg": "black" },
    "holy_ground:dim":     { "char": "+",  "fg": "dark_yellow", "bg": "black" },
    "holy_ground:bright":  { "char": "+",  "fg": "light_yellow", "bg": "black" },
    "holy_ground:pulse":   { "char": "+",  "fg": "white", "bg": "black" },
    "structure:wall":      { "char": "#",  "fg": "brown", "bg": "black" },
    "structure:door":      { "char": "+",  "fg": "brown", "bg": "black" },
    "structure:brazier":   { "char": "*",  "fg": "light_red", "bg": "black" },
    "structure:altar":     { "char": "=",  "fg": "light_yellow", "bg": "black" },
    "item:loot":           { "char": "!",  "fg": "light_yellow", "bg": "black" },
    "item:food":           { "char": "!",  "fg": "light_green", "bg": "black" },
    "item:tool":           { "char": "!",  "fg": "light_blue", "bg": "black" },
    "item:corrupted":      { "char": "!",  "fg": "dark_purple", "bg": "black" },
    "creature:player":     { "char": "@",  "fg": "white", "bg": "black" },
    "creature:wolf":       { "char": "w",  "fg": "dark_red", "bg": "black" },
    "creature:wendigo":    { "char": "W",  "fg": "white", "bg": "black" },
    "creature:shadow":     { "char": "s",  "fg": "dark_purple", "bg": "black" },
    "creature:drowned":    { "char": "z",  "fg": "dark_cyan", "bg": "black" },
    "creature:stag":       { "char": "D",  "fg": "white", "bg": "black" },
    "creature:eye":        { "char": "0",  "fg": "light_red", "bg": "black" },
    "elevated:slope":      { "char": "^",  "fg": "dark_green", "bg": "black" },
    "elevated:ridge":      { "char": "^",  "fg": "light_grey", "bg": "black" },
    "elevated:peak":       { "char": "A",  "fg": "white", "bg": "black" }
  },
  "animations": {
    "water:open": { "frames": ["~", "w"], "speed_ms": 1500 },
    "blight_fog:low": { "frames": ["\"", "="], "speed_ms": 2000 },
    "blight_fog:high": { "frames": ["=", "%"], "speed_ms": 2000 },
    "holy_ground:pulse": { "frames": ["+", "+"], "speed_ms": 3000 },
    "structure:brazier": { "frames": ["*", "^"], "speed_ms": 300 },
    "creature:wendigo": { "frames": ["W", "W"], "speed_ms": 500 }
  }
}
```

### 4.2 Future Tileset Mapping

When the graphics pack releases, the mapping file changes mode and references sprites:

```json
{
  "mode": "tileset",
  "tile_size": 16,
  "spritesheet": "wilds_of_canaan.png",
  "glyphs": {
    "forest:clean":        { "sprite": "pine_tree", "tint": "none" },
    "forest:blighted":     { "sprite": "pine_tree_dead", "tint": "purple" },
    "water:open":          { "sprite": "water", "tint": "none", "animated": true },
    "holy_ground:bright":  { "sprite": "consecrated_earth", "tint": "gold_glow" },
    "creature:player":     { "sprite": "priest_robe", "tint": "none" },
    "creature:wolf":       { "sprite": "wolf", "tint": "none" }
  }
}
```

**The engine does not change.** Only the client and the mapping file change.

---

## 5. Web-Based Prototype (First Version)

The first playable version is a **web application** served from a lightweight Python backend.

### 5.1 Architecture

```
+-------------------------------------------------------------+
|  BROWSER (Client)                                           |
|  + HTML5 Canvas (primary renderer)                          |
|  + WebSocket connection to server                           |
|  + Input handler (keyboard -> WS messages)                  |
|  + Glyph mapper (JSON mapping file)                         |
|  + Animation ticker (client-side frame cycling)             |
+-------------------------------------------------------------+
                           ^
                           |  WebSocket
                           v
+-------------------------------------------------------------+
|  PYTHON SERVER                                              |
|  + Tornado / aiohttp / FastAPI (WebSocket endpoint)         |
|  + Game Engine instance (one per connected player)          |
|  + Pty bridge (engine master fd <-> WebSocket)              |
|  + Static file server (HTML, JS, CSS, mapping JSON)         |
+-------------------------------------------------------------+
```

### 5.2 Why Web First?

- **No installation.** Players visit a URL and play immediately.
- **Cross-platform.** Windows, Mac, Linux, mobile browsers all work.
- **Easy sharing.** Send a link, not a binary.
- **Fast iteration.** Edit JS, refresh browser. No compile step.
- **Natural path to tile packs.** Canvas already draws images. Swapping ASCII for sprites is a one-line config change.
- **Future multiplayer.** WebSocket architecture supports multiple viewers/spectators naturally.

### 5.3 The Browser Client

**Tech stack:** Vanilla JavaScript + HTML5 Canvas. No frameworks. No dependencies.

**Why vanilla JS:** This is a rendering client, not a web app. It needs to draw 60x20 cells at 60fps with zero overhead. A framework adds nothing and costs frames.

**Canvas setup:**
```javascript
const CELL_W = 12;   // pixels per ASCII cell
const CELL_H = 16;
const VIEWPORT_W = 60;
const VIEWPORT_H = 20;

const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
canvas.width = VIEWPORT_W * CELL_W;
canvas.height = VIEWPORT_H * CELL_H;
```

**Rendering loop:**
```javascript
// Protocol line: DRAW 14 22 forest blight_3 dark_green black 0
function handleDraw(line) {
    const [, x, y, tile, state, fg, bg, variant] = line.split(' ');
    const key = `${tile}:${state}`;
    const glyph = glyphMap[key];

    // Background
    ctx.fillStyle = colorMap[bg];
    ctx.fillRect(x * CELL_W, y * CELL_H, CELL_W, CELL_H);

    // Character
    ctx.fillStyle = colorMap[fg];
    ctx.font = `${CELL_H}px monospace`;
    ctx.fillText(glyph.char, x * CELL_W, (y + 1) * CELL_H - 2);
}
```

**Animation:** The client maintains a `lastVariant` per cell. When `variant` changes, it looks up the animation frame for that tile type and cycles. The engine only sends variant changes every N ticks, not every frame.

**Input:** Keyboard events are captured and sent as WebSocket messages:
```javascript
document.addEventListener('keydown', (e) => {
    ws.send(`INPUT ${e.key}`);
});
```

### 5.4 The Python Server

**Framework:** `aiohttp` (async, simple, handles WebSocket and static files).

**Server structure:**
```python
import asyncio
import os
import pty
from aiohttp import web

class GameSession:
    def __init__(self):
        self.master_fd, self.slave_fd = pty.openpty()
        self.engine = subprocess.Popen(
            ['./engine', '--slave', str(self.slave_fd)],
            pass_fds=[self.slave_fd]
        )
        os.close(self.slave_fd)

    async def read_loop(self, ws):
        loop = asyncio.get_event_loop()
        while True:
            data = await loop.run_in_executor(None, os.read, self.master_fd, 1024)
            for line in data.decode().strip().split('\n'):
                await ws.send_str(line)

    def send_input(self, key):
        os.write(self.master_fd, f"INPUT {key}\n".encode())

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    session = GameSession()
    asyncio.create_task(session.read_loop(ws))
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            session.send_input(msg.data)
    return ws

app = web.Application()
app.router.add_get('/ws', websocket_handler)
app.router.add_static('/', path='static/')
web.run_app(app, port=8080)
```

**Static files:**
```
static/
  index.html
  game.js
  style.css
  glyphs_ascii.json    # The mapping table
```

### 5.5 HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>The Wilds of Canaan</title>
    <style>
        body { background: #000; color: #ccc; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
        canvas { image-rendering: pixelated; border: 1px solid #333; }
        #sidebar { position: fixed; right: 0; top: 0; width: 200px; background: #111; padding: 10px; font-family: monospace; }
        #log { position: fixed; bottom: 0; left: 0; width: calc(100% - 220px); height: 80px; background: #111; padding: 10px; font-family: monospace; overflow-y: auto; }
    </style>
</head>
<body>
    <canvas id="game"></canvas>
    <div id="sidebar">
        <div>Faith: <span id="faith">80%</span></div>
        <div>Warmth: <span id="warmth">60%</span></div>
        <div>Hunger: <span id="hunger">40%</span></div>
        <div>Corrupt: <span id="corrupt">15%</span></div>
        <div>Blight: <span id="blight">20%</span></div>
        <div>Season: <span id="season">Winter</span></div>
        <div>Time: <span id="time">Night 3:14 AM</span></div>
    </div>
    <div id="log"></div>
    <script src="game.js"></script>
</body>
</html>
```

---

## 6. The Engine Binary

The engine is a **single Python script** with no GUI dependencies. It reads from stdin and writes to stdout (or the pty master).

### 6.1 Engine Startup Modes

```bash
# Local mode: creates its own pty, renders via built-in ANSI client
./engine --local

# Slave mode: reads/writes on the given fd (used by server)
./engine --slave 12

# Headless mode: reads stdin, writes stdout (for debugging)
./engine --headless
```

### 6.2 Engine Input

The engine accepts these commands on its input stream:

| Input | Description |
|-------|-------------|
| `INPUT <key>` | Player pressed a key (arrow keys mapped to names) |
| `RESIZE <w> <h>` | Client viewport resized |
| `SAVE` | Trigger save to disk |
| `LOAD <slot>` | Load save slot |
| `QUIT` | Graceful shutdown |

### 6.3 Engine Output

The engine outputs the protocol lines described in Section 3. It batches changes and emits a `FLUSH` line when the frame is complete:

```
DRAW 10 5 player none white black 0
DRAW 11 5 forest clean dark_green black 0
STATUS Faith:80 Warmth:60
MSG You are hungry.
FLUSH
```

The client should buffer all lines between `CLEAR`/`FLUSH` and render them atomically to avoid tearing.

---

## 7. Future: The Tile Pack Release

When the game is ready for a graphics pack, the work is:

1. **Artist creates spritesheet** (e.g., 256x256 PNG with 16x16 tiles).
2. **Artist creates `glyphs_tileset.json`** mapping logical tiles to sprite coordinates.
3. **Player drops both files** into a `mods/` directory.
4. **Web client detects the mod** and switches `mode` to `tileset`.
5. **Engine is untouched.**

### 7.1 Tileset Client Changes

```javascript
const TILE_SIZE = 16;
const spritesheet = new Image();
spritesheet.src = 'wilds_of_canaan.png';

function drawTileset(x, y, spriteX, spriteY, tint) {
    ctx.drawImage(
        spritesheet,
        spriteX * TILE_SIZE, spriteY * TILE_SIZE,
        TILE_SIZE, TILE_SIZE,
        x * TILE_SIZE, y * TILE_SIZE,
        TILE_SIZE, TILE_SIZE
    );
    // Apply tint overlay if needed
}
```

The only code change in the client is: "if mode is tileset, use `drawImage` instead of `fillText`."

### 7.2 Mod Directory Structure

```
mods/
  default/
    glyphs.json          # ASCII mapping (ships with game)
  wilds_hd/
    glyphs.json          # Tileset mapping
    spritesheet.png      # 16x16 or 32x32 tiles
    ambient.mp3          # Optional: replaces default audio
    ui.css               # Optional: custom web UI styling
```

The player selects the mod in the browser:
```javascript
const mod = localStorage.getItem('mod') || 'default';
const glyphMap = await fetch(`mods/${mod}/glyphs.json`).then(r => r.json());
```

---

## 8. Multiplayer Considerations (Future)

The pty/WebSocket architecture naturally supports spectators and shared worlds:

- **Spectator mode:** Multiple WebSockets connect to the same engine master fd. All viewers see the same stream. Input from non-owner clients is ignored.
- **Co-op mode:** The engine accepts multiple `INPUT` streams, each tagged with a player ID. The protocol extends:
  ```
  DRAW 10 5 player:priest none white black 0
  DRAW 12 8 player:woodsman none white black 0
  ```
- **Dedicated server:** The engine runs as a systemd service. Players connect via WebSocket. Saves are server-side.

None of this requires engine rearchitecture. It only requires protocol extensions.

---

## 9. Development Roadmap (Web Prototype)

| Phase | Deliverable | Stack |
|-------|-------------|-------|
| **Week 1-2** | Protocol + headless engine + basic world gen | Python |
| **Week 3** | WebSocket server + static file serving | Python aiohttp |
| **Week 4** | Browser Canvas client (ASCII rendering) | Vanilla JS |
| **Week 5** | Input handling, movement, basic UI | JS + CSS |
| **Week 6** | Blight system, consecration, day/night | Python + JS |
| **Week 7** | One Vocation (Priest), one region (Shallows) | Full stack |
| **Week 8** | First Manifestation (Drowned Choir) | Full stack |
| **Week 9-10** | Remaining Vocations, regions, bestiary | Full stack |
| **Week 11-12** | The Chronicle, endings, polish | Full stack |

**Milestone:** Week 7 should produce a playable web demo. A Priest on the Shallows, building a chapel, surviving wolves, and attempting the first Rite.

---

## 9.1 World Generation & Seeds

The world is generated from a **numeric seed** (hex string, e.g., `7f3a9c`). The seed determines:
- Great Lakes geometry (peninsula shapes, water bodies, forest density)
- Resource placement (veins, groves, springs, deposits)
- Blight seed points (corruption origin points)
- Lost Scripture locations (which ruins hold which fragments)
- Pilgrim spawn points
- Manifestation arena layouts

**What the seed does NOT change:**
- The 5 region types always exist
- Winter arrives on Day 30
- Tier unlock order is fixed
- Fundamental scarcity ratios

**Protocol:**
```
SEED <hex_string>
```
Sent once at world start so the client can display it (top bar) and the player can share/save it.

**Engine startup with seed:**
```bash
./engine --seed 7f3a9c --local
./engine --seed random --slave 12
```

If no seed is provided, the engine generates one from system time and emits it via `SEED`.

## 9.2 Dynamic Viewport

The engine adapts to client viewport size:

**Client to Engine:**
```
RESIZE <w> <h>
```
Sent when the browser window is resized. The engine only emits cells within the player's view plus a 5-tile buffer.

**Engine to Client:**
```
VIEWPORT <w> <h>
```
The engine's maximum render area. The client should not request larger than this.

**Zoom levels (client-side only):**
```
ZOOM <level>
```
Where level is `far` (10x12 cells), `normal` (14x18 cells), or `close` (20x24 cells). The client adjusts CELL_W/H and sends a new `RESIZE`.

**Performance note:** At 100x45 (4,500 cells), the engine batches all changed cells into a single `FLUSH` frame. At 120x60 (7,200 cells), the same. The protocol is lightweight enough that viewport size does not significantly impact server load.

## 9.3 Architecture: Browser-Only Prototype, Backend Later

### 9.3.1 The Three-Phase Approach

The Wilds of Canaan uses a **three-phase architecture strategy**:

| Phase | Architecture | Stack | Hosting | Cost | Timeline |
|-------|-------------|-------|---------|------|----------|
| **Prototype** | Browser-only | TypeScript engine + Canvas client, Web Worker | GitHub Pages / Vercel / Netlify | $0 | Weeks 1-12 |
| **Beta** | Optional backend | Same browser client + Python/Go backend for cloud saves | $6 droplet | $6/mo | Post-prototype |
| **Production** | Full backend | Go backend + JS client | $6-24 droplet | $6-24/mo | Launch |

### 9.3.2 Why Browser-Only for the Prototype

**The prototype does not need a backend.** A backend adds cost, complexity, and deployment friction for zero benefit at this stage.

| Factor | Browser-Only | Backend Required |
|--------|-------------|------------------|
| **Deploy** | `git push` to GitHub Pages | Provision droplet, manage process |
| **Cost** | $0 | $6-24/month |
| **Iteration** | Refresh browser | Restart server, redeploy |
| **Offline** | Works after first load | Requires connection |
| **Debugging** | Chrome DevTools | SSH, tail logs |
| **Share** | URL with `?seed=7f3a9c` | URL + hope server is up |
| **Saves** | localStorage (auto) | SQLite/JSON on server |

**What you lose (and do not need yet):**
- Multiplayer / spectators
- Server-side anti-cheat
- Shared leaderboards
- Cross-device cloud saves

All of these are post-prototype features.

### 9.3.3 Browser-Only Architecture

```
+-------------------------------------------------------------+
|  BROWSER TAB                                                |
|                                                             |
|  +---------------------+                                    |
|  |  ENGINE (Web Worker)|  <-- TypeScript world sim          |
|  |  - World gen        |      (blight, AI, combat, crafting) |
|  |  - Blight sim       |                                    |
|  |  - Combat resolve   |      Emits protocol lines:         |
|  |  - AI               |      DRAW, STATUS, MSG, FLUSH      |
|  +---------------------+                                    |
|           ^                                                 |
|           | postMessage                                     |
|  +---------------------+                                    |
|  |  CLIENT (main thread)|                                   |
|  |  - Canvas renderer    |   Consumes protocol lines        |
|  |  - Input capture      |   Renders grid, sidebar, log     |
|  |  - UI/sidebar         |                                  |
|  +---------------------+                                    |
|                                                             |
|  localStorage: saves, Chronicle, settings, seed history     |
+-------------------------------------------------------------+
```

**The engine is a TypeScript class running in a Web Worker.** Heavy computation (world-gen, pathfinding, blight spread) happens off the main thread so the renderer stays at 60fps.

**The protocol is internal.** Instead of WebSocket, it is a `postMessage` call:

```typescript
// engine.worker.ts
self.onmessage = (e) => {
    const cmd = e.data;  // {type: 'INPUT', key: 'move_east'}
    engine.handleInput(cmd);

    // Batch changed cells and emit
    const lines = engine.flushProtocol();
    self.postMessage({type: 'PROTOCOL', lines});
};

// client.ts (main thread)
const worker = new Worker('engine.worker.js');

worker.onmessage = (e) => {
    if (e.data.type === 'PROTOCOL') {
        for (const line of e.data.lines) {
            handleProtocolLine(line);  // Same function WebSocket version uses
        }
    }
};

// Send input
worker.postMessage({type: 'INPUT', key: 'move_east'});
```

**The client code is identical to the backend version.** The `handleProtocolLine` function does not care if the line came from a WebSocket or a Web Worker. This means the migration to backend later requires zero client changes.

### 9.3.4 Why TypeScript for the Engine

| Factor | TypeScript | Python | Go |
|--------|-----------|--------|-----|
| **Runs in browser** | Native | No (needs backend) | No (needs backend) |
| **Type safety** | Strong | Dynamic | Strong |
| **Iteration speed** | Fast (no compile) | Fast (no compile) | Medium (compile) |
| **Debug** | Chrome DevTools | pdb / print | Delve |
| **Share prototype** | GitHub Pages | Droplet + process | Droplet + binary |
| **Port to backend later** | Extract logic, port to Go | Rewrite in Go | Already done |

**TypeScript is the pragmatic choice for the prototype:** it runs where the game runs (the browser), it shares types with the client, and it can be ported to Go later without architectural changes.

### 9.3.5 Save System (localStorage)

The prototype uses `localStorage` for persistence:

```typescript
// Save world state
localStorage.setItem('canaan_save', JSON.stringify(engine.serialize()));

// Save Chronicle
localStorage.setItem('canaan_chronicle', JSON.stringify(chronicle.entries));

// Save seed history
const seeds = JSON.parse(localStorage.getItem('canaan_seeds') || '[]');
seeds.push({seed: currentSeed, survived: days, vocation: 'priest'});
localStorage.setItem('canaan_seeds', JSON.stringify(seeds));
```

**Limitations:**
- ~5MB limit per origin (sufficient for world state + Chronicle).
- Browser-specific (cannot continue on another device).
- User can clear it (intentional for Ironman feel).

**For beta:** Add optional backend cloud save. The client POSTs save JSON to a simple endpoint. The server stores it. The client can GET it back. The save format does not change.

### 9.3.6 The Migration Path to Backend

When ready for backend (beta or production):

1. **Extract engine logic.** The TypeScript engine is already isolated in a Web Worker. Port it to Go (or keep in JS and run server-side with Node/Deno).
2. **Replace `postMessage` with WebSocket.** The protocol does not change. The client already parses `DRAW` lines.
3. **Move saves from localStorage to server.** The save format (JSON) does not change.
4. **Deploy binary to droplet.** Done.

**What changes:**
- Engine language: TypeScript -> Go
- Transport: Web Worker `postMessage` -> WebSocket
- Save location: localStorage -> server database

**What does NOT change:**
- Client code (Canvas renderer, input handling, UI)
- Protocol format (`DRAW x y tile state fg bg variant`)
- Save format (JSON world state)
- Static files (HTML, CSS, glyph mapping JSON)

### 9.3.7 When to Add a Backend

**Stay browser-only if:**
- The prototype is not yet playable end-to-end.
- You are still iterating on core mechanics.
- You have <100 active playtesters.
- You want zero hosting cost.

**Add a backend when:**
- You want cloud saves (play on laptop, continue on desktop).
- You want shared leaderboards ("Longest survival: 47 days").
- You want multiplayer (co-op, spectators).
- You want server-side validation (anti-cheat for competitive modes).
- You outgrow localStorage (unlikely for a single-player ASCII game).

**The rule:** Do not build a backend until the browser-only prototype proves the game is fun. A backend cannot fix bad design.

### 9.3.8 Hosting the Prototype

**Recommended: GitHub Pages (free)**

```bash
# Build the TypeScript
cd canaan-prototype
npm run build  # outputs to dist/

# Deploy to GitHub Pages
git subtree push --prefix dist origin gh-pages

# Game is live at:
# https://yourusername.github.io/canaan/?seed=7f3a9c
```

**Alternatives:**
- **Vercel:** Zero-config deploy on `git push`. Automatic previews for PRs.
- **Netlify:** Same. Drag-and-drop folder deploy.
- **Cloudflare Pages:** Fast CDN, generous free tier.

All of these support custom domains, HTTPS, and global CDN. For a static HTML/JS/Canvas game, they are identical in capability.

## 10. Summary

| Component | Technology | Responsibility |
|-----------|-----------|----------------|
| **Engine** | Python (headless) | World sim, logic, saves |
| **Protocol** | Custom text stream | Decouples engine from display |
| **Server** | Python aiohttp | WebSocket bridge, static files |
| **Web Client** | Vanilla JS + Canvas | Rendering, input, animation |
| **Terminal Client** | Python + ANSI | Future: SSH/local play |
| **Tile Pack** | PNG + JSON mod | Future: graphics override |

The golden rule: **The engine never draws. The client never simulates.** The protocol line between them is thin, text-based, and completely replaceable.

---

Document Version 1.0
The Wilds of Canaan - Technical Architecture Document
