# The Wilds of Canaan
## ASCII Visual Design Document

---

## 1. Philosophy

The visual identity of The Wilds of Canaan is built on contrast: the warm gold of consecrated ground against the pulsing purple of blight fog. The game does not need detail, it needs readability at a glance. A player in winter, starving, at 3 AM, surrounded by blight, must be able to assess their situation in under one second.

Rules:
- One character = one tile (primary view).
- Color carries more information than character shape.
- Animation is subtle: character cycling and color pulsing only.
- The Blight is the star of the show.

---

## 2. Top-Down Grid: The Primary View

This is the default viewport. One char per tile. Fast, readable, classic.

### 2.1 Basic Terrain Palette

```
..........................................................
..........................................................
..........^^^^^^^^^^......................................
........^^^^^^^^^^^^^^^^..................................
.......^^^^^""""""^^^^^..................................
......^^^^""++++++""^^^^................................
.....^^^^"+++####+++"^^^^.................................
....^^^^"+##++++++##+"^^^^..............................
...^^^^"+#++++++++++#+"^^^^...............................
...^^^^"+#++++@+++++#+"^^^^...............................
...^^^^"+#++++++++++#+"^^^^...............................
....^^^^"+##++++++##+"^^^^................................
.....^^^^"+++####+++"^^^^.................................
......^^^^""++++++""^^^^................................
.......^^^^^""""""^^^^^..................................
........^^^^^^^^^^^^^^^^..................................
..........^^^^^^^^^^......................................
..........................................................
```

Key:
| Symbol | Meaning | Color |
|--------|---------|-------|
| . | Unexplored / empty plains | Dark grey |
| , | Explored plains | Light grey |
| ^ | Forest (The Black Pines) | Dark green |
| ~ | Water (The Frozen Straits) | Cyan |
| = | Ice | White / light cyan |
| - | Cracking ice | Yellow (warning) |
| " | Blight fog (low intensity) | Purple |
| = | Blight fog (high intensity) | Dark purple |
| + | Holy ground / consecrated earth | Gold / white |
| # | Structure wall (chapel, cabin) | Brown / grey |
| @ | Player | White (bright) |
| * | Fire / light source | Red / yellow (pulsing) |
| ! | Dropped item / loot | Yellow |
| ? | Unknown / suspicious tile | Flickering grey |

---

### 2.2 Blight Progression (The Star Mechanic)

Blight is not binary. It has five visual stages that tell the player exactly how much danger they are in.

Stage 1: Clean (0-20)
```
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
```
Color: Light grey. Barely visible ground. Safe.

Stage 2: Tainted (21-40)
```
;;;;;;;;;;;
;;;;;;;;;;;
;;;;;;;;;;;
```
Color: Grey-green. Faint discoloration. No immediate danger, but blight is spreading.

Stage 3: Blighted (41-60)
```
"""""""""""
"""""""""""
"""""""""""
```
Color: Purple. Mist/fog. Hostile spawns begin. Agriculture fails.

Stage 4: Corrupted (61-80)
```
===========
===========
===========
```
Color: Dark purple. Thick, clinging fog. Building decay accelerates. Personal Corruption gain.

Stage 5: Hell (81-100)
```
%%%%%%%%%%%
%%%%%%%%%%%
%%%%%%%%%%%
```
Color: Black on dark red. Visible rot, almost solid. Near-certain death without holy protection.

Animation: Cycle between " and = every 2-3 seconds for active blight zones. It looks like breathing fog.

---

### 2.3 Holy Ground: The Priest's Domain

Holy ground uses warm colors (gold/white on black) and geometric patterns that visually push back the blight.

Small Chapel (early game):
```
..........
....++....
...+#+....
...+#+....
....++....
..........
```
Color: + is gold, # is brown. The + ring is the consecration radius.

Large Sanctuary (mid game):
```
..............
......++......
.....++++.....
....++##++....
...++#++#++...
...++#++#++...
...++#++#++...
....++##++....
.....++++.....
......++......
..............
```
The + pattern expands outward, consuming the . around it. When the Priest expands consecration, players see the + literally eat the ".

Consecration in Progress:
```
Before:          During:          After:
..........       ..........       ..........
..""""""..       ..""+"""..       ..++++++..
."""""""".       .""+##+"".       .++####++.
."""""""".  ->    ."+##+++.   ->    .+##++++#.
."""""""".       .""+##+"".       .++####++.
..""""""..       ..""+"""..       ..++++++..
..........       ..........       ..........
```
Animation: The + ring expands one tile per second during the rite. The " tiles flash white-to-gold as they convert.

---

### 2.4 The Three Vocations: Base Styles

Each Vocation creates visually distinct settlements.

Priest Base - The Sanctuary:
```
..............
......++......
.....++++.....
....++##++....
...++#**#++...
...++#@*#++...
...++#**#++...
....++##++....
.....++++.....
......++......
..............
```
Open, radiant, geometric. The * braziers are required for advanced rites. The @ is the altar.

Woodsman Base - The Nomad Camp:
```
^^^^....^^^^
^^^..!!..^^^
^^..!@@!..^^
^..!@~~@!..^
^..!@~~@!..^
^^..!@@!..^^
^^^..!!..^^^
^^^^....^^^^
```
Temporary, scattered. ! are warding salt markers (expire in 3-5 days). ~ are bedrolls. @ is the firepit. No walls, just the forest and salt.

Craftsman Base - The Bastion:
```
#############
#...........#
#..@........#
#...........#
#...####....#
#...#**#....#
#...####....#
#...........#
#############
```
Dense, fortified. Stone walls (#) resist blight decay. * are mechanical wards (clockwork prayer wheels). The Craftsman digs in; he does not expand.

---

### 2.5 Water & Ice

Open Water (The Shallows):
```
~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~
```
Color: Cyan. Animation: Cycle ~ -> w -> ~ every 1.5s.

Frozen Straits (Stable Ice):
```
================
================
================
================
```
Color: White / light cyan. Safe to walk. No animation.

Cracking Ice (Warning):
```
-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-=-
-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-=-
```
Color: Yellow. The ice is unstable. One more blight surge or heavy step and it breaks.

Broken Ice / Open Water in Winter:
```
~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~
```
Color: Dark cyan. You fall in. You freeze. You die.

---

### 2.6 Elevation (The Bluffs)

In top-down, elevation is abstract. Use character density and color intensity.

```
^^^^^^^^^^  ^5  Peak (The Bluffs)
^^^^^^^^^^  ^4  High ridge
^^^^^^^^^^  ^3  Rising ground
^^^^^^^^^^  ^2  Forested slope
,,,,,,,,,,  ,1  Lowland (The Mire)
~~~~~~~~~~  ~0  Water level
```

Color progression:
- ^5 = White (snow-capped, wind-scoured)
- ^4 = Light grey
- ^3 = Grey-green
- ^2 = Dark green
- ,1 = Brown/grey (swampy)
- ~0 = Cyan

Alternative: Use A for high forest/bluff, ^ for normal forest, , for lowland. Simpler, less visual noise.

```
AAAAAAAAAA
AA^^^^^^AA
A^^,,,^^A
A^,,,,,^A
A^,,,,,^A
A^^,,,^^A
AA^^^^^^AA
AAAAAAAAAA
```

---

## 3. Viewport & Display

### 3.1 Viewport Sizes

The game is designed for PC play via web browser. The viewport is dynamic and responsive.

| Context | Tiles | Pixel Size | Use Case |
|---------|-------|-----------|----------|
| Minimum | 80x30 | 1120x540 | Laptop, small window |
| Default (PC) | 100x45 | 1400x810 | Standard 1080p browser |
| Large | 120x60 | 1680x1080 | Fullscreen, 1440p monitors |
| Dynamic | Scales to browser | Responsive | Player resizes at will |

**Why 100x45 as default:**
- Exploration: ~50 tiles visibility in each direction. Spot blight lines, deer herds, water bodies.
- Base-building: A 6x4 Longhouse + walls fits comfortably without scrolling.
- Combat: See wolf pack flanking from the edge of vision.
- Blight drama: Watching purple fog advance across 40 tiles is unsettling at this scale.
- Performance: 4,500 cells per frame. At 60fps with only changed cells redrawn, Canvas 2D handles this easily.

### 3.2 Dynamic Sizing

The viewport responds to browser window size:

```javascript
const CELL_W = 14;
const CELL_H = 18;
const SIDEBAR_W = 250;  // Right sidebar width in pixels
const LOG_H = 120;      // Bottom log height in pixels

function resizeViewport() {
    const availableW = window.innerWidth - SIDEBAR_W;
    const availableH = window.innerHeight - LOG_H - TOP_BAR_H;

    VIEWPORT_W = Math.floor(availableW / CELL_W);
    VIEWPORT_H = Math.floor(availableH / CELL_H);

    canvas.width = VIEWPORT_W * CELL_W;
    canvas.height = VIEWPORT_H * CELL_H;

    // Tell engine the new viewport size
    ws.send(`RESIZE ${VIEWPORT_W} ${VIEWPORT_H}`);
}

window.addEventListener('resize', debounce(resizeViewport, 200));
```

The engine only emits cells within +/- VIEWPORT_W/2, +/- VIEWPORT_H/2 of the player, plus a 5-tile buffer for approaching entities.

### 3.3 Zoom Levels

| Zoom | Tile Size | Viewport (at 100x45 default) | Use Case |
|------|-----------|------------------------------|----------|
| Far | 10x12 | 140x54 tiles | Exploration. See more world. |
| Normal | 14x18 | 100x45 tiles | Default play. |
| Close | 20x24 | 70x33 tiles | Base inspection. Precision building. |

Zoom changes CELL_W/H but keeps the pixel canvas size constant, so the player sees fewer tiles but larger characters. Toggle with `Z` key.

### 3.4 The Full UI Layout (100x45 Default)

```
+--------------------------------------------------------------------------------------+
| The Wilds of Canaan    Day 14    Winter    -8F    Night  3:14 AM    Seed: 7f3a9c    |
+--------------------------------------------------------------------------------------+
|                                                                                        |
|    [100x45 ASCII grid = 1400x810 pixels]                                             |
|    [Player centered; world extends beyond viewport edges]                            |
|    [Visible: ~50 tiles in each direction]                                            |
|                                                                                        |
|    ..................................................................................|
|    ..................................................................................|
|    ..........^^^^^^^^^^..............................................................|
|    ........^^^^^^^^^^^^^^^^..........................................................|
|    .......^^^^^""""""^^^^^.........................................................|
|    ......^^^^""++++++""^^^^.......................................................|
|    .....^^^^"+++####+++"^^^^......................................................|
|    ....^^^^"+##++++++##+"^^^^.....................................................|
|    ...^^^^"+#++++++++++#+"^^^^....................................................|
|    ...^^^^"+#++++@+++++#+"^^^^....................................................|
|    ...^^^^"+#++++++++++#+"^^^^....................................................|
|    ....^^^^"+##++++++##+"^^^^.....................................................|
|    .....^^^^"+++####+++"^^^^......................................................|
|    ......^^^^""++++++""^^^^.......................................................|
|    .......^^^^^""""""^^^^^.........................................................|
|    ........^^^^^^^^^^^^^^^^.........................................................|
|    ..........^^^^^^^^^^..............................................................|
|    ..................................................................................|
|    ..................................................................................|
|                                                                                        |
+--------------------------------------------------------------------------------------+
| You are hungry.        |  Faith:    ########--  80%   (Priest)   |  [10x10 Mini-Map] |
| The blight creeps.     |  Warmth:   ######----  60%              |  ~~~~              |
| A wolf howls nearby.   |  Hunger:   ####------  40%              |  ~~~~ ^^           |
|                        |  Corrupt:  ##--------  15%              |  ~~  ^^            |
|                        |  Blight:   ##--------  20%  (local)     |      ^@^           |
|                        |  Season:   Winter                     |     ^^^            |
|                        |  Time:     Night (3:14 AM)            |    ^^              |
|                        |  Weather:  Snowing, -8F              |   ^^               |
|                        |  Seed:     7f3a9c                    |                    |
+------------------------|------------------------------------------+--------------------+
| > build wall                                           [TAB:Map]  [Z]oom: Normal     |
+--------------------------------------------------------------------------------------+
```

Layout breakdown:
- Top bar: Game title, Day, Season, Temperature, Time, Weather, **Seed**.
- Main viewport: 100x45 ASCII grid (1400x810 pixels, center).
- Right sidebar (250px): Stat bars, Season, Time, Weather, Seed, **Mini-Map**.
- Bottom left: Message log (last 4-5 events).
- Bottom center: Command prompt > _
- Bottom right: Context hints (e.g., [TAB:Map], [Z]oom, [E]Interact, [V]View).

---

### 3.1 Sidebar Detail

Faith bar (Priest only, or modified for other Vocations):
```
Faith:    ########--  80%
```
Color: Gold. Affects spell potency, vision clarity, and consecration radius.

Warmth bar:
```
Warmth:   ######----  60%
```
Color: Red when low (critical in winter). Blue when comfortable.

Hunger bar:
```
Hunger:   ####------  40%
```
Color: Green when full, yellow when moderate, red when starving.

Corruption bar:
```
Corrupt:  ##--------  15%
```
Color: Purple. Gains from blighted food, cursed wounds, dark areas. At 100%, you become a Revenant (game over).

Local Blight meter:
```
Blight:   ##--------  20%  (local)
```
Color: Purple. Shows the blight level of the tile you are standing on.

---

### 3.5 Mini-Map (Sidebar, 10x10)

```
+----------+
| ~~~~     |
| ~~~~ ^^  |
|  ~~  ^^  |
|      ^@^ |
|     ^^^  |
|    ^^    |
|   ^^     |
|          |
|          |
|          |
+----------+
```
Located in the right sidebar. A zoomed-out view of the local area. @ is player. ^ is forest. ~ is water. Updated in real-time. Shows approximately 200x200 tiles of surrounding terrain.

---

## 4. Creature Visibility & The Peripheral Horror

For Shadows (s), creatures only visible in peripheral light:

Normal view (Shadow is behind player, who faces north):
```
........
........
....@...
........
```
The s does not render. Instead, the tile shows a faint ? or flickers between . and ,.

When player turns around:
```
........
....s...
....@...
........
```
The s snaps into view in red. Jump scare in ASCII.

Wendigo (W) mimicking human screams:
```
........
....W...
....@...
........
```
Animation: Flicker between white (snow) and red (blood) every 0.5s. The W appears to bleed.

Drowned (z) underwater flicker:
```
~~~~~~~~
~~z~~~~~
~~~~~~~~
```
Animation: Only visible every other second. Underwater flicker. You see a shape, then it is gone.

Corrupted Wolf (w) pack behavior:
```
........
..w.w...
...@....
..w..w..
........
```
Color: Dark red. They stalk at the edge of vision, surrounding the player before closing in.

---

## 5. Animation Frames

### 5.1 Blight Pulse (Breathing Fog)

```
Frame 1:  Frame 2:  Frame 3:
"""""""   ========   """""""
"""""""   ========   """""""
"""""""   ========   """""""
```
Cycle: 2 seconds. Purple -> dark purple -> purple.

### 5.2 Fire / Brazier

```
Frame 1:  Frame 2:  Frame 3:
*         ^         *
^         *         ^
*         ^         *
```
Cycle: 0.3 seconds. Red -> yellow -> orange. Fast, urgent.

### 5.3 Water

```
Frame 1:  Frame 2:
~~~~~~~~   wwwwww
~~~~~~~~   wwwwww
~~~~~~~~   wwwwww
```
Cycle: 1.5 seconds. Cyan -> light cyan -> cyan.

### 5.4 Holy Ground Pulse

```
Frame 1:  Frame 2:
+++       +++
+@+       +@+
+++       +++
```
Color: Gold -> white -> gold. Slow, 3 seconds. Comforting.

### 5.5 The Burning Eye (Final Boss)

```
Frame 1:        Frame 2:        Frame 3:
........        ........        ........
..0.....        ..O.....        ..0.....
........        ........        ........
```
The 0 (zero) pulses between white and red. It is always centered. The screen shakes slightly (random . tiles flicker to ,).

---

## 6. Zoomed Base View: 3x3 Tiles

When the player enters their base or a chapel, toggle to a denser grid where one logical tile = 3x3 characters. This shows structure detail without leaving top-down.

Zoomed out (world map, 1x1):
```
..^#^..
..#@#..
..^#^..
```

Zoomed in (base view, 3x3 per tile):
```
+-----------+-----------+-----------+
|           |           |           |
|    ^^     |    ##     |    ^^     |
|   ^^^^    |    ##     |   ^^^^    |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    ##     |    @      |    ##     |
|    ##     |           |    ##     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    ^^     |    ##     |    ^^     |
|   ^^^^    |    ##     |   ^^^^    |
|           |           |           |
+-----------+-----------+-----------+
```

Or more practically, using pure ASCII for a chapel interior:

```
+-----------------------------------+
|                                   |
|              ___                  |
|             /   \                 |
|            /  *  \                |
|           |   @   |               |
|           |  ===  |               |
|           |_______|               |
|                                   |
|    +--+              +--+         |
|    |  |              |  |         |
|    +--+              +--+         |
|                                   |
+-----------------------------------+
```

* = altar candle. @ = player. === = altar. +--+ = pews/benches.

Toggle key: V (View) switches between world view and base view.

---

## 7. Screen Mockups

### 7.1 Title Screen

```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|                                                                  |
|           T H E   W I L D S   O F   C A N A A N                |
|                                                                  |
|                    "The land devours its own"                    |
|                                                                  |
|                                                                  |
|                        [N]ew Pilgrimage                          |
|                        [C]ontinue Chronicle                      |
|                        [O]ptions                                 |
|                        [Q]uit to DOS                             |
|                                                                  |
|                                                                  |
|              A survival of faith in an unholy land.              |
|                                                                  |
|                    ~ Press any key to begin ~                    |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

Decorative border using ~ to evoke water/untamed wilderness. Title in all-caps with spacing for gravitas. Subtitle is a found quote, not a tagline.

---

### 7.2 Character Creation (Vocation Select)

```
+------------------------------------------------------------------+
| The Wilds of Canaan - Choose Your Vocation                       |
+------------------------------------------------------------------+
|                                                                  |
|  [1] The Priest                                                  |
|      "I am the voice that holds back the dark."                  |
|      * Consecrate the land                                       |
|      * Heal corruption and restore faith                         |
|      * Weak in combat, dependent on wards                        |
|                                                                  |
|  [2] The Woodsman                                                |
|      "I read the forest like a psalm."                           |
|      * Track beasts and blight                                   |
|      * Move fast, strike from shadows                            |
|      * Cannot consecrate; must find Clean Ground                 |
|                                                                  |
|  [3] The Craftsman                                               |
|      "Stone and silver are my prayers."                          |
|      * Build fortresses that resist blight                       |
|      * Forge weapons and mechanical wards                        |
|      * Slow, dependent on prepared ground                        |
|                                                                  |
|                                                                  |
|  > _                                                             |
+------------------------------------------------------------------+
```

---

### 7.3 The Chronicle (Death Screen)

```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Chronicle of Brother John                          |
|           Vocation: Priest      Survived: 14 Days                |
|                                                                  |
|   Day 1:   We made shore. The trees are wrong.                   |
|            They grow too straight, as if pulled by a hand.       |
|                                                                  |
|   Day 3:   Found clean water. Thank God.                         |
|            I consecrated a small plot. The blight recoiled.      |
|                                                                  |
|   Day 7:   The Hollow Stag is not a legend.                      |
|            I saw it at the edge of the Black Pines.              |
|            It wore the antlers of a dead king.                   |
|                                                                  |
|   Day 12:  The blight has reached the potato cellar.             |
|            My wards are failing. I need more salt.               |
|                                                                  |
|   Day 14:  Salt is gone. I can hear the Choir at the ice's edge. |
|            I will attempt the Rite unprepared.                   |
|            If this is found, bury me facing east.                |
|                                                                  |
|              [ Here ends his account ]                           |
|                                                                  |
|           [R]eturn to main menu    [C]ontinue as new pilgrim   |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

Decorative border. The text is left-aligned, ragged, like a handwritten journal. The last line is always the same: [ Here ends his account ].

---

### 7.4 Inventory Screen

```
+------------------------------------------------------------------+
| Inventory - Brother John (Priest)                                |
+------------------------------------------------------------------+
|                                                                  |
|  [a] Blessed Silver Mace      (weapon)   [equipped]             |
|  [b] Wool Cloak               (armor)    [equipped]             |
|  [c] Prayer Book              (tool)     [equipped]             |
|  [d] Holy Water (3)           (consumable)                      |
|  [e] Salt Block (1)           (resource)                        |
|  [f] Blighted Venison (2)     (food)     [CORRUPTED]            |
|  [g] Flint & Tinder           (tool)                            |
|  [h] Pine Log (14)            (material)                        |
|  [i] Drowned Silver Ore (2)   (material)                        |
|                                                                  |
|  Weight: 34/50   |   Gold: 0   |   Faith: 80%                   |
|                                                                  |
|  [D]rop  [U]se  [E]quip  [C]raft  [TAB]Back                    |
+------------------------------------------------------------------+
```

Simple list. Corrupted items are flagged in red. Weight limit forces hard choices.

---

### 7.5 Crafting Screen

```
+------------------------------------------------------------------+
| Crafting - Forge                                                 |
+------------------------------------------------------------------+
|                                                                  |
|  [1] Silver Mace          (8 silver, 2 wood, 1 leather)         |
|      "A blunt instrument of holy wrath."                        |
|                                                                  |
|  [2] Warding Salt Ring    (5 salt, 1 holy water)                |
|      "Temporary consecration. Lasts 3 days."                    |
|                                                                  |
|  [3] Reinforced Palisade  (10 wood, 5 stone, 2 iron)            |
|      "Resists blight decay. +50% durability."                   |
|                                                                  |
|  [4] Mechanical Ward      (3 iron, 2 gears, 1 silver)           |
|      "Pushes back blight in a 3-tile radius."                   |
|                                                                  |
|  [5] Blessed Fishing Net  (4 twine, 2 wood, 1 holy water)       |
|      "Catches clean fish even in blighted water."               |
|                                                                  |
|  Materials:  Silver:8  Wood:14  Stone:5  Iron:3  Salt:1         |
|                                                                  |
|  > 2                                                             |
+------------------------------------------------------------------+
```

Craftsman gets a 20% material discount (not shown in UI, applied at craft time). Recipes are discovered by finding Lost Scriptures.

---

### 7.6 Map Screen (Zoomed Out)

```
+------------------------------------------------------------------+
| Map - The Wilds of Canaan                                        |
+------------------------------------------------------------------+
|                                                                  |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                    |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^^^^^^^^^^^^^^^                |
|  ~~~~~@~~~~~~~~~~~~~~~~~~~~~    ^^^^^^^^^^^^^^^^^^^^             |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^^""""""""""^^^^^^            |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^^""""""""""""^^^^             |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^""""""""""""""^^              |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ^""""""""""""""^               |
|                                   ^"""""""""""""^               |
|                                    ^"""""""""""^                |
|                                     ^^^^^^^^^^^                  |
|                                                                  |
|  [@] You are here    [^] Forest    [~] Water    ["] Blight      |
|                                                                  |
|  [TAB] Return to game    [M]ark waypoint    [C]enter on player  |
+------------------------------------------------------------------+
```

The map reveals explored areas. Unexplored tiles are blank ( ). Waypoints can be marked with !.

---

### 7.7 Combat / Encounter View

```
+------------------------------------------------------------------+
| The Wilds of Canaan    Day 14    Winter    -8F    Night  3:14 AM|
+------------------------------------------------------------------+
|                                                                  |
|    ............................................................. |
|    ............................................................. |
|    ..........^^^^^^^^^^......................................... |
|    ........^^^^^^^^^^^^^^^^..................................... |
|    .......^^^^^""""""^^^^^..................................... |
|    ......^^^^""++++++""^^^^...................................   |
|    .....^^^^"+++####+++"^^^^..................................   |
|    ....^^^^"+##++++++##+"^^^^.................................   |
|    ...^^^^"+#++++++++++#+"^^^^................................   |
|    ...^^^^"+#++++w+++++#+"^^^^........w.......................   |
|    ...^^^^"+#++++++++++#+"^^^^................................   |
|    ....^^^^"+##++++++##+"^^^^.................................   |
|    .....^^^^"+++####+++"^^^^..................................   |
|    ......^^^^""++++++""^^^^...................................   |
|    .......^^^^^""""""^^^^^..................................... |
|    ........^^^^^^^^^^^^^^^^..................................... |
|    ..........^^^^^^^^^^......................................... |
|    ............................................................. |
|    ............................................................. |
|                                                                  |
+------------------------------------------------------------------+
| A Corrupted Wolf pack surrounds you!                             |
| [1] Attack with Silver Mace    [2] Cast Banishment              |
| [3] Drink Holy Water           [4] Flee into the forest         |
+------------------------------------------------------------------+
```

Combat is turn-based. The viewport does not change; enemies appear as characters on the grid. The bottom bar becomes a combat menu.

---

### 7.8 Season Transitions

Spring (Thaw):
```
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```
Color: Light green. The snow melts. Rivers swell. Mud everywhere (;).

Summer (Growth):
```
^^^^^^^^^^
^^^^^^^^^^
^^^^^^^^^^
```
Color: Deep green. Forests are dense. Food is plentiful. Days are long.

Autumn (Harvest):
```
^^^^^^^^^^
^^^^^^^^^^
^^^^^^^^^^
```
Color: Orange / brown. Leaves fall. The last chance to stockpile before winter.

Winter (The Long Night):
```
**********
**********
**********
```
Color: White. Snow covers everything. * replaces ^ and ,. Movement is slow. Warmth is life. The Blood Moon rises.

---

### 7.9 Night vs. Day

Day:
```
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
```
Color: Full saturation. All terrain colors are bright. Vision radius: 12 tiles.

Dusk:
```
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
```
Color: Muted. Greens become grey-green. Vision radius: 8 tiles. Shadows begin to spawn.

Night:
```
..........
..........
..........
```
Color: Desaturated. Everything is grey or dark blue. Only light sources (*, + on Holy Ground) show true color. Vision radius: 5 tiles (without torch).

The Blood Moon (special night):
```
..........
..........
..........
```
Color: Red tint across the entire screen. All blight levels increase by 20. Hostile spawn rate triples. The Hollow Stag roams.

---

### 7.10 The Three Endings

Ending 1: The Sanctuary (Priest)
```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Sanctuary                                          |
|                                                                  |
|   You consecrated the Bluffs entirely. The land is healed.       |
|   The Burning Eye is sealed beneath a cathedral of light.        |
|   Pilgrims will find their way here, generation after generation.|
|                                                                  |
|   The Wilds of Canaan are wild no more.                          |
|   They are holy ground.                                          |
|                                                                  |
|                    [ The End ]                                   |
|                                                                  |
|           [M]ain Menu    [N]ew Pilgrimage    [Q]uit            |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

Ending 2: The Passage (Woodsman)
```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Passage                                            |
|                                                                  |
|   You did not defeat the Eye. You escaped it.                    |
|   The ship you built--birch and tar and prayer--                 |
|   carried you across the northern straits.                       |
|                                                                  |
|   Behind you, the Bluffs burn with an unholy light.              |
|   Ahead, the horizon is clean.                                   |
|   A new Canaan awaits.                                           |
|                                                                  |
|                    [ The End ]                                   |
|                                                                  |
|           [M]ain Menu    [N]ew Pilgrimage    [Q]uit            |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

Ending 3: The Bastion (Craftsman)
```
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|                                                                  |
|           The Bastion                                            |
|                                                                  |
|   You did not heal the land. You imprisoned the evil.            |
|   Beneath a vault of stone and silver,                           |
|   the Burning Eye rages in eternal darkness.                     |
|                                                                  |
|   The Wilds remain cursed.                                       |
|   But they are contained.                                        |
|   And you remain, the keeper of the lock.                        |
|                                                                  |
|                    [ The End ]                                   |
|                                                                  |
|           [M]ain Menu    [N]ew Pilgrimage    [Q]uit            |
|                                                                  |
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```

---

## 8. Isometric: The Exception

Isometric ASCII is not used for gameplay. It is reserved for static, decorative screens where the player is not making tactical decisions.

Title screen background (decorative only):
```
                    /\        /\        /                   /  \      /  \      /                    / ^^ \    / ^^ \    / ^^                  /______\  /______\  /______                /\      /\      /\      /               /  \    /  \    /  \    /                / ++ \  / "" \  / ++ \  / ~~              /______\/______\/______\/______```

Why this is acceptable here:
- The player is not moving or building.
- It is a single, static image.
- It creates visual interest for a screenshot or title card.
- It does not need to update 60 times per second.

Rule: If the screen requires real-time updates (gameplay, combat, inventory), use top-down. If the screen is static and decorative (title, death, ending), isometric is allowed as flavor.

---

## 9. Technical Implementation

### 9.1 Recommended Engines

| Engine | Pros | Cons |
|--------|------|------|
| Python + blessed | True terminal, cross-platform, easy color | Limited to terminal features |
| Python + bearlibterminal | Better color, sprite-like layering, easy input | Not a true terminal |
| C + ncurses | Maximum performance, massive maps | Harder to develop |
| Lua + LOVE2D + ASCII font | Smooth animation, sound, modern UI | Cheating (not true ASCII) |

Recommendation: Start with blessed (Python) for rapid prototyping. Switch to bearlibterminal if you need smoother animation or more than 16 colors.

### 9.2 Map Data Structure

```python
tile = {
    'terrain': 'forest',      # ^, ., ~, etc.
    'blight': 45,             # 0-100
    'holy': True,             # overrides blight visually
    'structure': 'chapel',    # None, 'wall', 'door', etc.
    'item': None,             # dropped gear
    'creature': 'wolf',       # None or creature ID
    'visible': True,          # FoW
    'explored': True,
    'elevation': 2            # 0-5
}
```

### 9.3 Rendering Order Per Tile

1. Terrain (base char + color)
2. Blight overlay (if present, semi-transparent or char swap)
3. Holy overlay (if present, gold tint)
4. Structure (if present)
5. Item (if present)
6. Creature (if present)

### 9.4 Color Palette (16-color terminal)

| Color | Usage |
|-------|-------|
| Black | Background, unexplored |
| Dark Grey | Explored plains |
| Light Grey | UI borders, text |
| Dark Green | Forest |
| Light Green | Clean grass, spring |
| Dark Cyan | Deep water |
| Light Cyan | Ice, shallow water |
| Dark Red | Hostile creatures, damage |
| Light Red | Fire, blood moon |
| Dark Purple | Blight (low) |
| Light Purple | Blight (high) |
| Dark Yellow | Warnings, cracking ice |
| Light Yellow | Holy ground, items, gold |
| Dark Blue | Night sky, deep water |
| Light Blue | Day sky, UI highlights |
| White | Player, text, snow |

### 9.5 Animation Budget

Maximum 3-4 animated tile types on screen at once.
- Priority 1: Blight fog (always animates)
- Priority 2: Water (if visible)
- Priority 3: Fire / braziers (if visible)
- Priority 4: Holy ground pulse (if visible)

Everything else is static. The human eye is drawn to motion; use it sparingly.

---

## 10. Summary

| View | Usage | Tile Size |
|------|-------|-----------|
| Top-down (1x1) | Primary gameplay (90% of the game) | 1 char |
| Top-down (3x3 zoom) | Base building, interior inspection | 3x3 chars |
| Isometric | Title screen, death screen, endings only | Decorative |
| Side-view | Not used | — |

The core visual principle: The player should be able to look at the screen and immediately answer three questions:
1. Where is the blight?
2. Where is safety?
3. Where am I?

If your ASCII layout answers those three questions in under one second, it is correct.

---

Document Version 1.0
The Wilds of Canaan - ASCII Visual Design Document
