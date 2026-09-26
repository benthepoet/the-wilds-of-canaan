"""Simulation core: tick loop, player entity, protocol rendering.

The Game owns the World, advances the simulation one tick at a time, and
emits protocol frames through a ProtocolEmitter. It contains no drawing
code — it only describes world state as protocol lines.
"""

from __future__ import annotations

import random
import secrets
import sys
from dataclasses import dataclass
from typing import IO

from .blight import blight_tick
from .protocol import ProtocolEmitter, parse_input
from .world import COAST, World, generate_world

# One tick = one in-game hour; a day is 24 ticks.
HOURS_PER_DAY = 24
# Blight escalation (roadmap Phase 4 / GDD): 1 spread step per day until
# Day 20, 2 per day after, and from Day 40 it additionally surges.
BLIGHT_INTERVAL_EARLY = 24
BLIGHT_INTERVAL_LATE = 12
SURGE_DAY = 40

# Consecration: cleanses radius 1 around the player, costs Faith.
CONSECRATE_RADIUS = 1
CONSECRATE_FAITH_COST = 5
# Gathering blighted wood raises Corruption.
BLIGHTED_WOOD_CORRUPT = 2

MOVE_KEYS = {
    "up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
    "w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0),
    "k": (0, -1), "j": (0, 1), "h": (-1, 0), "l": (1, 0),
}


@dataclass
class Player:
    x: int
    y: int
    faith: int = 80
    warmth: int = 60
    hunger: int = 40
    corrupt: int = 0
    wood: int = 0
    blighted_wood: int = 0


def _tile_glyph(world: World, x: int, y: int) -> tuple[str, str, str, str]:
    """Map a world tile to (tile_type, state, fg, bg) protocol fields."""
    tile = world.tile(x, y)
    if tile.holy:
        return "holy_ground", "bright", "light_yellow", "black"
    if tile.terrain == "water":
        return "water", "open", "dark_cyan", "black"
    if tile.terrain == COAST:
        return "empty", "explored", "brown", "black"
    if tile.terrain == "forest":
        b = tile.blight
        if b <= 0:
            return "forest", "clean", "dark_green", "black"
        if b <= 25:
            return "forest", "tainted", "dark_green", "black"
        if b <= 50:
            return "forest", "blighted", "dark_purple", "black"
        if b <= 75:
            return "forest", "corrupted", "dark_purple", "black"
        return "forest", "hell", "light_red", "dark_purple"
    if tile.terrain == "mire":
        return "empty", "explored", "dark_yellow", "black"
    if tile.terrain == "bluffs":
        return "elevated", "ridge", "light_grey", "black"
    return "empty", "explored", "light_grey", "black"


class Game:
    def __init__(self, seed: str | None = None, width: int = 60, height: int = 40,
                 out: IO[str] | None = None):
        if seed in (None, "random"):
            seed = secrets.token_hex(3)
        self.world = generate_world(seed, width, height)
        self.rng = random.Random(f"canaan:sim:{seed}")
        self.player = self._spawn_player()
        self.tick_count = 0
        self.hour = 6  # start at dawn
        self.emitter = ProtocolEmitter(out)
        self.running = True

    @property
    def day(self) -> int:
        return self.tick_count // HOURS_PER_DAY + 1

    def _spawn_player(self) -> Player:
        """Spawn on walkable Shallows coast near the south edge."""
        for y in range(self.world.height - 1, -1, -1):
            for x in range(self.world.width):
                tile = self.world.tile(x, y)
                if tile.terrain == COAST and tile.walkable:
                    return Player(x=x, y=y)
        raise RuntimeError("no walkable coast tile to spawn on")

    def blight_percent(self) -> int:
        land = blighted = 0
        for y in range(self.world.height):
            for x in range(self.world.width):
                t = self.world.tile(x, y)
                if t.walkable:
                    land += 1
                    blighted += t.blight
        if land == 0:
            return 0
        return round(blighted / (land * 100) * 100)

    def tick(self) -> None:
        """Advance the simulation one tick (one in-game hour)."""
        self.tick_count += 1
        self.hour = (self.hour + 1) % 24
        # Escalation: twice-daily spread after Day 20, surges from Day 40.
        interval = (BLIGHT_INTERVAL_LATE if self.day > 20
                    else BLIGHT_INTERVAL_EARLY)
        if self.tick_count % interval == 0:
            blight_tick(self.world, self.rng, surge=self.day > SURGE_DAY)
        self.emit_frame()

    def handle_command(self, line: str) -> None:
        """Handle one input line (INPUT/RESIZE/SAVE/LOAD/QUIT)."""
        parsed = parse_input(line)
        if parsed is None:
            return
        cmd, args = parsed
        if cmd == "QUIT":
            self.running = False
        elif cmd == "INPUT" and args:
            self._action(args[0].lower())

    def _action(self, key: str) -> None:
        if key in MOVE_KEYS:
            self._move(key)
        elif key == "g":
            self._gather()
        elif key == "c":
            self._consecrate()

    def _move(self, key: str) -> None:
        delta = MOVE_KEYS.get(key)
        if delta is None:
            return
        nx, ny = self.player.x + delta[0], self.player.y + delta[1]
        if self.world.in_bounds(nx, ny) and self.world.tile(nx, ny).walkable:
            self.player.x, self.player.y = nx, ny

    def _gather(self) -> None:
        """Chop one adjacent tree (or the tree underfoot) for wood.

        Per the Resource Gathering doc: a single keypress on the correct
        tile, base yield 2-4 pine wood. Wood from a blighted tree is
        blighted wood and raises Corruption.
        """
        p = self.player
        targets = [(p.x, p.y)] + list(self.world.neighbors4(p.x, p.y))
        for x, y in targets:
            tile = self.world.tile(x, y)
            if tile.terrain != "forest" or tile.holy:
                continue
            blighted = tile.blight > 0
            yield_ = self.rng.randint(2, 4)
            tile.terrain = COAST  # felled tree leaves cleared ground
            tile.blight = 0
            if blighted:
                p.blighted_wood += yield_
                p.corrupt += BLIGHTED_WOOD_CORRUPT
                self.emitter.msg(f"You gather {yield_} blighted wood. It festers.")
            else:
                p.wood += yield_
                self.emitter.msg(f"You gather {yield_} pine wood.")
            return
        self.emitter.msg("Nothing to gather here.")

    def _consecrate(self) -> None:
        """Consecrate the ground around the player: cleanse blight and
        mark tiles holy, which blocks future blight spread."""
        p = self.player
        if p.faith < CONSECRATE_FAITH_COST:
            self.emitter.msg("Your faith is too weak to consecrate.")
            return
        p.faith -= CONSECRATE_FAITH_COST
        for dy in range(-CONSECRATE_RADIUS, CONSECRATE_RADIUS + 1):
            for dx in range(-CONSECRATE_RADIUS, CONSECRATE_RADIUS + 1):
                x, y = p.x + dx, p.y + dy
                if not self.world.in_bounds(x, y):
                    continue
                tile = self.world.tile(x, y)
                if tile.walkable:
                    tile.blight = 0
                    tile.holy = True
        self.emitter.msg("The ground turns warm. The blight recoils.")

    def emit_frame(self) -> None:
        """Emit a full frame: CLEAR, all cells, player, status, FLUSH."""
        e = self.emitter
        e.clear()
        for y in range(self.world.height):
            for x in range(self.world.width):
                tile, state, fg, bg = _tile_glyph(self.world, x, y)
                e.draw(x, y, tile, state, fg, bg, 0)
        e.draw(self.player.x, self.player.y, "creature", "player",
               "white", "black", 0)
        e.status(Faith=self.player.faith, Warmth=self.player.warmth,
                 Hunger=self.player.hunger, Corrupt=self.player.corrupt,
                 Blight=self.blight_percent(), Day=self.day,
                 Wood=self.player.wood, BWood=self.player.blighted_wood)
        e.time(self.hour)
        e.flush()

    def run(self, max_ticks: int | None = None,
            input_stream: IO[str] | None = None) -> None:
        """Run the loop: announce seed, emit a frame, then process input.

        In headless mode each input line triggers a tick; with no input
        stream (or EOF) the game idles for max_ticks ticks and exits.
        """
        self.emitter.seed(self.world.seed)
        self.emit_frame()
        if input_stream is None:
            ticks = max_ticks if max_ticks is not None else 1
            for _ in range(ticks):
                self.tick()
            return
        ticks = 0
        for line in input_stream:
            self.handle_command(line)
            if not self.running:
                break
            self.tick()
            ticks += 1
            if max_ticks is not None and ticks >= max_ticks:
                break
        # On EOF (client closed stdin), idle out the remaining ticks so a
        # replay client still receives the full run.
        while self.running and max_ticks is not None and ticks < max_ticks:
            self.tick()
            ticks += 1


def main(argv: list[str] | None = None) -> None:
    import argparse

    parser = argparse.ArgumentParser(
        prog="canaan-engine",
        description="The Wilds of Canaan headless engine (emits protocol lines).")
    parser.add_argument("--seed", default="random",
                        help="world seed (hex string, or 'random')")
    parser.add_argument("--width", type=int, default=60)
    parser.add_argument("--height", type=int, default=40)
    parser.add_argument("--ticks", type=int, default=None,
                        help="max ticks to simulate before exiting")
    parser.add_argument("--headless", action="store_true",
                        help="read commands from stdin, write protocol to stdout")
    args = parser.parse_args(argv)

    game = Game(seed=args.seed, width=args.width, height=args.height)
    if args.headless:
        game.run(max_ticks=args.ticks, input_stream=sys.stdin)
    else:
        game.run(max_ticks=args.ticks or 1)


if __name__ == "__main__":
    main()
