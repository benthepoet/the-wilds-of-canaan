# The Wilds of Canaan
## Playable Milestones

This file is the **checkable companion to the Development Roadmap** (see
`The_Wilds_of_Canaan_Development_Roadmap.md` §5-§6). Each milestone is
something you can personally run and verify — exact commands, exact things
to observe, and a crisp done/not-done line. The milestones follow the
roadmap's 12-week phases; nothing here adds scope beyond the prototype goal.

**Status key:** ✅ done / ⬜ not done

---

## M1 ✅ — Walk the World

**What's new:** The headless Python engine. Seed-based world generation
(Shallows coast, Black Pines, Mire, Bluffs, Frozen Straits), player movement
with collision, gathering (`g`) for wood, consecration (`c`) that cleanses
ground and blocks blight, and blight escalation (1 spread/day, 2/day after
Day 20, surges from Day 40). Terminal client renders the protocol as ANSI
ASCII. *(Roadmap Phase 1 + first steps of Phases 3-4.)*

**How to check:**

```bash
# 1. The test suite (worldgen determinism, blight rules, gather, consecrate)
PYTHONPATH=engine python -m unittest discover -s tests
# EXPECT: "Ran 22 tests ... OK"

# 2. Determinism: same seed, same world, twice
PYTHONPATH=engine python -m canaan --seed 7f3a9c --ticks 1 | md5sum
PYTHONPATH=engine python -m canaan --seed 7f3a9c --ticks 1 | md5sum
# EXPECT: identical hashes

# 3. Gathering: walk north into the pines, then chop
{ for i in $(seq 1 20); do echo "INPUT up"; done
  echo "INPUT g"; echo QUIT; } | \
  PYTHONPATH=engine python -m canaan --seed 7f3a9c --headless | grep ^MSG
# EXPECT: lines like "MSG You gather 4 pine wood."

# 4. Consecration: Faith drops 80 -> 75, holy ground appears
printf 'INPUT c\nQUIT\n' | \
  PYTHONPATH=engine python -m canaan --seed 7f3a9c --headless | \
  grep -E "^(MSG|STATUS|DRAW.*holy_ground)"
# EXPECT: "MSG The ground turns warm. The blight recoils.",
#         STATUS with Faith:75, DRAW lines with "holy_ground bright"

# 5. Watch it: the terminal client renders the world
python client/terminal_client.py --seed 7f3a9c --ticks 60
# EXPECT: colored ASCII map (cyan water, green pines, purple blight
#         near blight sources, @ on the coast), status bar with
#         Faith/Warmth/Hunger/Corrupt/Blight/Day/Wood/BWood
```

**Done when:** all five checks above pass. They do today.

---

## M2 ⬜ — Play in a Browser

**What's new:** The game runs in a web browser (roadmap Phase 2). A vanilla
JS Canvas client consumes the same protocol; keyboard input moves the
player; the URL carries the seed so two people see the same world.
*(Stack decision lives here: port the engine to a TS Web Worker per
Architecture §9.3, or serve the Python engine over WebSocket per §5.
Either is acceptable — the protocol and this milestone's checks are the
same. Choose the smallest thing that works.)*

**How to check:**

```bash
# 1. Tests still pass
PYTHONPATH=engine python -m unittest discover -s tests   # (or npm test if ported)

# 2. Serve the prototype
python -m http.server 8000        # or the documented serve command
# EXPECT: open http://localhost:8000/?seed=7f3a9c in a browser

# 3. In the browser:
#    - The same world as M1's terminal render appears as ASCII on canvas
#      (coast at the bottom, pines above, water at the top).
#    - Arrow keys / hjkl move the @; trees block nothing but water does.
#    - Sidebar shows Faith/Warmth/Hunger/Corrupt/Blight/Day/Wood.
#    - Resize the window: the viewport adapts, no crash.
#    - Open ?seed=7f3a9c in a second browser: identical map layout.
```

**Done when:** you can share `?seed=7f3a9c` with a second browser window
and both show the identical world; movement works with visible feedback.

---

## M3 ⬜ — The Rhythm of Survival

**What's new:** Survival pressure (roadmap Phase 3). Hunger and thirst
drain over time and can kill; foraging/berries and fishing provide food;
tools (flint knife, stone axe) have durability and break; inventory has
weight. *(Builds directly on M1's `g` gather action.)*

**How to check:**

```bash
# Scripted run: idle without eating -> death with a clear cause
python tools/simulate.py --seed 7f3a9c --script idle --days 8
# EXPECT: a death line naming the cause, e.g.
#         "MSG Starvation. You had 0 food for 4 days."

# Scripted run: gather and eat -> survive past day 8
python tools/simulate.py --seed 7f3a9c --script forage_and_eat --days 8
# EXPECT: STATUS shows Hunger rising after meals; player alive on Day 8

# Durability: chop until the axe breaks
# EXPECT: "MSG Your axe shatters." and gathering yield drops/stops
```

**Done when:** an idle player starves with an instructive death message,
and a player who forages and eats survives the same period. *(Win/lose:
survive 7 days = win; the death message must name the cause.)*

---

## M4 ⬜ — Push Back the Dark

**What's new:** The core loop closes (roadmap Phase 4). Consecration costs
real resources (Holy Water + Salt), not just Faith; Corruption has teeth
(effects at high levels); the first hostile — Corrupted Wolf — hunts the
player; consecrated ground is visibly safe.

**How to check:**

```bash
# Blight threat: run to Day 25 with no consecration
python tools/simulate.py --seed 7f3a9c --script idle --days 25
# EXPECT: STATUS Blight: climbs; blighted tiles visibly approach the coast

# Consecration defense: establish a perimeter, hold it
python tools/simulate.py --seed 7f3a9c --script consecrate_perimeter --days 25
# EXPECT: holy tiles remain blight-free (blight never crosses + ground);
#         the perimeter fails only if you run out of Salt/Holy Water

# Wolves: stand in the open at night
# EXPECT: wolves approach and attack; HP/STATUS changes; death by wolf
#         is recorded with cause "Wolf pack"
```

**Done when:** *(win/lose)* — you can hold a consecrated perimeter through
Day 20 if you manage Salt/Holy Water, and you lose the ground if you don't.
Wolves kill an unprepared player at night.

---

## M5 ⬜ — A Home in the Wilds

**What's new:** Building (roadmap Phase 5). The 5 Tier-1 blueprints
(Lean-To, Firepit, Longhouse, Forge, Storehouse) with the three
construction stages (planned `?` → framed `+` → complete `#`); structures
give real bonuses (firepit warmth, storehouse protection); one rescued
pilgrim (Laborer) who helps build and eats daily.

**How to check:**

```bash
# Build a firepit from gathered wood
python tools/simulate.py --seed 7f3a9c --script build_firepit
# EXPECT: MSG lines showing ? -> + -> # stages across ticks;
#         STATUS Warmth drains slower near the fire at night

# A framed wall is not a wall: wolves pass a ? or + wall but stop at #
# EXPECT: observable difference in a scripted wolf-approach test

# Pilgrim: rescue consumes food
# EXPECT: Hunger/food stores drain faster with a pilgrim present;
#         the pilgrim's death appears as a message (Chronicle hook)
```

**Done when:** you can chop wood, place a firepit ghost, watch it frame
and complete, and measurably survive colder nights because of it.

---

## M6 ⬜ — Winter's Siege

**What's new:** Seasons (roadmap Phase 6). Autumn stockpile pressure,
winter arriving on Day 30 (snow, ice on the Straits, warmth drain,
forage scarcity), and one Blood Moon event.

**How to check:**

```bash
# Reach winter unprepared
python tools/simulate.py --seed 7f3a9c --script idle --days 32
# EXPECT: "MSG Winter has come." on Day 30; frozen/starved death soon
#         after, cause named

# Reach winter prepared (stockpiled food, firepit, shelter)
python tools/simulate.py --seed 7f3a9c --script winter_prepared --days 35
# EXPECT: alive on Day 35; foraging yields visibly less in winter
```

**Done when:** *(win/lose)* — winter kills an unprepared run and a
stockpiled, sheltered run survives to Day 35. Ice tiles on the Straits
render as `=` and are crossable-but-risky.

---

## M7 ⬜ — The Drowned Choir

**What's new:** The first Manifestation (roadmap Phase 7). The Drowned
Choir stalks the Shallows with telegraphed signs (lake fog, drowned dead);
at least one complete solution path (the Priest rite); victory drops
Drowned Silver and unlocks Tier 2; The Chronicle records deaths with cause.

**How to check:**

```bash
# Attempt the rite unprepared
python tools/simulate.py --seed 7f3a9c --script fight_choir_unprepared
# EXPECT: death; Chronicle entry written with cause and day

# Defeat it prepared (salt circle, holy water, consecrated arena)
python tools/simulate.py --seed 7f3a9c --script fight_choir_prepared
# EXPECT: "The Choir is silenced" victory message; Drowned Silver in
#         STATUS/inventory; Tier 2 blueprints available
```

**Done when:** *(win/lose)* — the boss kills an unprepared player with an
instructive death, and a prepared player can defeat it and receive the
unlock. A second run finds the first run's Chronicle entry.

---

## M8 ⬜ — The Promise (Prototype Complete)

**What's new:** End-to-end playability (roadmap Phase 10, scoped to the
promise, not the full game). One Vocation (Priest) playable from shipwreck
to Drowned Choir victory; one ending implemented; title screen, death
screen, basic audio cues; deployed to a public URL.

**How to check:**

```bash
# 1. Open the deployed URL. Create a Priest. Play.
# 2. EXPECT, in one sitting:
#    - Title screen -> character creation -> shipwreck on the Shallows
#    - Gather, build a chapel, survive wolves, hold the blight, winter
#      threatens, the Choir manifests, you win or die trying
#    - Death shows a cause screen; victory shows an ending
#    - A full run completes (win or lose) in under 2 hours
```

**Done when:** three people who did not build the game each play a full
run from the URL without instructions, at least one dies and understands
why, and at least one asks for "one more run." That is the 12-week goal.

---

## Notes

- Milestones M2-M8 assume the same CLI/protocol conventions established in
  M1 (`--seed`, `--headless`, stdin `INPUT` commands, `DRAW/STATUS/MSG/FLUSH`
  frames). If the browser pivot (M2) ports the engine to TypeScript, the
  `python tools/simulate.py` checks become the equivalent TS test/sim
  harness — the *observations* stay identical.
- `tools/simulate.py` does not exist yet; it is a thin scripted-driver over
  the existing stdin protocol (feed a recorded input script, assert on
  protocol output). Build it as part of M3 and reuse it thereafter.
- The roadmap's weekly checkpoint table (§6) remains the schedule view;
  this file is the verification view. Update the ✅/⬜ markers as
  milestones land.

---

Document Version 1.0
The Wilds of Canaan - Playable Milestones
