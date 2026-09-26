"""Terminal client: consumes the engine protocol and renders ANSI ASCII.

Reads protocol lines (from a pipe or by launching the engine itself) and
draws the world to the terminal. Contains no simulation logic.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time

# Named protocol colors -> ANSI codes (Architecture doc §3.5).
ANSI_COLORS = {
    "black": 0, "dark_red": 1, "dark_green": 2, "dark_yellow": 3,
    "dark_blue": 4, "dark_purple": 5, "dark_cyan": 6, "light_grey": 7,
    "dark_grey": 8, "light_red": 9, "light_green": 10, "light_yellow": 11,
    "light_blue": 12, "light_purple": 13, "light_cyan": 14, "white": 15,
    "brown": 130, "orange": 208,
}

# tile_type:state -> ASCII glyph (subset of the default mapping, §4.1).
GLYPHS = {
    ("empty", "unexplored"): " ",
    ("empty", "explored"): ".",
    ("forest", "clean"): "^",
    ("forest", "tainted"): ";",
    ("forest", "blighted"): '"',
    ("forest", "corrupted"): "=",
    ("forest", "hell"): "%",
    ("water", "open"): "~",
    ("water", "ice"): "=",
    ("holy_ground", "dim"): "+",
    ("holy_ground", "bright"): "+",
    ("elevated", "slope"): "^",
    ("elevated", "ridge"): "^",
    ("elevated", "peak"): "A",
    ("creature", "player"): "@",
    ("creature", "wolf"): "w",
    ("creature", "wendigo"): "W",
}

# Animations (ASCII Visual Design §2.5, §9.5): open water cycles
# ~ -> w -> ~ every 1.5s; blighted forest breathes " <-> = every 2.5s.
# Purely presentational. (frames, period_ms)
ANIM = {
    ("water", "open"): (["~", "w", "~"], 1500),
    ("forest", "blighted"): (['"', "="], 2500),
    ("forest", "corrupted"): (['"', "="], 2500),
}


def anim_char(key: tuple[str, str], char: str, now_ms: float) -> str:
    """Animation frame for a tile at time now_ms; static tiles unchanged."""
    entry = ANIM.get(key)
    if entry is None:
        return char
    frames, period = entry
    return frames[int(now_ms // period) % len(frames)]


def fg(code: int) -> str:
    return f"\x1b[38;5;{code}m"


def bg(code: int) -> str:
    return f"\x1b[48;5;{code}m"


RESET = "\x1b[0m"


class TerminalClient:
    def __init__(self):
        self.grid: dict[tuple[int, int], tuple[str, str, str]] = {}
        self.status: dict[str, str] = {}
        self.messages: list[str] = []
        self.seed = None
        self.hour = None

    def handle_line(self, line: str) -> None:
        parts = line.rstrip("\n").split(" ", 6)
        if not parts or not parts[0]:
            return
        cmd = parts[0]
        if cmd == "SEED":
            self.seed = parts[1]
        elif cmd == "CLEAR":
            self.grid.clear()
        elif cmd == "DRAW" and len(parts) >= 7:
            _, x, y, tile, state, fg_name, rest = parts
            bg_name = rest.split(" ", 1)[0]
            self.grid[(int(x), int(y))] = (tile, state, f"{fg_name} {bg_name}")
        elif cmd == "STATUS":
            for pair in parts[1].split():
                if ":" in pair:
                    k, v = pair.split(":", 1)
                    self.status[k] = v
        elif cmd == "MSG":
            self.messages.append(line[4:].rstrip("\n"))
        elif cmd == "TIME":
            self.hour = parts[1]
        elif cmd == "FLUSH":
            self.render()

    def render(self) -> None:
        if not self.grid:
            return
        max_x = max(x for x, _ in self.grid)
        max_y = max(y for _, y in self.grid)
        term = shutil.get_terminal_size((120, 50))
        out = ["\x1b[H"]  # cursor home (assumes screen cleared at start)
        header = f"THE WILDS OF CANAAN  seed:{self.seed}  hour:{self.hour}"
        out.append(header[: term.columns - 1])
        for y in range(min(max_y + 1, term.lines - 6)):
            row = []
            for x in range(min(max_x + 1, term.columns - 1)):
                cell = self.grid.get((x, y))
                if cell is None:
                    row.append(" ")
                    continue
                tile, state, colors = cell
                fg_name, bg_name = colors.split(" ")
                char = anim_char((tile, state),
                                 GLYPHS.get((tile, state), "?"),
                                 time.monotonic() * 1000)
                row.append(
                    fg(ANSI_COLORS.get(fg_name, 15))
                    + bg(ANSI_COLORS.get(bg_name, 0))
                    + char + RESET)
            out.append("".join(row))
        stats = "  ".join(f"{k}:{v}" for k, v in self.status.items())
        out.append(stats)
        for msg in self.messages[-3:]:
            out.append(msg)
        sys.stdout.write("\n".join(out) + "\n")
        sys.stdout.flush()


def run(seed: str, ticks: int, fps_delay: float) -> None:
    engine = subprocess.Popen(
        [sys.executable, "-m", "canaan", "--seed", seed,
         "--ticks", str(ticks), "--headless"],
        cwd="engine",
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    assert engine.stdout is not None and engine.stdin is not None
    # This client is a non-interactive replay viewer: close stdin so the
    # engine sees EOF and idles out the requested ticks.
    engine.stdin.close()
    sys.stdout.write("\x1b[2J")  # clear screen once
    client = TerminalClient()
    try:
        for line in engine.stdout:
            client.handle_line(line)
            if line.startswith("FLUSH"):
                # Re-render during the inter-tick delay so water and
                # blight animations cycle between engine frames.
                deadline = time.monotonic() + fps_delay
                while time.monotonic() < deadline:
                    client.render()
                    time.sleep(min(0.15, max(0.0,
                                   deadline - time.monotonic())))
    finally:
        engine.wait()
        sys.stdout.write(RESET + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Canaan terminal client")
    parser.add_argument("--seed", default="random")
    parser.add_argument("--ticks", type=int, default=60)
    parser.add_argument("--fps", type=float, default=10,
                        help="frames per second to replay ticks at")
    args = parser.parse_args()
    run(args.seed, args.ticks, 1.0 / args.fps)


if __name__ == "__main__":
    main()
