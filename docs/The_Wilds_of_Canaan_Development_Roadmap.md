# The Wilds of Canaan
## Development Roadmap & Design Playbook

---

## 1. The Goal

Build a **playable web prototype** in 12 weeks that demonstrates the core loop: survive, gather, build, consecrate, and defeat the first Manifestation. The prototype must be **engaging** (you want to start another run), **fun** (the mechanics feel good), and **challenging** (you should die often, but always understand why).

---

## 2. What Makes It Engaging

Engagement is not content volume. It is the **density of meaningful decisions per minute.**

### 2.1 The Three Hooks

**The Hook of Discovery:**
- The map is procedural. No two runs have the same Clean Spring placement.
- Lost Scriptures are shuffled. You might find the Bishop's Fragment on run 3, or run 15.
- The Chronicle of dead characters appears in the world. Reading them gives you maps, warnings, and one free cross-class ability. Every death makes the next run slightly wiser.
- **Rule:** The player should discover something new in the first 5 minutes of every run.

**The Hook of Near-Misses:**
- You should almost survive. You should almost find enough salt. You should almost consecrate the ground before the blight surges.
- The game logs "near-misses" in The Chronicle: "Day 9: The blight reached the chapel wall. One more day and it would have been inside."
- **Rule:** Every death should feel like "if I had just done X differently, I would have made it."

**The Hook of Asymmetry:**
- The three Vocations play like different games. A player who masters the Priest has not mastered the Woodsman.
- Cross-class learning creates "builds." A Woodsman who finds the Bishop's Fragment plays like a hybrid nomad-sanctifier.
- **Rule:** The player should want to try "just one more run as [other Vocation]."

### 2.2 Engagement Mechanics

| Mechanic | Why It Works |
|----------|-------------|
| **The Chronicle** | Legacy without meta-progression. You do not get stronger. You get wiser. This respects the player without trivializing the challenge. |
| **Mood system** | The settlement feels alive. Pilgrims sing or cry. You are not managing numbers; you are managing despair. |
| **Seasonal urgency** | Autumn creates a natural deadline. The player feels the clock ticking. |
| **Blight as visible threat** | You can see the purple fog advancing. It is not abstract. It is coming for your home. |
| **Manifestation telegraphing** | Before a boss appears, the world changes. The Drowned Choir causes lake fog. The Hollow Stag causes trees to bleed sap. The player knows something is coming and prepares. |
| **Construction stages** | Watching a wall go from ghost (`?`) to framed (`+`) to complete (`#`) is satisfying. It creates visual progress. |
| **Pilgrim rescue** | Finding a broken person in the woods and bringing them back creates an emotional investment. Their death hurts more than losing wood. |

### 2.3 Anti-Engagement (What to Avoid)

| Trap | Why It Kills Engagement | Solution |
|------|------------------------|----------|
| **Inventory tetris** | Micromanaging grid space is not fun. | Weight-based inventory. Simple list. No grid. |
| **Crafting bloat** | 50 recipes, 90% useless. | 20 core recipes. Each unlocks a meaningful capability. |
| **Empty walking** | 30 seconds of holding W to reach the next thing. | Woodsman speed bonus. Fast-forward until hostiles or resources detected. |
| **Grinding** | "I need 100 wood for the Cathedral." | Blueprints require specific materials, not bulk. 20 wood for a Longhouse, not 200. |
| **Opaque failure** | "Why did I die?" | The Chronicle records the exact cause. Status effects have clear names. Death screen shows: "Starvation. You had 0 food for 4 days." |
| **Save scumming temptation** | Ironman is the default, but the temptation to copy-paste save files exists. | Saves are server-side in web prototype. Local play uses a single hidden save file. |

---

## 3. What Makes It Fun

Fun is **feedback.** The game must respond to the player immediately, visibly, and satisfyingly.

### 3.1 The Fun Loop

```
1. See a need      ("I need a wall before winter.")
2. Make a plan     ("I will chop 10 wood, build a palisade.")
3. Execute         (Chop, chop, build, build.)
4. Get feedback    (The wall stands. Wolves scratch at it and fail.)
5. Feel smart      ("I survived because I prepared.")
```

**Every action must have a visible consequence.**
- Chop a tree: Tree disappears, wood appears in inventory, stamina drops, axe degrades.
- Consecrate ground: Purple fog recedes, gold `+` spreads, a sound cue plays.
- Build a wall: Ghost outline appears, then framed, then solid. A pilgrim helps. You hear hammering.
- Eat blighted meat: Hunger goes down, Corruption goes up, screen tints purple briefly.

### 3.2 Juicy Feedback

| Action | Visual | Audio | Text |
|--------|--------|-------|------|
| **Consecration** | Gold pulse spreads from Priest | Chanting/bell | "The ground turns warm. The blight recoils." |
| **Trap trigger** | Enemy falls, `!` appears | Snap/crash | "The wolf falls into the pit." |
| **First snow** | Screen tints white, `*` replaces `^` | Wind howl | "Winter has come." |
| **Pilgrim rescue** | New `t`/`a`/`h` appears | Sobbing/weak voice | "You found a survivor. They call themselves Thomas." |
| **Manifestation spawn** | Screen shakes, red flash | Dissonant chord | "The Hollow Stag has entered the forest." |
| **Weapon break** | Character flashes red, weapon vanishes | Crack | "Your axe shatters." |
| **Mood shift (Doomed)** | Pilgrims stop moving, heads down | Silence replaces ambient | "The chanting has stopped." |

### 3.3 The "One More Turn" Factor

The game must create situations where the player thinks "I should stop, but let me just..."

- "...consecrate this one tile before I save and quit." (Blight surges during the rite.)
- "...check if that deer is still there." (It is not. A Wendigo is.)
- "...finish framing this wall." (Night falls. Wolves howl. You need the wall.)
- "...read this Chronicle I found." (It warns of a Clean Spring 20 tiles north. You must go.)

**The game never lets you quit on a clean boundary.** There is always a loose thread.

---

## 4. What Makes It Challenging

Challenge is not difficulty for its own sake. It is **the player against the world, with clear rules and unfair odds.**

### 4.1 The Challenge Pillars

**Scarcity:**
- Clean water is rare. You will drink snowmelt.
- Salt is rare. You will run out of warding material.
- Holy Water requires an altar. You will be tempted to drink it in desperation.
- Wood is abundant but heavy. Stone is scarce but permanent. You must choose.

**Time Pressure:**
- Day/night cycle: 10 real minutes = 1 game day.
- Winter arrives on Day 30. You cannot stop it.
- Food rots. Jerky takes a day to make. You must plan 2 days ahead.
- Pilgrims eat daily. They do not wait for you to be ready.

**Blight Escalation:**
- Blight spreads 1 tile per day in The Black Pines.
- After Day 20, it spreads 2 tiles per day.
- After Day 40, it surges: 5 tiles in a random direction.
- The player cannot outpace it forever. They must push back (Priest) or endure (Craftsman) or outrun it (Woodsman).

**No Perfect Safety:**
- Holy Ground stops blight spread but does not reverse it.
- A palisade stops wolves but not Wendigos (they phase through).
- A Chapel heals Faith but requires maintenance (braziers need wood).
- Pilgrims help but consume resources. More pilgrims = more mouths = more risk.

### 4.2 Difficulty Curves by Vocation

| Vocation | Early Game | Mid Game | Late Game | Spike Moments |
|----------|-----------|----------|-----------|---------------|
| **Priest** | Easy (consecrate = safe base) | Hard (combat is brutal, needs help) | Hard (channeling vulnerable during Manifestations) | First Blood Moon (no combat skills) |
| **Woodsman** | Hard (no base, no healing) | Medium (mobility = safety) | Hard (Manifestations require prepared ground) | Winter (camps expire, no greenhouse) |
| **Craftsman** | Medium (slow, but durable) | Easy (fortress = safety) | Medium (resource drain for maintenance) | Blight surge (walls decay, must repair under pressure) |

### 4.3 Death Should Be Instructive

Every death teaches:

| Death Cause | Lesson |
|-------------|--------|
| Starvation | "I did not stockpile in autumn. I did not build a smokehouse." |
| Wolf pack | "I walked at night without a light source. I had no walls." |
| Wendigo | "I followed the voice. I left holy ground." |
| Drowned | "I fought too close to the water. I had no silver mace." |
| Blight (Corruption 100) | "I gathered too much blighted wood. I did not purify." |
| Frozen | "I crossed the ice in late winter. I did not check for cracks." |
| Manifestation | "I attempted the Rite without enough salt. I did not prepare the arena." |
| Pilgrim suicide | "I let Mood drop to 0. I did not feed them. I did not pray with them." |

**The Chronicle records the lesson.** The next player finds the body and the warning.

### 4.4 Optional Hard Modes

For players who master the base game:

| Mode | Modifier |
|------|----------|
| **Ironman** | Default. One save. Death = delete. |
| **Martyr** | No cross-class learning. Pure Vocation only. |
| **The Long Night** | Winter starts on Day 20. Blight spreads 2x faster. |
| **Alone** | No pilgrims. Ever. |
| **The False Pilgrimage** | Random events are all negative. No blessings. |
| **Canaan Unholy** | Blight starts at 50% everywhere. No Clean Springs. |

---

## 5. The 12-Week Development Roadmap

### Phase 1: The Foundation (Weeks 1-2)

**Goal:** A headless engine that can generate a world, emit protocol lines, and accept input.

**Deliverables:**
- [ ] Procedural map generation (Great Lakes-style: peninsulas, forests, water, blight seed)
- [ ] **Seed-based generation** (numeric seed determines world layout, resources, blight origins, Lost Scripture placement)
- [ ] Protocol emitter (`DRAW`, `CLEAR`, `FLUSH`, `SEED`)
- [ ] Protocol input parser (`INPUT <key>`, `RESIZE <w> <h>`)
- [ ] Basic tile system (terrain + blight level + visibility)
- [ ] Player entity (move, collide with terrain)
- [ ] Day/night cycle (tint, vision radius)
- [ ] Save/load (JSON world state)

**Engagement checkpoint:** Can you walk around a generated map, see terrain change color at night, and notice that a different seed produces a different layout? If yes, the foundation is solid.

**Fun checkpoint:** Does the blight spread visibly? Can you watch it consume a forest tile by tile?

**Challenge checkpoint:** Does night reduce vision? Can you get lost?

---

### Phase 2: The Browser Client (Weeks 3-4)

**Goal:** The game runs entirely in the browser — engine, renderer, input, and saves.

**Deliverables:**
- [ ] TypeScript engine in Web Worker (world gen, blight sim, combat, AI)
- [ ] Vanilla JS Canvas renderer (**dynamic viewport: 80x30 to 120x60, default 100x45**)
- [ ] **Dynamic resizing** (browser window resize recalculates viewport)
- [ ] **Zoom levels** (`Z` key: far/normal/close)
- [ ] Glyph mapping JSON loaded and applied
- [ ] Keyboard input capture (vi-keys, numpad, arrows)
- [ ] Mouse input (click to move, right-click context menus, hover tooltips)
- [ ] Sidebar rendering (stats, mini-map)
- [ ] Message log rendering
- [ ] Basic animation (blight pulse, water cycle)
- [ ] localStorage save/load system
- [ ] Deploy to GitHub Pages / Vercel (free hosting)

**Engagement checkpoint:** Can a friend open a URL with `?seed=7f3a9c`, see the same world you see, resize their browser, and have the viewport adapt? If yes, the architecture works.

**Fun checkpoint:** Does the blight pulse look cool? Does consecration feel satisfying to watch?

**Challenge checkpoint:** Can you actually get lost at night? Does the mini-map help but not solve everything?

---

### Phase 3: Gathering & Tools (Week 5)

**Goal:** The player can gather resources, craft basic tools, and feel the rhythm of survival.

**Deliverables:**
- [ ] Resource spawning (wood, stone, berries, fish, deer)
- [ ] Tool system (flint knife, stone axe, pick, bow)
- [ ] Gathering actions (chop, mine, forage, hunt, fish)
- [ ] Inventory and weight system
- [ ] Tool degradation
- [ ] Basic crafting (axe, pick, spear, knife)
- [ ] Hunger and food consumption
- [ ] Thirst and water gathering

**Engagement checkpoint:** Does gathering feel good? Is there a visible yield? Does the axe degrade noticeably?

**Fun checkpoint:** Can you chop a tree and see it disappear? Can you eat a berry and see Hunger drop?

**Challenge checkpoint:** Do tools break at the worst time? Do you run out of food if you don't plan?

---

### Phase 4: The Blight & The Priest (Week 6)

**Goal:** The core mechanic works. Blight spreads, the Priest pushes it back.

**Deliverables:**
- [ ] Blight spread algorithm (1 tile/day, escalation rules)
- [ ] Consecration rite (radius-based, resource cost, Faith cost)
- [ ] Holy Ground creation and visual distinction
- [ ] Corruption stat (gain from blight, blighted resources)
- [ ] Priest Vocation (consecrate, bless water, basic healing)
- [ ] Blight effects on terrain (forest withers, water corrupts)
- [ ] First hostile: Corrupted Wolf (basic AI, pack behavior)

**Engagement checkpoint:** Can you watch blight advance and feel urgency? Can you push it back and feel relief?

**Fun checkpoint:** Does consecration have a visual pulse? Does the gold `+` feel warm and safe?

**Challenge checkpoint:** Does the blight outpace early-game consecration? Do you need to choose which ground to save?

---

### Phase 5: Building & The Craftsman (Week 7)

**Goal:** The player can build a base, and it feels like a base.

**Deliverables:**
- [ ] Craftsman Vocation (blueprints, freeform building)
- [ ] 5 Tier-1 blueprints (Lean-To, Firepit, Longhouse, Forge, Storehouse)
- [ ] Construction stages (ghost, planned, framed, complete)
- [ ] Ghost rendering (dashed outline, material checklist)
- [ ] Structure bonuses (warmth, storage, decay protection)
- [ ] Pilgrim system (rescue, basic AI, 1 role: Laborer)
- [ ] Mood system (basic: hopeful/cautious/desperate/doomed)
- [ ] Chapel recognition (soft blueprint)

**Engagement checkpoint:** Does building a wall feel like progress? Do pilgrims help and make the settlement feel alive?

**Fun checkpoint:** Does the ghost outline make planning satisfying? Do you watch pilgrims hammer and feel like a leader?

**Challenge checkpoint:** Do construction stages create vulnerability? Does a half-built wall fail to stop wolves?

---

### Phase 6: Winter & The Woodsman (Week 8)

**Goal:** The seasonal cycle creates pressure, and the Woodsman feels different.

**Deliverables:**
- [ ] Woodsman Vocation (speed, tracking, Read the Woods, camps)
- [ ] Season system (spring, summer, autumn, winter)
- [ ] Winter mechanics (snow cover, warmth drain, ice, reduced foraging)
- [ ] Autumn stockpile pressure (visible resource depletion)
- [ ] Blood Moon event (special night, blight surge, hostile spawn spike)
- [ ] Clean Spring detection (Woodsman passive)
- [ ] Advanced hostiles: Wendigo (mimicry, corruption aura)

**Engagement checkpoint:** Does autumn feel urgent? Do you feel the need to stockpile? Does winter feel like a siege?

**Fun checkpoint:** Does the first snow look beautiful and terrifying? Does the Blood Moon tint the screen red?

**Challenge checkpoint:** Does winter kill unprepared players? Do camps expire and force hard choices?

---

### Phase 7: The First Manifestation (Week 9)

**Goal:** The Drowned Choir is defeatable, and the fight feels like a culmination.

**Deliverables:**
- [ ] The Drowned Choir (boss entity, spawn rules, abilities)
- [ ] Boss arena mechanics (dry land vs. water, brazier requirements)
- [ ] 3 solution paths (Priest rite, Woodsman traps, Craftsman dock siege)
- [ ] Boss loot (Drowned Silver, Tier 2 unlock)
- [ ] The Chronicle (death entries, legacy drops)
- [ ] Lost Scripture system (random drops, cross-class learning)
- [ ] Tier 2 blueprints unlocked (Watchtower, Infirmary, Dock)

**Engagement checkpoint:** Does the boss feel like a puzzle, not a DPS check? Do you want to try a different Vocation's solution?

**Fun checkpoint:** Does the boss entrance feel dramatic? Does victory feel earned?

**Challenge checkpoint:** Does the boss kill you the first time? Do you understand why?

---

### Phase 8: The Full Bestiary (Week 10)

**Goal:** The world is dangerous and varied.

**Deliverables:**
- [ ] All enemy types: Wolf, Bear, Corrupted Deer, Wendigo, Shadow, Drowned, Revenant
- [ ] Enemy AI behaviors (pack, charge, phase, grab, mimicry)
- [ ] Fear effects (panic, drop weapon, freeze)
- [ ] Status effects (bleeding, blighted wound, frozen, cursed)
- [ ] Combat system (turn-based, 2 AP, damage types, degradation)
- [ ] Weapon roster (melee, ranged, traps, armor)
- [ ] Death types and Chronicle entries

**Engagement checkpoint:** Do enemies feel distinct? Do you change tactics for each?

**Fun checkpoint:** Does killing a Wendigo with a silver trap feel clever? Does a Shadow appearing behind you make you jump?

**Challenge checkpoint:** Do enemies kill you in fair fights? Do you need to prepare the battlefield?

---

### Phase 9: Pilgrims & Mood (Week 11)

**Goal:** The settlement feels alive, and pilgrim management is a real system.

**Deliverables:**
- [ ] All pilgrim roles (Laborer, Acolyte, Hunter, Smith, Patient)
- [ ] Pilgrim AI (work, sleep, eat, pray, flee, despair)
- [ ] Pilgrim events (death, suicide, finding, blessing)
- [ ] Mood system fully implemented (all 4 tiers, ambient text)
- [ ] Pilgrim limits (5 max, resource consumption)
- [ ] Cemetery system (named graves, mood effects)
- [ ] Confessional structure (cures Corruption)

**Engagement checkpoint:** Do you care when a pilgrim dies? Does their name appear in The Chronicle?

**Fun checkpoint:** Do acolytes chanting at night create atmosphere? Does a doomed settlement feel heavy?

**Challenge checkpoint:** Do pilgrims consume too much food? Do you regret rescuing them?

---

### Phase 10: Polish & The Endgame (Week 12)

**Goal:** The prototype is smooth, atmospheric, and ends with a choice.

**Deliverables:**
- [ ] All 5 regions (Shallows, Black Pines, Frozen Straits, Mire, Bluffs)
- [ ] All 5 Manifestations (at least placeholder AI for 2-5)
- [ ] 3 endings (Sanctuary, Passage, Bastion) — at least 1 fully implemented
- [ ] Title screen, character creation, death screen
- [ ] Sound design (ambient: wind, chanting, wolves; cues: consecration, trap, death)
- [ ] UI polish (smooth animations, responsive input, clear feedback)
- [ ] Bug fixes, balance passes, difficulty tuning
- [ ] Playtest with 5+ external players

**Engagement checkpoint:** Do playtesters want a second run immediately? Do they ask "what if I tried Woodsman?"

**Fun checkpoint:** Does the title screen set the tone? Does the death screen feel like a story, not a failure?

**Challenge checkpoint:** Do playtesters die in the first week? Do they understand why? Do they succeed on run 3-5?

---

## 6. Milestone Checkpoints

| Week | Demo Question | Pass Criteria |
|------|--------------|---------------|
| 2 | "Can you walk around a map?" | Procedural generation, day/night, basic rendering |
| 4 | "Can you play it in a browser?" | WebSocket connection, input, rendering, sidebar |
| 6 | "Can you push back the blight?" | Consecration works, blight spreads, wolves spawn |
| 8 | "Can you survive winter?" | Seasons cycle, winter kills the unprepared, stockpiling matters |
| 9 | "Can you beat the first boss?" | Drowned Choir defeatable, 3 paths work, loot drops |
| 12 | "Would you buy this?" | Playtesters engage for 2+ hours, ask about release |

---

## 7. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Blight algorithm is boring** | Medium | High | Prototype it in Week 2. If it feels like a paint flood, add surge events and regional variation. |
| **Web client is too slow** | Low | High | Use requestAnimationFrame, batch draws, only render changed cells. Test on low-end hardware. |
| **Pty protocol is over-engineered** | Medium | Medium | Start simple. If `DRAW x y char fg bg` is enough, use that. Add complexity only when needed. |
| **Pilgrim AI is annoying** | Medium | High | Keep AI simple (state machine: work -> eat -> sleep). Complex emergent behavior is a stretch goal. |
| **Not challenging enough** | Medium | High | Tune numbers aggressively. Starvation should happen. Winter should kill. Blight should outpace early consecration. |
| **Not fun enough** | Low | High | Juicy feedback is cheap (screen shake, sound cues, color pulses). Implement early and often. |
| **Scope creep** | High | High | Stick to the 12-week plan. Manifestations 2-5 can be placeholders. Tile packs are post-release. |

---

## 8. Success Metrics

**For the 12-week prototype:**
- [ ] A new player can complete a run (reach and defeat the Drowned Choir) in under 2 hours.
- [ ] A new player dies 3-5 times before their first victory.
- [ ] A player can share their seed via URL (`?seed=7f3a9c`) and challenge others to survive the same world.
- [ ] Resizing the browser window feels natural and does not break the game.
- [ ] The prototype runs entirely in the browser with zero backend cost.
- [ ] A player who wins once wants to try a different Vocation immediately.
- [ ] A player who wins with all 3 Vocations wants to try a hard mode.
- [ ] The average play session is 45+ minutes.
- [ ] The Chronicle is quoted by playtesters ("I found my own body from last run!")

**For the full release:**
- [ ] All 5 Manifestations are unique, memorable, and require different tactics per Vocation.
- [ ] The 3 endings feel distinct and emotionally resonant.
- [ ] Mod support (tile packs, custom maps) is documented and functional.
- [ ] Optional backend (Go) for cloud saves, leaderboards, and multiplayer co-op (2-3 players, shared world).
- [ ] The game is reviewed as "the most atmospheric ASCII survival game since Dwarf Fortress."

---

## 9. Summary

| Pillar | How We Achieve It |
|--------|-------------------|
| **Engaging** | Asymmetric Vocations, procedural discovery, Chronicle legacy, Mood system, seasonal urgency |
| **Fun** | Visible feedback for every action, juicy audio/visual cues, construction progress, pilgrim rescue |
| **Challenging** | Scarcity, time pressure, blight escalation, no perfect safety, instructive death, hard modes |

The 12-week roadmap builds from engine to client to mechanics to content to polish. Each week has a concrete deliverable and a checkpoint question. The goal is not a finished game. It is a **convincing promise** of what the finished game will be.

---

Document Version 1.0
The Wilds of Canaan - Development Roadmap & Design Playbook
