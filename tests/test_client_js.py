"""Camera-math checks for the web client.

The camera lives in JavaScript (server/static/game.js), which unittest
cannot import. If node is available, we extract the pure `cameraOrigin`
function from game.js and assert its clamping behaviour; otherwise these
tests skip.
"""

import json
import shutil
import subprocess
import unittest
from pathlib import Path

GAME_JS = Path(__file__).parent.parent / "server" / "static" / "game.js"

NODE_SCRIPT = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
function extract(re, name) {
    const m = src.match(re);
    if (!m) { console.error(name + " not found"); process.exit(2); }
    return m[0];
}
// eval at top level so the declarations land in this scope
eval(extract(/const ANIM = \{[\s\S]*?\};/, "ANIM")
     + extract(/function cameraOrigin[\s\S]*?\n}/, "cameraOrigin")
     + extract(/function animChar[\s\S]*?\n}/, "animChar"));
// [px, py, viewW, viewH, worldW, worldH] -> [camX, camY]
const cases = process.argv[2];
const out = JSON.parse(cases).map(c => cameraOrigin(...c));
console.log(JSON.stringify(out));
"""

ANIM_NODE_SCRIPT = r"""
const fs = require("fs");
const src = fs.readFileSync(process.argv[1], "utf8");
function extract(re, name) {
    const m = src.match(re);
    if (!m) { console.error(name + " not found"); process.exit(2); }
    return m[0];
}
eval(extract(/const ANIM = \{[\s\S]*?\};/, "ANIM")
     + extract(/function animChar[\s\S]*?\n}/, "animChar"));
// [key, char, now_ms] -> rendered char
const cases = JSON.parse(process.argv[2]);
console.log(JSON.stringify(cases.map(c => animChar(c[0], c[1], c[2]))));
"""


@unittest.skipUnless(shutil.which("node"), "node not available")
class CameraTests(unittest.TestCase):
    def run_camera(self, cases):
        result = subprocess.run(
            ["node", "-e", NODE_SCRIPT, str(GAME_JS), json.dumps(cases)],
            capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def test_spawn_visible_seed_7f3a9c(self):
        # Player spawns at (0,39) on a 60x40 world; default-ish view 40x25.
        [[cx, cy]] = self.run_camera([[0, 39, 40, 25, 60, 40]])
        # Player must be inside the view.
        self.assertLessEqual(cx, 0)
        self.assertLess(0, cx + 40)
        self.assertLessEqual(cy, 39)
        self.assertLess(39, cy + 25)

    def test_centers_on_player(self):
        [[cx, cy]] = self.run_camera([[30, 20, 40, 25, 60, 40]])
        self.assertEqual((cx, cy), (10, 8))  # 30-20, 20-12

    def test_clamps_at_far_edges(self):
        [[cx, cy]] = self.run_camera([[59, 39, 40, 25, 60, 40]])
        self.assertEqual((cx, cy), (20, 15))  # worldW-viewW, worldH-viewH

    def test_view_larger_than_world_pins_to_origin(self):
        [[cx, cy]] = self.run_camera([[30, 20, 100, 60, 60, 40]])
        self.assertEqual((cx, cy), (0, 0))

    def test_northwest_corner(self):
        [[cx, cy]] = self.run_camera([[0, 0, 40, 25, 60, 40]])
        self.assertEqual((cx, cy), (0, 0))


@unittest.skipUnless(shutil.which("node"), "node not available")
class WebAnimTests(unittest.TestCase):
    """animChar() in game.js: water and blight cycle; everything else
    is static (ASCII Visual Design §9.5 animation budget)."""

    def run_anim(self, cases):
        result = subprocess.run(
            ["node", "-e", ANIM_NODE_SCRIPT, str(GAME_JS), json.dumps(cases)],
            capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def test_water_cycles_every_1500ms(self):
        out = self.run_anim([["water:open", "~", t]
                             for t in (0, 1500, 3000, 4500)])
        self.assertEqual(out, ["~", "w", "~", "~"])  # ~ -> w -> ~ cycle

    def test_blight_breathes_every_2500ms(self):
        out = self.run_anim([["forest:blighted", '"', t]
                             for t in (0, 2500, 5000)])
        self.assertEqual(out, ['"', "=", '"'])
        out = self.run_anim([["forest:corrupted", "=", t]
                             for t in (0, 2500)])
        self.assertEqual(out, ['"', "="])

    def test_static_tiles_never_change(self):
        cases = [["water:ice", "=", t] for t in (0, 2500, 9999)]
        cases += [["forest:clean", "^", t] for t in (0, 2500, 9999)]
        cases += [["forest:hell", "%", 9999],
                  ["creature:player", "@", 9999]]
        out = self.run_anim(cases)
        self.assertEqual(out, [c[1] for c in cases])


class TerminalAnimTests(unittest.TestCase):
    """Same animation contract in the terminal client (pure Python)."""

    def setUp(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "terminal_client",
            Path(__file__).parent.parent / "client" / "terminal_client.py")
        self.tc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.tc)

    def test_water_cycles(self):
        f = self.tc.anim_char
        self.assertEqual(f(("water", "open"), "~", 0), "~")
        self.assertEqual(f(("water", "open"), "~", 1500), "w")
        self.assertEqual(f(("water", "open"), "~", 3000), "~")

    def test_blight_breathes(self):
        f = self.tc.anim_char
        self.assertEqual(f(("forest", "blighted"), '"', 0), '"')
        self.assertEqual(f(("forest", "blighted"), '"', 2500), "=")

    def test_static_tiles_unchanged(self):
        f = self.tc.anim_char
        self.assertEqual(f(("water", "ice"), "=", 9999), "=")
        self.assertEqual(f(("forest", "clean"), "^", 9999), "^")


if __name__ == "__main__":
    unittest.main()
