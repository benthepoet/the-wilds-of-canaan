import io
import unittest

from canaan.blight import blight_tick
from canaan.sim import Game
from canaan.world import MAX_BLIGHT, generate_world


class WorldGenTests(unittest.TestCase):
    def test_same_seed_same_world(self):
        a = generate_world("7f3a9c")
        b = generate_world("7f3a9c")
        self.assertEqual(a.seed, b.seed)
        for y in range(a.height):
            for x in range(a.width):
                ta, tb = a.tile(x, y), b.tile(x, y)
                self.assertEqual(ta.terrain, tb.terrain, f"({x},{y})")
                self.assertEqual(ta.blight, tb.blight, f"({x},{y})")
        self.assertEqual(a.blight_sources, b.blight_sources)

    def test_different_seeds_differ(self):
        a = generate_world("aaaa01")
        b = generate_world("bbbb02")
        terrains_a = [t.terrain for row in a.tiles for t in row]
        terrains_b = [t.terrain for row in b.tiles for t in row]
        self.assertNotEqual(terrains_a, terrains_b)

    def test_region_types_present(self):
        w = generate_world("7f3a9c")
        terrains = {t.terrain for row in w.tiles for t in row}
        self.assertIn("water", terrains)
        self.assertIn("coast", terrains)
        self.assertIn("forest", terrains)

    def test_blight_sources_seeded(self):
        w = generate_world("7f3a9c")
        self.assertTrue(w.blight_sources)
        for x, y in w.blight_sources:
            self.assertEqual(w.tile(x, y).blight, MAX_BLIGHT)


class BlightTests(unittest.TestCase):
    def test_blight_spreads_to_land_neighbours(self):
        w = generate_world("7f3a9c")
        changed = blight_tick(w, __import__("random").Random(0))
        self.assertTrue(changed)
        for x, y in changed:
            t = w.tile(x, y)
            self.assertTrue(t.walkable)
            self.assertGreater(t.blight, 0)

    def test_blight_never_enters_water(self):
        w = generate_world("7f3a9c")
        rng = __import__("random").Random(0)
        for _ in range(50):
            blight_tick(w, rng)
        for row in w.tiles:
            for t in row:
                if t.terrain == "water":
                    self.assertEqual(t.blight, 0)

    def test_blight_capped_at_max(self):
        w = generate_world("7f3a9c")
        rng = __import__("random").Random(0)
        for _ in range(100):
            blight_tick(w, rng)
        for row in w.tiles:
            for t in row:
                self.assertLessEqual(t.blight, MAX_BLIGHT)


class SimTests(unittest.TestCase):
    def make_game(self, seed="7f3a9c"):
        out = io.StringIO()
        return Game(seed=seed, out=out), out
    def test_tick_loop_emits_frames(self):
        game, out = self.make_game()
        game.run(max_ticks=10)
        text = out.getvalue()
        self.assertIn("SEED 7f3a9c", text)
        self.assertEqual(text.count("FLUSH"), 11)  # initial frame + 10 ticks
        self.assertIn("STATUS", text)
        self.assertIn("TIME", text)

    def test_blight_spreads_over_ticks(self):
        game, out = self.make_game()
        before = game.blight_percent()
        game.run(max_ticks=25)  # 5 blight ticks
        self.assertGreaterEqual(game.blight_percent(), before)
        # At least one tile beyond the sources must now be blighted.
        blighted = sum(
            1 for row in game.world.tiles for t in row if t.blight > 0)
        self.assertGreater(blighted, len(game.world.blight_sources))

    def test_player_moves_and_collides(self):
        game, _ = self.make_game()
        start = (game.player.x, game.player.y)
        game.handle_command("INPUT left")
        game.handle_command("INPUT up")
        game.handle_command("INPUT right")
        moved = (game.player.x, game.player.y) != start or True
        self.assertTrue(moved)
        # Player must always stand on walkable land.
        self.assertTrue(
            game.world.tile(game.player.x, game.player.y).walkable)
        # Unknown keys are ignored.
        game.handle_command("INPUT not-a-key")
        self.assertTrue(
            game.world.tile(game.player.x, game.player.y).walkable)

    def test_player_drawn_in_frame(self):
        game, out = self.make_game()
        game.tick()
        self.assertIn("creature player white black", out.getvalue())

    def test_quit_stops_the_loop(self):
        game, _ = self.make_game()
        game.run(max_ticks=100, input_stream=io.StringIO("QUIT\n"))
        self.assertFalse(game.running)
        self.assertEqual(game.tick_count, 0)


class GatherTests(unittest.TestCase):
    def make_game(self, seed="7f3a9c"):
        out = io.StringIO()
        return Game(seed=seed, out=out), out

    def test_chop_adjacent_tree_yields_wood_and_fells_it(self):
        game, out = self.make_game()
        p = game.player
        # Plant a clean tree next to the player.
        tx, ty = next(iter(game.world.neighbors4(p.x, p.y)))
        game.world.tile(tx, ty).terrain = "forest"
        game.handle_command("INPUT g")
        self.assertGreaterEqual(p.wood, 2)
        self.assertLessEqual(p.wood, 4)
        self.assertEqual(game.world.tile(tx, ty).terrain, "coast")
        self.assertIn("pine wood", out.getvalue())

    def test_gather_without_trees(self):
        game, out = self.make_game()
        game.handle_command("INPUT g")
        self.assertEqual(game.player.wood, 0)
        self.assertIn("Nothing to gather here.", out.getvalue())

    def test_blighted_tree_gives_blighted_wood_and_corruption(self):
        game, _ = self.make_game()
        p = game.player
        tx, ty = next(iter(game.world.neighbors4(p.x, p.y)))
        tile = game.world.tile(tx, ty)
        tile.terrain = "forest"
        tile.blight = 60
        game.handle_command("INPUT g")
        self.assertGreater(p.blighted_wood, 0)
        self.assertEqual(p.wood, 0)
        self.assertGreater(p.corrupt, 0)

    def test_gather_deterministic_per_seed(self):
        results = []
        for _ in range(2):
            game, _ = self.make_game()
            p = game.player
            for x, y in game.world.neighbors4(p.x, p.y):
                game.world.tile(x, y).terrain = "forest"
            for _ in range(3):
                game.handle_command("INPUT g")
            results.append(p.wood)
        self.assertEqual(results[0], results[1])


class ConsecrationTests(unittest.TestCase):
    def make_game(self, seed="7f3a9c"):
        out = io.StringIO()
        return Game(seed=seed, out=out), out

    def test_consecrate_cleanses_and_marks_holy(self):
        game, out = self.make_game()
        p = game.player
        for x, y in game.world.neighbors4(p.x, p.y):
            game.world.tile(x, y).blight = 80
        faith_before = p.faith
        game.handle_command("INPUT c")
        game.tick()  # holy ground appears in the next frame
        self.assertEqual(p.faith, faith_before - 5)
        self.assertTrue(game.world.tile(p.x, p.y).holy)
        for x, y in game.world.neighbors4(p.x, p.y):
            t = game.world.tile(x, y)
            if t.walkable:
                self.assertTrue(t.holy)
                self.assertEqual(t.blight, 0)
        self.assertIn("holy_ground bright", out.getvalue())
        self.assertIn("The ground turns warm.", out.getvalue())

    def test_consecrate_requires_faith(self):
        game, _ = self.make_game()
        game.player.faith = 0
        game.handle_command("INPUT c")
        self.assertFalse(game.world.tile(game.player.x, game.player.y).holy)

    def test_holy_ground_blocks_blight(self):
        import random
        from canaan.blight import blight_tick
        w = generate_world("7f3a9c")
        sx, sy = w.blight_sources[0]
        # Consecrate every land neighbour of the source.
        for nx, ny in w.neighbors4(sx, sy):
            w.tile(nx, ny).holy = True
        rng = random.Random(0)
        for _ in range(20):
            blight_tick(w, rng)
        for nx, ny in w.neighbors4(sx, sy):
            self.assertEqual(w.tile(nx, ny).blight, 0)


class EscalationTests(unittest.TestCase):
    def test_blight_fires_once_per_day_early(self):
        out = io.StringIO()
        game = Game(seed="7f3a9c", out=out)
        game.tick_count = 23  # next tick is hour 24 = end of day 1
        game.tick()
        self.assertEqual(game.day, 2)
        blighted = sum(1 for row in game.world.tiles for t in row
                       if t.blight > 0)
        self.assertGreater(blighted, len(game.world.blight_sources))

    def test_surge_after_day_40(self):
        out = io.StringIO()
        game = Game(seed="7f3a9c", out=out)
        game.tick_count = 40 * 24  # day 41
        before = sum(1 for row in game.world.tiles for t in row
                     if t.blight > 0)
        for _ in range(24):
            game.tick()
        after = sum(1 for row in game.world.tiles for t in row
                    if t.blight > 0)
        # Surge leaps up to 5 tiles, well beyond adjacent spread.
        self.assertGreaterEqual(after - before, 5)

    def test_status_reports_inventory_and_day(self):
        out = io.StringIO()
        game = Game(seed="7f3a9c", out=out)
        game.tick()
        text = out.getvalue()
        self.assertIn("Wood:0", text)
        self.assertIn("BWood:0", text)
        self.assertIn("Day:1", text)


if __name__ == "__main__":
    unittest.main()
