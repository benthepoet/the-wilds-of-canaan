"""Blight spread mechanic.

The Blight spreads from seeded origin points into neighbouring land tiles.
Per the roadmap, the full escalation rules (1 tile/day, 2 after Day 20,
surges after Day 40) arrive in Phase 4; this skeleton spreads a small
amount per blight tick so the spread is visible and testable.
"""

from __future__ import annotations

import random

from .world import MAX_BLIGHT, WALKABLE, World

# Blight level increase per blight tick for tiles adjacent to blighted ones.
SPREAD_RATE = 25
# A tile becomes a spreader itself once it passes this level.
ACTIVE_THRESHOLD = 50


def blight_tick(world: World, rng: random.Random,
                surge: bool = False) -> list[tuple[int, int]]:
    """Advance the blight one step. Returns the list of cells that changed.

    Blight only spreads into walkable land (never into water, never into
    consecrated holy ground), and only from tiles whose blight level has
    passed ACTIVE_THRESHOLD. When ``surge`` is set (Day 40+), the blight
    additionally leaps up to 5 tiles in a random direction from a random
    active tile.
    """
    changed: list[tuple[int, int]] = []
    active = [
        (x, y)
        for y in range(world.height)
        for x in range(world.width)
        if world.tile(x, y).blight >= ACTIVE_THRESHOLD
    ]
    for x, y in active:
        for nx, ny in world.neighbors4(x, y):
            tile = world.tile(nx, ny)
            if tile.terrain not in WALKABLE or tile.holy:
                continue
            if tile.blight >= MAX_BLIGHT:
                continue
            tile.blight = min(MAX_BLIGHT, tile.blight + SPREAD_RATE)
            changed.append((nx, ny))

    if surge and active:
        sx, sy = rng.choice(active)
        dx, dy = rng.choice(((0, 1), (0, -1), (1, 0), (-1, 0)))
        for step in range(1, 6):
            nx, ny = sx + dx * step, sy + dy * step
            if not world.in_bounds(nx, ny):
                break
            tile = world.tile(nx, ny)
            if tile.terrain not in WALKABLE or tile.holy:
                break
            tile.blight = MAX_BLIGHT
            changed.append((nx, ny))
    return changed
