"""Web server for The Wilds of Canaan (M2: Play in a Browser).

Stdlib-only (http.server). Serves the vanilla-JS client and streams the
existing engine's protocol over Server-Sent Events; player input arrives
as HTTP POSTs. One shared Game per seed: every client that connects with
the same seed watches (and plays) the identical world, per the
architecture doc's spectator model.

Endpoints:
    GET  /                     -> static/index.html
    GET  /game.js              -> static/game.js
    GET  /stream?seed=HEX      -> SSE stream of protocol lines
    POST /input?seed=HEX&key=K -> feed "INPUT K" to that seed's game

Run:
    PYTHONPATH=engine python server/canaan_server.py --port 8000
"""

from __future__ import annotations

import argparse
import queue
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from canaan.sim import Game

STATIC_DIR = Path(__file__).parent / "static"

TICK_SECONDS = 0.5  # one in-game hour every half second


class FrameBroadcaster:
    """Captures protocol output from a Game and fans it out to subscribers.

    Passed to the Game as its output stream; the engine's per-frame flush()
    becomes one broadcast of that frame's lines.
    """

    def __init__(self) -> None:
        self._buf: list[str] = []
        self.subscribers: list[queue.Queue] = []

    def write(self, text: str) -> int:
        self._buf.extend(text.splitlines())
        return len(text)

    def flush(self) -> None:
        if not self._buf:
            return
        frame, self._buf = self._buf, []
        for sub in self.subscribers:
            sub.put(frame)

    def subscribe(self) -> queue.Queue:
        q: queue.Queue = queue.Queue()
        self.subscribers.append(q)
        return q

    def unsubscribe(self, q: queue.Queue) -> None:
        if q in self.subscribers:
            self.subscribers.remove(q)


class WorldSession:
    """One shared game world (keyed by seed) plus its tick thread."""

    def __init__(self, seed: str, width: int = 60, height: int = 40):
        self.seed = seed
        self.broadcaster = FrameBroadcaster()
        self.game = Game(seed=seed, width=width, height=height,
                         out=self.broadcaster)
        self.lock = threading.Lock()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._started = False

    def start(self) -> None:
        if not self._started:
            self._started = True
            self._thread.start()

    def _run(self) -> None:
        with self.lock:
            self.game.emit_frame()
        while self.game.running:
            time.sleep(TICK_SECONDS)
            with self.lock:
                self.game.tick()

    def handle_input(self, key: str) -> None:
        with self.lock:
            self.game.handle_command(f"INPUT {key}")
            # Re-emit immediately so the player sees the result without
            # waiting for the next tick.
            self.game.emit_frame()


class SessionManager:
    def __init__(self):
        self._sessions: dict[str, WorldSession] = {}
        self._lock = threading.Lock()

    def get(self, seed: str) -> WorldSession:
        with self._lock:
            session = self._sessions.get(seed)
            if session is None:
                session = WorldSession(seed)
                session.start()
                self._sessions[seed] = session
            return session


MANAGER = SessionManager()


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args) -> None:  # quiet
        pass

    def _send_bytes(self, body: bytes, content_type: str, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        url = urlparse(self.path)
        params = parse_qs(url.query)
        if url.path == "/":
            self._send_bytes((STATIC_DIR / "index.html").read_bytes(),
                             "text/html")
        elif url.path == "/game.js":
            self._send_bytes((STATIC_DIR / "game.js").read_bytes(),
                             "text/javascript")
        elif url.path == "/stream":
            seed = params.get("seed", ["random"])[0]
            self._stream(MANAGER.get(seed))
        else:
            self._send_bytes(b"not found", "text/plain", 404)

    def do_POST(self) -> None:
        url = urlparse(self.path)
        params = parse_qs(url.query)
        if url.path == "/input":
            seed = params.get("seed", ["random"])[0]
            key = params.get("key", [""])[0]
            MANAGER.get(seed).handle_input(key)
            self._send_bytes(b"ok", "text/plain")
        else:
            self._send_bytes(b"not found", "text/plain", 404)

    def _stream(self, session: WorldSession) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        # SEED is sent once at world start, so late-joining clients would
        # never see it in the broadcast; send it directly on subscribe.
        self.wfile.write(f"data: SEED {session.game.world.seed}\n\n".encode())
        sub = session.broadcaster.subscribe()
        try:
            while True:
                frame = sub.get()
                for line in frame:
                    self.wfile.write(f"data: {line}\n\n".encode())
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            session.broadcaster.unsubscribe(sub)


def main() -> None:
    parser = argparse.ArgumentParser(description="Canaan web server")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"The Wilds of Canaan: http://localhost:{args.port}/?seed=7f3a9c")
    server.serve_forever()


if __name__ == "__main__":
    main()
