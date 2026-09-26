/* The Wilds of Canaan — browser client (M2).
 * Vanilla JS, no dependencies. Consumes the engine protocol over SSE and
 * renders it to canvas. Sends keystrokes back via POST /input.
 * The client never simulates; it only parses DRAW/STATUS/MSG/etc.
 */

// Named protocol colors -> CSS (Architecture doc §3.5).
const COLORS = {
    black: "#000000", dark_grey: "#333333", light_grey: "#aaaaaa",
    white: "#ffffff", dark_green: "#228b22", light_green: "#90ee90",
    dark_cyan: "#008b8b", light_cyan: "#e0ffff", dark_red: "#8b0000",
    light_red: "#ff4500", dark_purple: "#4b0082", light_purple: "#da70d6",
    dark_yellow: "#b8860b", light_yellow: "#ffd700", dark_blue: "#00008b",
    light_blue: "#87ceeb", brown: "#8b4513", orange: "#ff8c00",
};

// tile_type:state -> ASCII glyph (same subset as the terminal client).
const GLYPHS = {
    "empty:unexplored": " ", "empty:explored": ".",
    "forest:clean": "^", "forest:tainted": ";", "forest:blighted": "\"",
    "forest:corrupted": "=", "forest:hell": "%",
    "water:open": "~", "water:ice": "=",
    "holy_ground:dim": "+", "holy_ground:bright": "+",
    "elevated:slope": "^", "elevated:ridge": "^", "elevated:peak": "A",
    "creature:player": "@", "creature:wolf": "w", "creature:wendigo": "W",
};

// Compact fixed cell size; the camera scrolls over the world rather than
// scaling cells to fill the window.
const CELL_W = 9, CELL_H = 13;
const FONT_STACK = 'ui-monospace, Menlo, Consolas, "Liberation Mono", monospace';

// Pure camera math (also exercised by tests/camera_check.js via node):
// center the view on the player, clamped so the view never leaves the map.
// If the map is smaller than the view on an axis, the camera pins to 0.
function cameraOrigin(px, py, viewW, viewH, worldW, worldH) {
    const cx = Math.max(0, Math.min(px - Math.floor(viewW / 2),
                                    worldW - viewW));
    const cy = Math.max(0, Math.min(py - Math.floor(viewH / 2),
                                    worldH - viewH));
    return [cx, cy];
}

const SEED = new URLSearchParams(location.search).get("seed") || "random";
document.getElementById("seed").textContent = SEED;

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

// World buffer: (x,y) -> {char, fg, bg}. Filled between CLEAR and FLUSH.
let pending = new Map();
let world = new Map();
let worldW = 60, worldH = 40;
let playerX = 0, playerY = 0;

// Viewport size in cells follows the canvas pixel size; cells stay fixed.
let viewW = 40, viewH = 25;
function resize() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;
    viewW = Math.max(1, Math.floor(canvas.width / CELL_W));
    viewH = Math.max(1, Math.floor(canvas.height / CELL_H));
    render();
}
window.addEventListener("resize", resize);

function render() {
    ctx.fillStyle = "#0a0a0a";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.font = CELL_H + "px " + FONT_STACK;
    ctx.textBaseline = "top";
    const [camX, camY] = cameraOrigin(playerX, playerY, viewW, viewH,
                                      worldW, worldH);
    for (const [key, cell] of world) {
        const [x, y] = key.split(",").map(Number);
        const sx = x - camX, sy = y - camY;
        if (sx < 0 || sy < 0 || sx >= viewW || sy >= viewH) continue;
        if (cell.bg !== "black") {
            ctx.fillStyle = COLORS[cell.bg] || "#000";
            ctx.fillRect(sx * CELL_W, sy * CELL_H, CELL_W, CELL_H);
        }
        ctx.fillStyle = COLORS[cell.fg] || "#fff";
        ctx.fillText(cell.char, sx * CELL_W, sy * CELL_H);
    }
}

function handleLine(line) {
    const parts = line.split(" ");
    const cmd = parts[0];
    if (cmd === "SEED") {
        document.getElementById("seed").textContent = parts[1];
    } else if (cmd === "CLEAR") {
        pending = new Map();
    } else if (cmd === "DRAW") {
        const [_, x, y, tile, state, fg, bg] = parts;
        const char = GLYPHS[tile + ":" + state] || "?";
        pending.set(x + "," + y, { char, fg, bg });
        worldW = Math.max(worldW, Number(x) + 1);
        worldH = Math.max(worldH, Number(y) + 1);
        if (tile === "creature" && state === "player") {
            playerX = Number(x);
            playerY = Number(y);
        }
    } else if (cmd === "STATUS") {
        document.getElementById("stats").innerHTML =
            parts.slice(1).map(p => p.replace(":", ": ")).join("<br>");
    } else if (cmd === "MSG") {
        const log = document.getElementById("log");
        log.innerHTML += line.slice(4) + "<br>";
        log.scrollTop = log.scrollHeight;
    } else if (cmd === "FLUSH") {
        world = pending;
        pending = new Map();
        render();
    }
}

const source = new EventSource("/stream?seed=" + encodeURIComponent(SEED));
source.onmessage = (e) => handleLine(e.data);

const KEYS = {
    ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right",
    w: "w", a: "a", s: "s", d: "d",
    h: "h", j: "j", k: "k", l: "l",
    g: "g", c: "c",
};
document.addEventListener("keydown", (e) => {
    const key = KEYS[e.key] || KEYS[e.key.toLowerCase()];
    if (!key) return;
    e.preventDefault();
    fetch("/input?seed=" + encodeURIComponent(SEED) + "&key=" + key,
          { method: "POST" });
});

resize();
