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
const m = src.match(/function cameraOrigin[\s\S]*?\n}/);
if (!m) { console.error("cameraOrigin not found"); process.exit(2); }
eval(m[0]);
// [px, py, viewW, viewH, worldW, worldH] -> [camX, camY]
const cases = process.argv[2];
const out = JSON.parse(cases).map(c => cameraOrigin(...c));
console.log(JSON.stringify(out));
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


if __name__ == "__main__":
    unittest.main()
