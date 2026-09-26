"""Protocol emitter for the headless engine.

Implements the text protocol from the Technical Architecture doc §3:
one line per logical rendering command, batched between frames and
terminated by FLUSH. The engine writes these lines; clients parse them.
"""

from __future__ import annotations

import sys
from typing import IO


class ProtocolEmitter:
    """Writes protocol lines to an output stream (stdout, pty, socket)."""

    def __init__(self, out: IO[str] | None = None):
        self._out = out if out is not None else sys.stdout

    def _write(self, line: str) -> None:
        self._out.write(line + "\n")

    def seed(self, seed_hex: str) -> None:
        self._write(f"SEED {seed_hex}")

    def clear(self) -> None:
        self._write("CLEAR")

    def draw(self, x: int, y: int, tile: str, state: str,
             fg: str, bg: str, variant: int = 0) -> None:
        self._write(f"DRAW {x} {y} {tile} {state} {fg} {bg} {variant}")

    def status(self, **stats: int | str) -> None:
        pairs = " ".join(f"{k}:{v}" for k, v in stats.items())
        self._write(f"STATUS {pairs}")

    def msg(self, text: str) -> None:
        self._write(f"MSG {text}")

    def sound(self, sound_id: str) -> None:
        self._write(f"SOUND {sound_id}")

    def viewport(self, w: int, h: int) -> None:
        self._write(f"VIEWPORT {w} {h}")

    def time(self, hour: int) -> None:
        self._write(f"TIME {hour}")

    def flush(self) -> None:
        self._write("FLUSH")
        self._out.flush()


def parse_input(line: str) -> tuple[str, list[str]] | None:
    """Parse an engine input line into (command, args), or None if unknown.

    Supported inputs (Architecture §6.2): INPUT, RESIZE, SAVE, LOAD, QUIT.
    """
    parts = line.strip().split()
    if not parts:
        return None
    cmd, args = parts[0].upper(), parts[1:]
    if cmd not in {"INPUT", "RESIZE", "SAVE", "LOAD", "QUIT"}:
        return None
    return cmd, args
