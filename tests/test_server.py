import http.client
import threading
import unittest

from server.canaan_server import Handler, MANAGER, ThreadingHTTPServer


class ServerFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever,
                                      daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def get(self, path):
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        conn.request("GET", path)
        return conn.getresponse()


class StaticTests(ServerFixture):
    def test_index_served(self):
        resp = self.get("/")
        self.assertEqual(resp.status, 200)
        self.assertIn(b"The Wilds of Canaan", resp.read())

    def test_game_js_served(self):
        resp = self.get("/game.js")
        self.assertEqual(resp.status, 200)
        self.assertIn(b"EventSource", resp.read())

    def test_404(self):
        resp = self.get("/nope")
        self.assertEqual(resp.status, 404)
        resp.read()


def read_protocol_lines(path, max_lines, port):
    """Open an SSE stream and collect protocol lines."""
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=15)
    conn.request("GET", path)
    resp = conn.getresponse()
    lines = []
    buf = b""
    while len(lines) < max_lines:
        chunk = resp.read1(4096)
        if not chunk:
            break
        buf += chunk
        while b"\n" in buf:
            raw, buf = buf.split(b"\n", 1)
            raw = raw.decode().strip()
            if raw.startswith("data: "):
                lines.append(raw[6:])
                if len(lines) >= max_lines:
                    break
    conn.close()
    return lines


def first_frame(lines):
    """Extract one atomic frame (up to and incl. FLUSH), minus TIME."""
    frame = lines[: lines.index("FLUSH") + 1]
    return [l for l in frame if not l.startswith("TIME")]


class StreamTests(ServerFixture):
    def test_stream_emits_seed_and_frame(self):
        lines = read_protocol_lines("/stream?seed=unittest1", 20, self.port)
        self.assertEqual(lines[0], "SEED unittest1")
        self.assertIn("CLEAR", lines)
        self.assertTrue(any(l.startswith("DRAW ") for l in lines))

    def test_two_clients_same_seed_identical_frames(self):
        # A second client on the same seed joins the same world and sees
        # the identical stream. Frames are broadcast atomically; we drop
        # TIME (clients may join on different ticks).
        a = first_frame(
            read_protocol_lines("/stream?seed=unittest2", 2500, self.port))
        b = first_frame(
            read_protocol_lines("/stream?seed=unittest2", 2500, self.port))
        self.assertEqual(a, b)
        self.assertEqual(a[0], "SEED unittest2")
        self.assertTrue(any(" creature player " in l for l in a))

    def test_input_moves_player(self):
        seed = "unittest3"
        before = read_protocol_lines(f"/stream?seed={seed}", 2500, self.port)
        pos0 = next(l for l in before
                    if l.startswith("DRAW") and " creature player " in l)

        def post(key):
            c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
            c.request("POST", f"/input?seed={seed}&key={key}")
            r = c.getresponse()
            self.assertEqual(r.status, 200)
            r.read()
            c.close()

        moved = False
        for key in ("up", "right", "down", "left"):
            post(key)
            lines = read_protocol_lines(f"/stream?seed={seed}", 2500,
                                        self.port)
            pos = next(l for l in lines
                       if l.startswith("DRAW") and " creature player " in l)
            if pos != pos0:
                moved = True
                break
        self.assertTrue(moved, f"player never moved from {pos0}")


if __name__ == "__main__":
    unittest.main()
