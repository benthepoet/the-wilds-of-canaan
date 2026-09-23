# The Wilds of Canaan
## The Juice: Specific Effects & Polish Document

---

## 1. Philosophy

"Juice" is the term for making game interactions feel satisfying through visual, audio, and tactile feedback. It is the difference between "I pressed a button and a thing happened" and "I pressed a button and the world RESPONDED."

In Canaan, juice is not about flash. It is about **weight, consequence, and atmosphere.** Every action should feel like it matters.

---

## 2. Movement Juice

### 2.1 Footstep Feedback

| Terrain | Visual | Audio | Tactile |
|---------|--------|-------|---------|
| **Grass/Plains** | Tiny dust puff (`,`) | Soft crunch | — |
| **Snow** | Footprint (`'`) that fades in 5s | Sharp crunch, louder | — |
| **Ice** | Crack lines (brief) | Hollow thud | — |
| **Holy Ground** | Gold shimmer (brief) | Muted, almost silent | — |
| **Blight** | Purple residue on player char | Squelch, whisper | Screen tint (brief) |
| **Water** | Ripple rings | Splash | — |

### 2.2 Sprint

- **Visual:** Player char (`@`) leaves a faint trail (`'`) for 2 tiles that fades over 1 second.
- **Audio:** Heavy breathing that intensifies as Stamina drops below 50%.
- **Screen:** Subtle chromatic aberration at edges (suggests exertion).

### 2.3 Collision

- **Bump wall:** Player char shakes left-right once. Dull thud.
- **Bump hostile:** Screen flash (red, 100ms). Hostile snarls. Player grunts.
- **Bump blight (high):** Screen flash (purple, 200ms). Corruption +1. Whisper sound.

---

## 3. Gathering Juice

### 3.1 Chop Tree

**Sequence:**
1. **Wind-up:** Player char raises axe (1 frame).
2. **Strike:** Axe swings down. `*` spark at impact point.
3. **Impact:** Tree shakes (2 frames left-right). Wood chip particles (`'`) fly.
4. **Result:** Tree disappears. `2 wood` appears in inventory. Axe condition drops (subtle `!` on axe icon).

**Audio:** Chop (impact) + wood crack + rustle.

### 3.2 Mine Stone

**Sequence:**
1. **Strike:** Pick swings. `*` spark.
2. **Impact:** Stone shakes. Dust particles (`.`) fly.
3. **Result:** Stone remains (depleted). `2 stone` in inventory.

**Audio:** Dull clang + stone chip.

### 3.3 Gather Berries

**Sequence:**
1. **Reach:** Player char leans toward bush.
2. **Pluck:** Bush shakes. Berry particles (`o`) float up and vanish.
3. **Result:** Berries in inventory.

**Audio:** Soft rustle + pop.

---

## 4. Building Juice

### 4.1 Blueprint Placement

- **Ghost appears:** Dashed outline (`?`) fades in over 300ms.
- **Valid position:** Outline glows green. Material checklist appears (slide in from right, 200ms).
- **Invalid position:** Outline glows red. Shake left-right (2 frames).
- **Confirm:** Outline snaps to solid (`+` framed). Satisfying "thud" sound.

### 4.2 Construction Progress

**Framed stage:**
- Wood structures: `+` appears. Hammer sounds begin (rhythmic, every 2 seconds).
- Stone structures: `=` appears. Chisel sounds begin.
- Pilgrims assisting: Additional hammer sounds overlap (chorus effect).

**Complete stage:**
- Structure char changes to final (`#`).
- **Screen shake** (subtle, 100ms) — the ground settles.
- **Audio:** Final nail + structure "thud" + dust settle.
- **Visual:** Dust particles (`.`) rise and fall around structure.
- **Message:** "The {structure} is complete." (gold text, slides in from bottom).

### 4.3 Chapel Recognition

When the engine recognizes a Chapel:
1. All `+` tiles **pulse brighter** (gold -> white -> gold, 1 second).
2. **Bell toll** (distant, then closer).
3. **Screen tint** (gold, 500ms fade in, 500ms fade out).
4. Pilgrims within 10 tiles stop moving and face the Chapel for 2 seconds.
5. Message: "The space is sanctified. This is a Chapel." (gold, italic).

---

## 5. Combat Juice

### 5.1 Player Attack

**Melee:**
1. **Wind-up:** Weapon char appears briefly (1 frame).
2. **Strike:** Weapon swings toward target. White trail (`-`).
3. **Impact:** Target flashes red (100ms). Blood particle (`~`) flies.
4. **Result:** Target char changes (wounded variant). Damage number floats up (`-14`, red, fades over 1s).

**Ranged (bow):**
1. **Draw:** Bow char appears. String creak.
2. **Release:** Arrow (`>`) flies across screen (3 frames).
3. **Impact:** Target flashes. Arrow sticks for 1 second, then vanishes.
4. **Result:** Damage number. Arrow retrieval message (50% chance).

### 5.2 Hostile Attack

1. **Telegraph:** Hostile char flashes white (200ms). Growl sound.
2. **Lunge:** Hostile moves 1 tile toward player (1 frame).
3. **Impact:** Player flashes red. Screen shake (200ms). Grunt sound.
4. **Result:** Health bar drops (animated). Damage number (`-8`, red).

### 5.3 Death

**Player death:**
1. Player char flashes red 3 times (rapid).
2. Player char falls (`@` -> `x`, 3 frames).
3. **Screen desaturates** to grey over 2 seconds.
4. **Audio:** Final breath. Wind returns (louder).
5. **Screen shake** (subtle, continuous for 3 seconds).
6. Chronicle fades in (typewriter effect, 1 char per 50ms).

**Hostile death:**
1. Hostile flashes red. Death sound (yelp/hiss/clatter).
2. Hostile char falls (`w` -> `,`, 2 frames).
3. Corpse appears (`,` with red tint).
4. Loot sparkles (`!`) briefly (1 second).

### 5.4 Trap Trigger

1. **Trigger:** Snap sound. Hostile freezes (1 frame).
2. **Effect:** Pit trap — hostile falls (`W` vanishes, `^` appears). Crash sound.
3. **Result:** Damage number (`-25`, large). Hostile reappears in pit (`w`, trapped).

---

## 6. Blight Juice

### 6.1 Blight Spread

- **Normal spread:** Tile char changes (`,` -> `;` -> `"`). Purple tint fades in over 2 seconds.
- **Surge:** All blighted tiles **pulse simultaneously** (bright purple -> dark purple, 500ms). Ground crack sound. Screen border flashes purple (200ms).
- **Reach structure:** Structure char flashes purple. Decay sound (wood rot: creak. Stone: crumble).

### 6.2 Consecration

1. **Start:** Priest char glows gold (300ms).
2. **Channeling:** Gold ring expands from Priest at 1 tile per second.
3. **Tile conversion:** Each tile flashes white -> gold. Blight tiles **recoil** (shrink briefly before vanishing).
4. **Complete:** All new Holy Ground tiles pulse gold -> white -> gold (1 second). Bell toll. Ambient audio shifts (wind becomes quieter, hum begins).
5. **Message:** "The ground turns warm. The blight recoils." (gold, fades in).

### 6.3 Corruption (Player)

- **Corruption +1:** Screen edge tints purple (100ms).
- **Corruption 25+:** Subtle whisper audio begins. Screen has permanent faint purple vignette.
- **Corruption 50+:** Whispers become audible words. Screen vignette intensifies. Occasional "hallucination" (false hostile char appears for 1 frame).
- **Corruption 100:** Screen flashes purple -> black. Scream. Player char changes (`@` -> `Z`). Game over.

---

## 7. Seasonal Juice

### 7.1 Season Transitions

**Spring -> Summer:**
- Grass tiles (` ,`) brighten (grey -> green, 3 seconds).
- Bird sounds fade in.
- Message: "The thaw is complete. The forest grows."

**Summer -> Autumn:**
- Forest tiles (`^`) shift green -> orange -> brown (5 seconds).
- Leaf particles (`'`) fall from forest tiles (continuous, light).
- Message: "The leaves turn. Winter approaches."

**Autumn -> Winter:**
- **Screen flash** (white, 500ms).
- All `,` and `^` tiles become `*` (snow) over 2 seconds.
- Wind sound intensifies. All animal sounds stop.
- Message: "Winter has come." (white, bold).
- **Screen shake** (subtle, continuous — cold shiver).

**Winter -> Spring:**
- Snow tiles (`*`) melt (`,` appears underneath, 5 seconds).
- Water sounds return. Bird sounds fade in.
- Message: "The thaw begins." (green, italic).

### 7.2 Day/Night

**Dusk:**
- Screen desaturates over 10 seconds.
- Ambient sounds shift (birds -> insects -> wind).
- First star appears (`.` -> `.` with white tint, one at a time).

**Night:**
- Screen fully desaturated. Only light sources show true color.
- Fire tiles (`*`) cast orange glow on adjacent tiles (2-tile radius).
- Holy Ground (`+`) casts gold glow (1-tile radius).
- Player vision radius shrinks (animated, 2 seconds).

**Dawn:**
- Screen re-saturates over 10 seconds.
- First light: eastern edge of screen brightens first.
- Bird sounds fade in.

### 7.3 Blood Moon

1. **Warning:** Message "The Blood Moon rises." (red, bold). Screen edge tints red (5 seconds).
2. **Transition:** Screen shifts to red tint over 3 seconds. All blighted tiles pulse faster.
3. **Active:** Low drone audio begins. All ambient drops to 20%. Hostile spawn rate increases.
4. **End:** Red tint fades over 5 seconds. Drone stops. Message: "The Blood Moon sets." (grey).

---

## 8. UI Juice

### 8.1 Message Log

- **New message:** Slides in from bottom (200ms). Older messages scroll up.
- **Important message:** Gold text, stays for 3 seconds before scrolling.
- **Danger message:** Red text, screen flash (50ms).
- **Death message:** White text on black background. Stays until dismissed.

### 8.2 Stat Bars

- **Health drops:** Bar flashes red. Drops animated (not instant).
- **Faith drops:** Bar flashes purple.
- **Corruption rises:** Bar pulses purple.
- **Warmth drops:** Bar turns blue (cold) or red (hot).
- **Hunger drops:** Bar turns yellow -> red.

### 8.3 Inventory

- **Item added:** Item slides into inventory list (200ms). Brief sparkle.
- **Item removed:** Item slides out. Brief fade.
- **Corrupted item:** Red border, pulsing.
- **Equipped item:** Gold border.

### 8.4 Mini-Map

- **Player moves:** Mini-map updates in real-time (no delay).
- **New area discovered:** Mini-map tile "pops" (scales up 150% then down to 100%, 200ms).
- **Blight spreads:** Mini-map tile pulses purple.
- **Waypoint set:** `!` icon bounces once (300ms).

---

## 9. Manifestation Juice

### 9.1 Spawn Sequence

1. **Warning:** Ambient drops to 10%. Screen desaturates.
2. **Approach:** Ground shakes (subtle, continuous). Distant sound (unique per Manifestation).
3. **Arrival:** Screen flash (color unique per Manifestation). Manifestation char appears.
4. **Stabilize:** Ambient returns to 30%. Manifestation sound becomes continuous drone.

| Manifestation | Flash Color | Sound | Screen Effect |
|---------------|-------------|-------|---------------|
| **Drowned Choir** | Cyan | Underwater choral drone | Screen "wobbles" (water distortion) |
| **Hollow Stag** | White | Broken horn blast | Breath fog (cold) on screen edges |
| **Leviathan's Shadow** | Dark blue | Deep whale moan | Screen darkens (underwater) |
| **Crooked Man** | Yellow | Creaking wood, child laugh | Screen tilts 2 degrees (dizzy) |
| **Burning Eye** | Red | Sustained organ note | Screen vignette closes (tunnel vision) |

### 9.2 Defeat Sequence

1. **Final blow:** Manifestation flashes white 3 times.
2. **Death:** Manifestation char dissolves (pixels scatter outward, 1 second).
3. **Silence:** All audio stops for 2 seconds.
4. **Relief:** Ambient returns. Screen re-saturates.
5. **Loot:** Dropped items sparkle (`!`).
6. **Message:** "The {Name} is banished." (gold, large, fades in over 2 seconds).

---

## 10. Summary

| Category | Effects | Priority |
|----------|---------|----------|
| **Movement** | Footstep particles, sprint trail, collision feedback | High |
| **Gathering** | Tool wind-up, impact particles, resource pop | High |
| **Building** | Ghost placement, construction sounds, completion shake | High |
| **Combat** | Attack trails, impact flashes, damage numbers, death sequences | Critical |
| **Blight** | Spread animation, consecration ring, corruption vignette | Critical |
| **Seasons** | Color transitions, particle effects, screen tints | High |
| **Day/Night** | Desaturation, light glow, vision radius shrink | High |
| **Blood Moon** | Red tint, drone audio, blight pulse acceleration | Medium |
| **UI** | Message slides, stat bar animations, inventory sparkles | Medium |
| **Manifestations** | Unique spawn sequences, defeat dissolves | Critical |

**The rule:** If an action has a consequence, it has juice. If an action has no juice, it has no consequence.

---

Document Version 1.0
The Wilds of Canaan - The Juice: Specific Effects & Polish Document
