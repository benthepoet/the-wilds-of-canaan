"""World model: tiles, regions, and seed-based procedural generation.

Region layout follows the GDD: the five region types always exist, but the
seed determines the exact geometry (coastline shape, forest density, blight
origin points). For this skeleton, regions are arranged south-to-north:

    Shallows (coast) -> Black Pines (forest) -> Mire -> Bluffs -> Frozen Straits (water/ice)
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

# Terrain kinds, south to north by default.
WATER = "water"
COAST = "coast"      # The Shallows
FOREST = "forest"    # The Black Pines
MIRE = "mire"        # The Mire
BLUFFS = "bluffs"    # The Bluffs

# Fraction of map height given to each region band (south -> north).
REGION_BANDS = [
    (COAST, 0.15),
    (FOREST, 0.45),
    (MIRE, 0.20),
    (BLUFFS, 0.10),
    (WATER, 0.10),  # The Frozen Straits at the north edge
]

WALKABLE = {COAST, FOREST, MIRE, BLUFFS}

MAX_BLIGHT = 100


@dataclass
class Tile:
    terrain: str
    blight: int = 0  # 0..MAX_BLIGHT
    holy: bool = False  # consecrated ground: blocks blight, never blighted

    @property
    def walkable(self) -> bool:
        return self.terrain in WALKABLE


@dataclass
class World:
    width: int
    height: int
    seed: str
    tiles: list[list[Tile]] = field(repr=False, default_factory=list)
    blight_sources: list[tuple[int, int]] = field(default_factory=list)

    def tile(self, x: int, y: int) -> Tile:
        return self.tiles[y][x]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors4(self, x: int, y: int):
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny):
                yield nx, ny


def _value_noise(rng: random.Random, width: int, height: int,
                 cell: int) -> list[list[float]]:
    """Simple smoothed value noise, deterministic for a given Random state."""
    gw, gh = width // cell + 2, height // cell + 2
    grid = [[rng.random() for _ in range(gw)] for _ in range(gh)]

    def sample(gx: int, gy: int) -> float:
        return grid[gy][gx]

    out = []
    for y in range(height):
        row = []
        for x in range(width):
            gx, gy = x // cell, y // cell
            fx = (x % cell) / cell
            fy = (y % cell) / cell
            # Bilinear interpolation of the four surrounding lattice points.
            v = (
                sample(gx, gy) * (1 - fx) * (1 - fy)
                + sample(gx + 1, gy) * fx * (1 - fy)
                + sample(gx, gy + 1) * (1 - fx) * fy
                + sample(gx + 1, gy + 1) * fx * fy
            )
            row.append(v)
        out.append(row)
    return out


def generate_world(seed: str, width: int = 60, height: int = 40) -> World:
    """Generate a deterministic world from a seed string.

    Same seed + dimensions always produce the identical world.
    """
    rng = random.Random(f"canaan:{seed}:{width}x{height}")
    coast_noise = _value_noise(rng, width, height, cell=8)
    forest_noise = _value_noise(rng, width, height, cell=6)
    water_noise = _value_noise(rng, width, height, cell=10)

    world = World(width=width, height=height, seed=seed)

    # Region band boundaries, measured from the south (bottom) edge.
    bounds = []
    acc = 0.0
    for region, frac in REGION_BANDS:
        acc += frac
        bounds.append((region, acc))

    tiles: list[list[Tile]] = []
    for y in range(height):
        row = []
        # depth 0.0 = south edge, 1.0 = north edge
        depth = 1.0 - (y / max(height - 1, 1))
        for x in range(width):
            # Wobble the coastline/band edges with noise so regions interlock.
            d = depth + (coast_noise[y][x] - 0.5) * 0.12
            terrain = WATER
            for region, upper in bounds:
                if d <= upper:
                    terrain = region
                    break
            # Patch lakes into the middle regions.
            if terrain in (FOREST, MIRE) and water_noise[y][x] > 0.78:
                terrain = WATER
            # Thin out forest into coast-like clearings where noise is low.
            if terrain == FOREST and forest_noise[y][x] < 0.25:
                terrain = COAST
            row.append(Tile(terrain=terrain))
        tiles.append(row)
    world.tiles = tiles

    # Blight seed points: a handful of origin cells in the Black Pines.
    candidates = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if tiles[y][x].terrain == FOREST
    ]
    n_sources = min(3, len(candidates))
    for x, y in rng.sample(candidates, n_sources) if candidates else []:
        tiles[y][x].blight = MAX_BLIGHT
        world.blight_sources.append((x, y))

    return world
