# The Wilds of Canaan
## The Chronicle: Deep System Design Document

---

## 1. Philosophy

The Chronicle is not a scoreboard. It is not an achievement list. It is the **memory of the world.** Every run leaves traces — bodies, journals, warnings, blessings — that persist into future runs. The wilderness is not empty because it is full of the dead.

The Chronicle serves three purposes:
- **Legacy:** Death is not erasure. It is contribution.
- **Wisdom:** Past failures teach future survivors.
- **Atmosphere:** The world feels old, haunted, and real.

---

## 2. Chronicle Structure

### 2.1 The Entry

Each Chronicle entry is a structured object:

```typescript
interface ChronicleEntry {
    id: string;              // UUID
    seed: string;            // World seed
    day: number;             // In-game day
    tick: number;            // In-game tick (for ordering)
    type: ChronicleType;     // Category
    author: string;          // "Pilgrim", "Brother Thomas", or anonymous
    text: string;            // The narrative text
    metadata: {
        position?: {x: number, y: number};  // Where this happened
        vocation?: Vocation;
        survivedDays?: number;
        causeOfDeath?: string;
        manifesto?: string;  // Player's final words (optional)
    };
}

type ChronicleType = 
    | 'arrival'      // First day
    | 'daily'        // Routine log
    | 'event'        // Significant occurrence
    | 'death'        // Final entry
    | 'warning'      // Found in world (another player's)
    | 'map'          // Partial map data
    | 'scripture'    // Lost Scripture found
    | 'grave'        // Burial marker
    | 'miracle'      // Unusual survival
    | 'despair';     // Mood collapse
```

### 2.2 The Chronicle of the Current Run

Every run generates its own Chronicle. It is written automatically by the game engine, not by the player. The player can add **annotations** (marked with `>`), but the core text is authored by the system.

**Example — Full Chronicle:**
```
The Chronicle of Brother Elias
Vocation: Priest      Survived: 14 Days

Day 1:   We made shore. The ship is splinters. I am alone.
         I have a knife, a cloak, and the Psalm of Protection.
         The trees are wrong. They grow too straight.

Day 2:   Found clean water. Thank God. Consecrated a small plot.
         The blight recoiled. I wept.

Day 3:   Built a chapel. It is small. It is enough.
         I found a body on the shore. A Woodsman. He drowned.
         I buried him facing east. His name was Jonah.

Day 5:   The Hollow Stag is not a legend.
         I saw it at the edge of the Black Pines.
         It wore the antlers of a dead king.
         I fled. It did not follow.

Day 7:   Found a survivor. Thomas. He had nailed his own hand
         to a tree. I cut him free. He does not speak.
         He carries stone. God provides.

Day 10:  The blight has reached the potato cellar.
         My wards are failing. I need more salt.

Day 12:  Thomas died in the night. The blight took him.
         I performed Last Rites. He did not rise.
         I am alone again.

Day 14:  Salt is gone. I can hear the Choir at the ice's edge.
         I will attempt the Rite unprepared.
         If this is found, bury me facing east.

         > [Player annotation]: Should have built the storehouse.

              [ Here ends his account ]
```

### 2.3 Chronicle Generation Rules

The engine generates entries based on events, not random text:

| Event | Entry Type | Template |
|-------|-----------|----------|
| Day start | `daily` | "Day {N}: {weather description}. {mood description}." |
| First shore landing | `arrival` | "We made shore. The ship is {condition}. I am {alone/with others}." |
| Found Clean Spring | `event` | "Found clean water. {gratitude/praise}. {consecrated/drank}." |
| Built Chapel | `event` | "Built a chapel. It is {size}. It is {adequate/insufficient}." |
| Found body | `event` | "Found a body. A {vocation}. {condition}. I {buried/left them}." |
| Rescued pilgrim | `event` | "Found a survivor. {name}. {condition description}. {current behavior}." |
| Pilgrim death | `event` | "{name} died. {cause}. I {performed Last Rites/left them}." |
| Mood shift (Desperate) | `despair` | "{settlement description}. {pilgrim behavior}. {personal feeling}." |
| Blight reaches base | `warning` | "The blight has reached {structure}. My wards are {condition}." |
| Manifestation spotted | `warning` | "The {name} is not a legend. {description}. {action taken}." |
| Death | `death` | "{final situation}. {final action}. {final words}." |

**Variations:** Each template has 3-5 variants. The engine selects based on:
- Vocation (Priest uses religious language, Woodsman uses natural, Craftsman uses practical)
- Mood (Hopeful entries are longer; Desperate entries are fragmented)
- Season (Winter entries mention cold; Summer entries mention abundance)

---

## 3. The World Chronicle (Cross-Run Persistence)

### 3.1 What Persists

When a run ends, certain Chronicle entries are saved to the **World Chronicle** — a global repository for that seed:

| Persists? | Entry Type | Why |
|-----------|-----------|-----|
| **Yes** | `death` | Future players find your body and Chronicle. |
| **Yes** | `grave` | Burial markers remain in the world. |
| **Yes** | `warning` | Warnings about Manifestations, blight routes. |
| **Yes** | `map` | Partial map data (explored areas). |
| **Yes** | `scripture` | Lost Scriptures are physical objects in the world. |
| **No** | `daily` | Too voluminous. |
| **No** | `event` (routine) | Only significant events persist. |
| **No** | `despair` | Too personal. |

### 3.2 Finding Past Chronicles

In a new run on the same seed, the player discovers past Chronicles:

```
[MSG] You find a weathered journal half-buried in snow.
[MSG] It is the Chronicle of Brother Elias. He survived 14 days.
```

**Reading the Chronicle:**
- Grants **partial map** (all areas Elias explored are revealed on your map).
- Grants **one Lost Scripture** (random: Elias knew something you don't).
- Grants **a warning** (Elias's final entry is displayed).

**Finding a body:**
```
[MSG] You find a body. A Priest, frozen, facing east.
[MSG] His hand clutches a journal. His name was Elias.
```

**Looting a body:**
- Retrieve their **best item** (weapon, armor, or tool).
- Retrieve their **remaining resources** (food, salt, holy water).
- Risk: If not given Last Rites, the body rises as a Revenant in 1 day.

### 3.3 The Graveyard

Pilgrims and players who are given Last Rites are buried. Their graves persist:

```
+------------------------------------------------------------------+
|                                                                  |
|    ..............                                                |
|    ...++##++....                                                 |
|    ..+#**#++....                                                 |
|    ..+#@*#++....                                                 |
|    ...++##++....                                                 |
|    ....++++......                                                |
|    .......+.......  [Here lies Brother Elias]                    |
|    .......++......  [Priest. 14 days. Facing east.]              |
|    ........+......                                               |
|    ...............                                               |
|                                                                  |
+------------------------------------------------------------------+
```

**Grave effects:**
- **Mood +5** to all pilgrims in 10-tile radius ("We are not the first. We will not be the last.").
- **Faith +10%** when praying at a grave (once per day).
- **Corruption -5** when performing Last Rites at a grave (the dead help the living).

### 3.4 The Seed Memory

Each seed has a "memory" — the accumulation of all Chronicles from all runs:

```typescript
interface SeedMemory {
    seed: string;
    totalRuns: number;
    totalDeaths: number;
    totalVictories: number;  // Any ending
    longestSurvival: number;  // Days
    mostCommonDeath: string;
    graves: Grave[];
    chronicles: ChronicleEntry[];
    mapRevealed: Set<string>;  // "x,y" tiles
}
```

**The seed gets harder over time:**
- Every 10 deaths on a seed: Blight spreads 5% faster.
- Every victory on a seed: Manifestations gain one new ability.
- This prevents "solved" seeds. The community cannot just publish the "optimal route."

---

## 4. The Chronicle UI

### 4.1 In-Game View

Press `L` to open the Chronicle:

```
+------------------------------------------------------------------+
| The Chronicle - Brother Elias (Day 14)              [Esc] Close  |
+------------------------------------------------------------------+
|                                                                  |
|  Day 1: We made shore...                                         |
|  Day 2: Found clean water...                                     |
|  Day 3: Built a chapel...                                        |
|  Day 5: The Hollow Stag...                                       |
|  Day 7: Found a survivor...                                      |
|  Day 10: The blight has reached...                               |
|  Day 12: Thomas died...                                          |
|  Day 14: Salt is gone...                                         |
|                                                                  |
|  [Scroll: Up/Down]  [Annotate: A]  [Share: S]  [Export: E]      |
+------------------------------------------------------------------+
```

### 4.2 Death Screen

The death screen IS the Chronicle:

```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Chronicle of Brother Elias                         |
|           Vocation: Priest      Survived: 14 Days                |
|           Cause: Starvation (after blight reached cellar)        |
|                                                                  |
|   [Full Chronicle text, as above]                                |
|                                                                  |
|   Seed: 7f3a9c                                                   |
|   This seed has seen 47 deaths and 3 victories.                  |
|   Longest survival: 34 days (Craftsman).                         |
|                                                                  |
|   [N]ew Pilgrimage    [S]ame Seed    [H]elp    [Share]          |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

### 4.3 Share Format

The Chronicle can be exported as text:

```
The Wilds of Canaan - Chronicle Export
=======================================

Seed: 7f3a9c
Player: Brother Elias
Vocation: Priest
Survived: 14 Days
Cause: Starvation

Day 1: We made shore...
[...full text...]

Share this seed: https://canaan.game/?seed=7f3a9c
```

Or as an image (auto-generated ASCII screenshot of the death screen).

---

## 5. Technical Implementation

### 5.1 Storage

**Current run:** In-memory (JavaScript object). Saved to `localStorage` every 10 turns:

```typescript
// Auto-save
setInterval(() => {
    const save = {
        world: engine.serialize(),
        chronicle: chronicle.entries,
        tick: engine.tick
    };
    localStorage.setItem('canaan_save', JSON.stringify(save));
}, 10000);  // Every 10 seconds
```

**World Chronicle (cross-run):**
```typescript
// Append to seed-specific Chronicle
const seedKey = `canaan_chronicle_${seed}`;
const existing = JSON.parse(localStorage.getItem(seedKey) || '[]');
existing.push({
    type: 'death',
    author: playerName,
    survivedDays: engine.day,
    cause: engine.causeOfDeath,
    text: chronicle.toString(),
    mapRevealed: engine.map.getExploredTiles()
});
localStorage.setItem(seedKey, JSON.stringify(existing));
```

**Size limit:** `localStorage` is ~5MB. A Chronicle entry is ~2KB. A seed with 100 deaths = ~200KB. Well within limits.

### 5.2 Protocol Integration

The Chronicle generates protocol lines for the client:

```
CHRONICLE Day 14
CHRONICLE "Salt is gone. I can hear the Choir..."
CHRONICLE_END
```

The client renders these in the message log and stores them in the Chronicle panel.

### 5.3 Generation Algorithm

```typescript
function generateEntry(event: GameEvent): ChronicleEntry {
    const templates = getTemplates(event.type, player.vocation, player.mood);
    const template = selectTemplate(templates, event);

    const text = template
        .replace('{name}', event.target?.name || 'the survivor')
        .replace('{day}', String(engine.day))
        .replace('{weather}', engine.weather.description)
        .replace('{mood}', engine.mood.label.toLowerCase());

    return {
        id: generateUUID(),
        seed: engine.seed,
        day: engine.day,
        tick: engine.tick,
        type: event.type,
        author: player.name,
        text,
        metadata: {
            position: player.position,
            vocation: player.vocation,
            survivedDays: engine.day
        }
    };
}
```

---

## 6. Summary

| Feature | Purpose |
|---------|---------|
| **Auto-generated entries** | The game writes the story. The player lives it. |
| **Vocation-specific language** | Priests sound religious, Woodsmen sound natural. |
| **Cross-run persistence** | Deaths become landmarks. The world remembers. |
| **Partial map transfer** | Past explorers help future ones. |
| **Lost Scripture transfer** | Cross-class learning through legacy. |
| **Grave effects** | The dead protect the living. |
| **Seed memory** | Seeds evolve. The community cannot "solve" them. |
| **Shareable exports** | Stories spread. Seeds become challenges. |

The Chronicle is the soul of Canaan. It turns a survival game into a story game. It turns death into legacy. It turns a single-player experience into a communal one — not through multiplayer, but through shared memory.

---

Document Version 1.0
The Wilds of Canaan - The Chronicle: Deep System Design Document
