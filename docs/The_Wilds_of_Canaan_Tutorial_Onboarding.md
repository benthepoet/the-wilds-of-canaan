# The Wilds of Canaan
## Tutorial & Onboarding Document

---

## 1. Philosophy

The first 10 minutes determine whether a player stays. Canaan is a hard game. It will kill you. But it must **teach you why before it kills you.** The tutorial is not a separate mode. It is the first run, guided by context.

**Principles:**
- **No tutorial level.** The game starts immediately. The tutorial is woven into the first run.
- **No walls of text.** Information appears when needed, where needed, in 1-2 sentences.
- **Diegetic teaching.** The game teaches through the world, not through pop-ups. A dead body teaches you about wolves. A ruined chapel teaches you about consecration.
- **Safe to fail.** The first death is expected and celebrated (Chronicle entry). The second death teaches more.

---

## 2. The First Run: The Shipwreck

### 2.1 Opening (0:00 - 0:30)

The game opens on the title screen. The player presses any key.

**Screen:**
```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           T H E   W I L D S   O F   C A N A A N                |
|                                                                  |
|                    "The land devours its own"                    |
|                                                                  |
|                                                                  |
|                        [N]ew Pilgrimage                          |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

**Player presses N.**

**Character creation appears.** Only one choice matters now: Vocation. The others are pre-selected (name: "Pilgrim", random seed).

```
+------------------------------------------------------------------+
| Choose Your Vocation                                             |
|                                                                  |
|  [1] The Priest  - "I am the voice that holds back the dark."    |
|  [2] The Woodsman - "I read the forest like a psalm."            |
|  [3] The Craftsman - "Stone and silver are my prayers."          |
|                                                                  |
|  > 1                                                             |
+------------------------------------------------------------------+
```

**The player selects Priest (recommended for first run).**

### 2.2 The Opening Narrative (0:30 - 1:00)

```
+------------------------------------------------------------------+
|                                                                  |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                  |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                  |
|    ~~~~~@~~~~~~~~~~~~~~~~~~~~~    ^^^^^^^^^^^^^^^^               |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^^^^^^^^^^^^^^^^^^^          |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^^""""""""""^^^^^^         |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^""""""""""""^^^^          |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^""""""""""""""^^           |
|    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^""""""""""""""^            |
|                                   ^"""""""""""""^            |
|                                    ^"""""""""""^             |
|                                     ^^^^^^^^^^^                  |
|                                                                  |
+------------------------------------------------------------------+
| You wash ashore. The ship is gone. The others are dead or        |
| drowned. You have a flint knife, a wool cloak, and the clothes   |
| on your back. Winter is coming.                                  |
|                                                                  |
| [Space] Continue                                                 |
+------------------------------------------------------------------+
```

**No controls explained yet.** Just atmosphere.

### 2.3 The First Action (1:00 - 2:00)

The player is on the shore. The message log shows:

```
You are hungry. (Hunger: 80%)
The wind is cold. (Warmth: 70%)

> _
```

**Context hint appears:**
```
[Arrow keys / hjklyubn] Move    [G]ather    [X]Examine    [?]Help
```

The player moves. Each movement shows the viewport shifting. After 3 moves:

```
You find a pine tree.
```

**Context hint updates:**
```
[Pine tree]  [G]ather wood    [X]Examine    [C]hop (needs axe)
```

The player presses `G`:

```
You gather 2 pine wood. Your flint knife dulls.
```

**Context hint updates:**
```
[Inventory: 2 wood]  [I]nventory    [C]raft    [?]Help
```

### 2.4 The First Danger (2:00 - 3:00)

The player explores. After 10 moves:

```
[MSG] A wolf howls in the distance. Northeast.
```

**Audio cue:** Distant howl, panned right.

**Context hint:**
```
[Wolf nearby]  [F]lee to shelter    [T]rap (needs materials)    [?]Help
```

The player does not need to act. The wolf is distant. But they are warned.

After 5 more moves:

```
[MSG] The wolf has spotted you. It approaches.
```

**Screen shake. Wolf icon (`w`) appears at edge of vision.**

**Context hint:**
```
[Wolf approaching]  [Sprint] Shift+move    [Enter structure]    [F]ight
```

If the player flees back to the shore (starting area):

```
[MSG] The wolf stops at the water's edge. It will not follow.
```

**Lesson learned:** Water is safety. Wolves fear it.

If the player fights:

```
[MSG] You strike the wolf with your flint knife. It bleeds.
[MSG] The wolf bites you. (-8 Health)
```

**Lesson learned:** Combat is dangerous. You are not strong.

### 2.5 The First Night (3:00 - 5:00)

Night falls. The screen desaturates. Vision radius drops.

```
[MSG] Night falls. The temperature drops. (Warmth: 50%)
```

**Context hint:**
```
[Cold]  [Build fire] needs 2 wood    [Find shelter]    [Keep moving]
```

The player has 2 wood from earlier. They press `C` (craft):

```
Craft: [F]irepit (2 wood)  [L]ean-to (4 wood, 1 hide)
```

They build a firepit:

```
[MSG] You build a firepit. The flame is small, but warm.
(Warmth: 65%)
```

**Visual:** Fire tile (`*`) appears. Orange glow on surrounding tiles.

**Audio:** Fire crackle fades in.

### 2.6 The First Death (5:00 - 10:00)

The first run is designed to end in death. The player will:
- Run out of food (Hunger drops to 0)
- Get cold (Warmth drops to 0)
- Encounter a wolf pack
- Or simply wander into the blight

**When death occurs:**

```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Chronicle of Pilgrim                               |
|           Vocation: Priest      Survived: 3 Days                 |
|                                                                  |
|   Day 1:   Washed ashore. Gathered wood. Built a fire.           |
|            A wolf stalked me. I fled to the water.               |
|                                                                  |
|   Day 2:   Explored inland. Found berries. Ate them.             |
|            The blight is visible to the east. Purple fog.        |
|                                                                  |
|   Day 3:   Starved. I had no food. The fire went out.            |
|            I walked toward the blight, hoping to find something. |
|            I found nothing.                                      |
|                                                                  |
|              [ Here ends his account ]                           |
|                                                                  |
|   Lessons:                                                       |
|   - Food rots. Stockpile before winter.                          |
|   - Fire needs wood. Gather daily.                               |
|   - The blight is not food. Do not enter it.                     |
|                                                                  |
|           [N]ew Pilgrimage    [S]ame Seed    [H]elp              |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

**The death screen teaches.** It does not just say "Game Over." It says why, and what to do differently.

### 2.7 The Second Run (10:00 - 20:00)

The player starts again. This time:
- They know about gathering wood.
- They know about the fire.
- They know about wolves.
- They know about starvation.

**The tutorial fades.** Context hints become less frequent. By Day 5, only critical hints appear (new enemy types, new mechanics). By Day 10, the player is on their own.

---

## 3. Contextual Hint System

### 3.1 Hint Triggers

Hints appear based on state, not time:

| Trigger | Hint | Frequency |
|---------|------|-----------|
| Hunger < 50% | "You are hungry. Find food." | Once per run |
| Warmth < 50% | "You are cold. Build a fire or wear warmer clothes." | Once per run |
| Blight tile visible | "Purple fog is blight. It corrupts. Avoid it." | Once per run |
| First hostile spotted | "Hostiles are dangerous. Flee or prepare." | Once per run |
| First night | "Night is cold and dark. Find shelter." | Once per run |
| First winter | "Winter has come. Food is scarce. Stay warm." | Once per run |
| First pilgrim found | "A survivor. They can help, but they need food." | Once per run |
| First Manifestation | "The [Name] approaches. Prepare." | Once per run |

### 3.2 Hint Suppression

Hints are suppressed if:
- The player has already performed the action successfully (e.g., built a fire after seeing the fire hint).
- The player has died to the related cause (e.g., died to starvation → food hints are permanently more detailed).
- The player has disabled hints in settings.

### 3.3 The `?` Key

Pressing `?` at any time opens the contextual help:

```
+------------------------------------------------------------------+
| Help - Current Situation                                         |
+------------------------------------------------------------------+
|                                                                  |
|  You are: A Priest on Day 4 of Winter.                           |
|  Location: The Black Pines (blighted).                           |
|  Status: Hungry, Cold, Corrupted (15%).                          |
|                                                                  |
|  Immediate concerns:                                             |
|  - Find food (berries are gone in winter; try ice fishing)       |
|  - Build a fire or find shelter (you have 1 wood)                |
|  - Purify yourself (Corruption is rising; find Holy Water)       |
|                                                                  |
|  Current threats:                                                |
|  - Wolf pack, 3 tiles northeast                                  |
|  - Blight surge imminent (Day 5)                                 |
|                                                                  |
|  Suggested actions:                                              |
|  [G]ather ice fish (needs hole in ice)                           |
|  [R]ite: Bless Flame (needs Holy Water)                          |
|  [F]lee toward shore (wolves fear water)                         |
|                                                                  |
+------------------------------------------------------------------+
```

This is not a generic manual. It is **situational advice** based on the current world state.

---

## 4. The Tutorial Bot (Optional)

For players who want to watch before playing:

### 4.1 Ghost Mode

The player starts a new run. A translucent `@` (the Ghost) appears and moves independently.

```
[MSG] The Ghost of a previous pilgrim walks beside you.
[MSG] It survived 14 days. Watch. Learn.
```

The Ghost performs optimal actions:
- Day 1: Gathers wood, builds fire, finds berries.
- Day 2: Explores, finds Clean Spring, consecrates ground.
- Day 3: Builds Chapel, rescues pilgrim.
- Day 4-7: Stockpiles for winter.
- Day 8+: Defeats first Manifestation.

The player can:
- **Watch:** The Ghost plays in real-time. The player observes.
- **Interrupt:** Press any key to take control. The Ghost vanishes.
- **Follow:** The player moves with the Ghost, mimicking its actions.

### 4.2 Commentary

The Ghost narrates via the message log:

```
[Ghost] "I gathered wood first. Fire is life."
[Ghost] "See the purple fog? That is blight. Never enter it."
[Ghost] "I consecrated this ground. Now I can build."
[Ghost] "Winter comes on Day 30. I need 30 days of food."
```

---

## 5. Difficulty Presets

At character creation, the player can select a difficulty that affects tutorial intensity:

| Preset | Tutorial | Death Penalty | Resource Scarcity | Blight Speed |
|--------|----------|---------------|-------------------|--------------|
| **Pilgrim** | Full hints, Ghost available | Chronicle only (no Corruption) | Abundant | Slow |
| **Settler** | Context hints only | Standard | Normal | Normal |
| **Exile** | No hints | Hardcore (save deleted) | Scarce | Fast |
| **Martyr** | No hints, no cross-class | Permadeath, no Chronicle legacy | Extreme | Extreme |

**Default:** Settler.

---

## 6. The First 30 Minutes: Learning Curve

| Time | Milestone | Teaching Goal |
|------|-----------|---------------|
| 0:00 | Title screen | Atmosphere, tone |
| 0:30 | Shipwreck narrative | Stakes, isolation |
| 1:00 | First movement | Controls |
| 2:00 | First gathering | Resources, tools |
| 3:00 | First wolf | Danger, fleeing |
| 5:00 | First night | Fire, warmth, time pressure |
| 8:00 | First blight sighting | The core threat |
| 10:00 | First death | Failure is learning |
| 12:00 | Second run starts | Application of lessons |
| 20:00 | First Chapel (if skilled) | Progression, Vocation identity |
| 30:00 | First Manifestation attempt | Endgame introduction |

**By 30 minutes:** The player should understand: movement, gathering, combat (avoid it), fire, hunger, warmth, blight, and the existence of Manifestations. They should not yet understand: crafting tiers, pilgrim management, Mood, cross-class learning, or the 3 endings.

---

## 7. Accessibility

### 7.1 Cognitive Load

- **Hint text:** Maximum 15 words per hint. No compound sentences.
- **Message log:** Last 5 messages visible. Older messages scroll off but are preserved (press `L` for full log).
- **Color dependency:** No critical information is color-only. Blight is `"` (shape) + purple (color). Holy ground is `+` (shape) + gold (color).
- **Speed:** Turn-based. No time pressure. The player can stare at the screen for 10 minutes.

### 7.2 Screen Reader Support

The message log is a live `<div>` with `aria-live="polite"`. Screen readers announce:

```
"You are hungry. The wind is cold. A wolf howls nearby."
"Faith: 80 percent. Warmth: 60 percent. Hunger: 40 percent."
"Corrupted Wolf, 3 tiles to the west."
```

The sidebar is real HTML (not canvas), so screen readers can navigate it.

### 7.3 Motor Accessibility

- **Mouse-only mode:** All actions clickable. No keyboard required.
- **Sticky keys:** Press `Shift` once to sprint until pressed again.
- **Auto-repeat:** Hold `G` to gather continuously until resource depleted or hostile spotted.
- **Pause:** `Esc` pauses the game (single-player only). Time stops. Menu appears.

---

## 8. Metrics

Track these to measure tutorial effectiveness:

| Metric | Target | Measurement |
|--------|--------|-------------|
| **First-run survival** | 2-4 days | Average days survived on first attempt |
| **Second-run survival** | 5-10 days | Average days survived on second attempt |
| **Chapel built by Day 10** | 30% of players | Event tracking |
| **First Manifestation reached** | 20% of players by 2 hours | Event tracking |
| **Hint dismissal rate** | <10% | How often players press `Esc` to close hints |
| **Ghost mode usage** | 40% of first-time players | Button click tracking |
| **Help key (`?`) usage** | <5% after Day 5 | Players should not need it |

---

## 9. Summary

| Feature | Purpose |
|---------|---------|
| **Integrated tutorial** | No separate mode. Learning is the first run. |
| **Contextual hints** | Information when needed, where needed. |
| **Diegetic teaching** | The world teaches through corpses, ruins, and weather. |
| **Celebrated death** | The Chronicle frames failure as story, not defeat. |
| **Ghost mode** | Optional watch-and-learn for hesitant players. |
| **Difficulty presets** | Pilgrim (guided) to Martyr (no help). |
| **Accessibility** | Screen readers, mouse-only, sticky keys, pause. |

The goal is simple: by the time a player dies twice, they should know why they died, what they could have done differently, and they should want to try again.

---

Document Version 1.0
The Wilds of Canaan - Tutorial & Onboarding Document
