# The Wilds of Canaan

ASCII survival-crafter / frontier horror. This repo currently contains the
design documents (`docs/`) and the first runnable engine skeleton (roadmap
Phase 1, weeks 1-2).

## Layout

- `engine/canaan/` — headless Python engine package (stdlib only)
  - `world.py` — seed-based procedural world generation (Shallows coast,
    Black Pines forest, Mire, Bluffs, Frozen Straits water)
  - `blight.py` — Blight spread mechanic
  - `sim.py` — tick loop, player entity, protocol frames, CLI entry point
  - `protocol.py` — protocol emitter + input parser
- `client/terminal_client.py` — ANSI terminal client that renders the protocol
- `server/canaan_server.py` + `server/static/` — stdlib web server (SSE
  protocol stream, POST input) and vanilla-JS canvas browser client
- `tests/` — unittest suite

## Protocol

The engine never draws; it emits text lines (see
`docs/The_Wilds_of_Canaan_Technical_Architecture.md` §3):

```
SEED 7f3a9c
CLEAR
DRAW 14 22 forest blighted dark_purple black 0
DRAW 10 5 creature player white black 0
STATUS Faith:80 Warmth:60 Hunger:40 Corrupt:0 Blight:3
TIME 7
FLUSH
```

Input commands on stdin: `INPUT <key>`, `RESIZE <w> <h>`, `SAVE`, `LOAD`,
`QUIT`.

Player input keys (`INPUT <key>`):

- Movement: `up/down/left/right`, `wasd`, or vi-keys `hjkl`
- `g` — gather/chop: fell an adjacent tree for 2-4 wood (blighted trees
  give blighted wood and raise Corruption)
- `c` — consecrate: cleanse blight in radius 1 and mark holy ground
  (blocks blight spread); costs 5 Faith

Blight escalation (per the GDD): spreads one step per day, twice per day
after Day 20, and additionally surges (a leap of up to 5 tiles in a random
direction) from Day 40.

## Run

Browser client (M2 — stdlib server, SSE protocol stream, POST input):

```bash
PYTHONPATH=engine python server/canaan_server.py --port 8000
# open http://localhost:8000/?seed=7f3a9c
# move: arrows / wasd / hjkl;  g = gather;  c = consecrate
# every client connected with the same seed shares one world
```

Headless protocol dump:

```bash
PYTHONPATH=engine python -m canaan --seed 7f3a9c --ticks 20
```

Terminal client (launches the engine, renders each tick as ASCII):

```bash
python client/terminal_client.py --seed 7f3a9c --ticks 60
```

Interactive headless mode (one tick per input line):

```bash
printf 'INPUT up\nINPUT left\nQUIT\n' | PYTHONPATH=engine python -m canaan --headless
```

## Test

```bash
PYTHONPATH=engine:. python -m unittest discover -s tests -v
```
