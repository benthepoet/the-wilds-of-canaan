# The Wilds of Canaan
## Building Granularity & Settlement Life Document

---

## 1. The Two Questions

This document answers two design questions that emerged during development:

1. **How granular is building?** Do players place individual wall segments or pre-fab structures?
2. **How do settlements feel alive?** The wilderness is empty of civilization, but the player\'s base should feel inhabited.

The answer to both is: **asymmetric by Vocation, and deliberately imperfect.**

---

## 2. Building Granularity: Three Philosophies

Each Vocation builds differently. There is no universal "build mode."

### 2.1 The Craftsman: Piece-by-Piece Fortification

The Craftsman places **individual components** on a grid, one at a time. This is the most granular building in the game.

**Placement flow:**
```
> build
Component: [W]all  [D]oor  [F]loor  [R]oof  [B]razier  [T]rap
> w
Material: [S]tone  [W]ood  [I]ron-reinforced
> s
Place wall at: > 14, 8
```

**Components:**
| Component | Char | Cost | Notes |
|-----------|------|------|-------|
| Stone Wall | `#` | 2 stone | Resists blight decay. +50% durability. |
| Wood Wall | `#` | 3 wood | Cheap. Rots in blight over time. |
| Iron Wall | `#` | 2 stone + 1 iron | Rare. Near-immune to physical damage. |
| Door | `+` | 1 wood + 1 iron | Can be locked/barred. |
| Floor | `.` | 1 wood | Required for furniture placement. |
| Roof | `^` | 2 wood | Prevents rain/snow indoors. Warmth bonus. |
| Brazier | `*` | 1 stone + 1 wood | Light source. Required for some rites. |
| Palisade | `=` | 4 wood | Outdoor wall. Slows wolves. |
| Trap (pit) | `^` | 2 wood + 1 iron | Hidden. Deals damage to hostiles. |
| Trap (silver stake) | `!` | 1 silver + 1 wood | Holy damage. Effective vs. Wendigo. |

**Construction stages:**
Nothing appears instantly. Each component has **three stages**:

1. **Planned** (`?`): You designated the spot. Resources are reserved. A ghost outline appears.
2. **Framed** (`+`): The skeleton is up. Not functional yet. Provides no protection.
3. **Complete** (`#`): Fully built. Functional.

**Who builds it?**
In single-player, the Craftsman builds everything himself (slowly). If NPC pilgrims are present, they assist construction automatically when not eating/sleeping/praying.

**Why this granularity:**
- It makes the Craftsman feel like an engineer.
- It allows organic, non-rectangular bases.
- It creates vulnerability during construction (a framed wall doesn\'t stop wolves).
- It mirrors Dwarf Fortress / Rimworld construction depth without their complexity.

---

### 2.2 The Priest: Rite-Based Sanctification

The Priest does not "build" in the carpentry sense. He **performs rites** that transform space.

**Placement flow:**
```
> rite
Rite: [C]onsecrate Ground  [E]rect Altar  [B]less Boundary
> c
Radius: [1]  [3]  [5]  [7]
> 3
Cost: 1 Holy Water, 3 Salt, -5 Faith
Perform rite at: > 16, 10
```

**Ritual structures:**
| Structure | Char | Cost | Effect |
|-----------|------|------|--------|
| Consecrated Ground | `+` | Holy Water + Salt | Blight cannot spread here. Required for all other structures. |
| Altar | `=` | 5 stone + 2 silver | Required for advanced blessings. Faith regeneration zone. |
| Brazier (Holy) | `*` | 2 wood + 1 Holy Water | Light + blight repulsion in 3-tile radius. |
| Circle of Salt | `o` | 10 salt | Temporary trap. Hostiles cannot cross. Dissolves in rain. |
| Reliquary | `!` | 5 silver + rare incense | Creates tiny Holy Ground bubble anywhere. Fuel-required. |
| Confessional | `n` | 4 wood + 1 silver | Cures Corruption for NPCs and player. |

**Key difference:** The Priest\'s structures appear **instantly** upon rite completion. There is no construction stage. The "work" is the ritual performance (a timed, vulnerable channel).

**Why this granularity:**
- It separates Priest building from Craftsman building thematically.
- It emphasizes faith over labor.
- It creates tension: the Priest is vulnerable while channeling a rite.

---

### 2.3 The Woodsman: No Building

The Woodsman does not build permanent structures. He **camps**.

**Placement flow:**
```
> camp
Camp type: [L]ean-to  [S]alt Ring  [H]unting Blind  [F]irepit
> l
Place lean-to at: > 8, 12
```

**Camp components:**
| Component | Char | Cost | Duration |
|-----------|------|------|----------|
| Lean-to | `\` | 2 wood + 1 hide | 3 days. Basic shelter. |
| Salt Ring | `o` | 3 salt | 3 days. Blight protection in 2-tile radius. |
| Hunting Blind | `^` | 3 wood + 1 hide | Permanent (until destroyed). Stealth bonus. |
| Firepit | `@` | 2 wood | 1 day. Warmth + cooking. Must be relit. |
| Bedroll | `~` | 1 hide | Permanent. Sleep anywhere. No warmth bonus. |
| Smoke Rack | `T` | 2 wood | Permanent. Cures meat (prevents blight corruption). |

**Key difference:** Woodsman camps are **temporary, portable, and disposable.** He does not construct a settlement. He moves through the wilderness leaving traces.

**Why this granularity:**
- It forces a nomadic playstyle.
- It creates tension: your camp will expire. You must keep moving.
- It contrasts with the Craftsman\'s permanence and the Priest\'s sanctity.

---

## 3. Settlement Life: The Pilgrim System

The wilderness has no villages, no natives, no traders. But the player\'s base can still feel alive through **rescued pilgrims**—survivors of previous expeditions found starving, wounded, or mad in the wilds.

### 3.1 Finding Pilgrims

Pilgrims are discovered in specific contexts:
- **In ruins:** Huddled in a collapsed chapel, eating blighted meat, near death.
- **In the forest:** Tied to a tree by their own hands, trying to escape a Wendigo they believed was following them.
- **On the ice:** Frozen, but breathing. A failed crossing.
- **In the Mire:** Standing perfectly still, staring at nothing. They will not respond until brought to Holy Ground.

**They are not quest-givers.** They do not have names (unless you give them one in The Chronicle). They do not have dialogue trees. They are **broken people** who either recover or die.

### 3.2 Pilgrim States

Each rescued pilgrim tracks:

| Stat | Function |
|------|----------|
| **Health** | Physical condition. Starvation, wounds, blight exposure. |
| **Faith** | Mental/spiritual condition. Low faith = they stop working, whisper to themselves, may wander into blight. |
| **Skill** | What they can do. Random on rescue: `labor`, `prayer`, `hunting`, `crafting`. |
| **Loyalty** | Will they flee when things get bad? Starts low. Rises with food, safety, and witnessing miracles (rites). |

### 3.3 Pilgrim Roles

Pilgrims automatically assume roles based on their skill and what the settlement needs:

| Role | Skill Required | Behavior |
|------|---------------|----------|
| **Laborer** | `labor` | Assists Craftsman construction. Carries resources. Chops wood. |
| **Acolyte** | `prayer` | Assists Priest rites (reduces Faith cost by 10%). Tends braziers. Chants at night (morale boost). |
| **Hunter** | `hunting` | Hunts small game near base. Sets traps. Cannot fight Manifestations. |
| **Smith** | `crafting` | Repairs tools. Smelts ore. Only available if a forge exists. |
| **Patient** | `none` | Too broken to work. Must be fed and healed. May recover. May die. |

**The player does not micromanage them.** There is no "assign job" screen. Pilgrims look at what exists in the settlement and contribute automatically. A `prayer` pilgrim near an altar becomes an Acolyte. A `labor` pilgrim near a construction site becomes a Laborer.

### 3.4 Pilgrim Events

Pilgrims create emergent narrative through events, not dialogue:

```
[MSG] The acolyte has stopped chanting. She stares at the blight line.
[MSG] A laborer fell through cracking ice while gathering stone. He drowned.
[MSG] The hunter brought back a corrupted deer. The meat is tainted.
[MSG] A patient woke screaming. "The Eye is open. The Eye is open." She will not sleep.
[MSG] An acolyte performed Last Rites on a dead laborer. The body did not rise.
```

**The Chronicle records them:**
```
Day 23: Found a survivor in the Black Pines. He had nailed his own hand to a tree.
Day 24: He does not speak. He carries stone. I call him Thomas.
Day 31: Thomas died in the night. The blight reached the cellar.
```

### 3.5 Pilgrim Limits

- **Max 5 pilgrims** per settlement. Space, food, and faith are limiting factors.
- **Pilgrims consume resources.** Each needs 1 food/day, a bedroll/floor to sleep on, and Holy Ground to sleep safely.
- **Pilgrims can despair.** If Faith drops to 0, they may: flee into the wilderness (lost forever), commit suicide (found hanging), or turn hostile (attacked by a "patient" who became possessed).
- **Pilgrims can be blessed.** A Priest can perform a Blessing rite on a pilgrim, permanently raising their Faith cap and granting them a title ("Blessed Thomas").

### 3.6 Why Pilgrims, Not NPCs

Pilgrims are not villagers. They are not a economy. They are **consequences of exploration** and **burdens of compassion.**

- You are not building a town. You are building a **refuge**.
- They do not make the game easier. They make it **more desperate** (more mouths to feed).
- They do not give quests. They **create problems** (despair, corruption, death).
- They make the settlement feel alive because **you watch them die**.

---

## 4. Settlement Evolution

A base progresses through stages based on population and structures:

### Stage 1: Camp (Player only)
- 1-2 temporary structures
- No pilgrims
- Surviving, not living

### Stage 2: Refuge (1-2 pilgrims)
- First permanent walls (Craftsman)
- First consecrated ground (Priest)
- A firepit that is always lit
- The Chronicle begins mentioning "we" instead of "I"

### Stage 3: Sanctuary (3-5 pilgrims)
- Chapel with altar
- Dedicated sleeping quarters
- A named cemetery (pilgrims who died are buried here)
- Acolytes chanting at night creates ambient audio/text
- The settlement has a **mood** that shifts based on recent deaths, food stores, and blight proximity

### Stage 4: Mission (Endgame)
- Cathedral-tier structure (Craftsman + Priest collaboration)
- All pilgrims have roles
- The Burning Eye is visible from the Bluffs, watching
- The final choice: sanctify, escape, or imprison

---

## 5. The Mood System

Settlements have an invisible **Mood** score (0-100) that affects pilgrim behavior and ambient text.

| Mood | Label | Effects |
|------|-------|---------|
| 80-100 | Hopeful | Pilgrims work faster. Faith regenerates. Rare positive events ("A pilgrim composed a hymn"). |
| 50-79 | Cautious | Normal operation. |
| 20-49 | Desperate | Pilgrims whisper. Construction slows. One random pilgrim loses Faith each night. |
| 0-19 | Doomed | Pilgrims may flee or suicide. Blight spreads 20% faster. Hostile spawn rate increases. The Chronicle entries become bleak. |

**Mood factors:**
- Recent deaths (-20 each)
- Food shortage (-10 per day starving)
- Blight encroaching on Holy Ground (-15)
- Successful rite/Manifestation defeat (+15)
- New pilgrim rescued (+10)
- All pilgrims blessed (+10)
- Blood Moon (-30)

**Ambient text examples by mood:**

*Hopeful:*
```
[MSG] The acolytes are singing. Their voices carry across the lake.
[MSG] A laborer found wild berries. Small blessings.
```

*Desperate:*
```
[MSG] The chanting has stopped. The braziers are low.
[MSG] Someone is crying in the longhouse. No one comforts them.
```

*Doomed:*
```
[MSG] The salt line is breached. They know it. They do not speak.
[MSG] A pilgrim walked into the blight last night. We did not stop her.
```

---

## 6. Building + Pilgrims: Interaction Examples

**Example 1: The Craftsman builds a wall, a pilgrim helps.**
```
> build wall stone at 14, 8
[MSG] You mark the foundation. Thomas the Laborer brings stone.
[MSG] The wall is framed. (+)
[MSG] Thomas hammers through the night. The wall stands. (#)
```

**Example 2: The Priest consecrates ground, an acolyte assists.**
```
> rite consecrate radius 3 at 16, 10
[MSG] You begin the Rite. The acolyte kneels beside you.
[MSG] Her voice joins yours. The Faith cost is reduced.
[MSG] The ground turns gold. The blight recoils.
```

**Example 3: A Woodsman returns to find his camp has been expanded.**
```
[MSG] You return from the Black Pines. The Craftsman has built a palisade.
[MSG] Two pilgrims huddle by the fire. They look at you like salvation.
```

**Example 4: A pilgrim dies during construction.**
```
[MSG] Thomas was framing the chapel roof when the blight surged.
[MSG] He fell. The wood fell with him. He is buried beneath the altar.
[MSG] The chapel is incomplete. His blood marks the stone.
```

---

## 7. Technical Implications (Web Prototype)

### 7.1 Protocol Extensions for Building

The protocol from the Architecture Document needs three new commands:

| Command | Description |
|---------|-------------|
| `GHOST <x> <y> <tile> <fg> <bg>` | Planned construction (semi-transparent/outline) |
| `STAGE <x> <y> <stage>` | Construction stage changed (0=planned, 1=framed, 2=complete) |
| `PILGRIM <id> <x> <y> <role> <state>` | Pilgrim position and status |
| `MOOD <value>` | Settlement mood update |

### 7.2 Client Rendering: Ghosts

Planned but unbuilt structures render at 30% opacity or as outlines:

```javascript
// Ghost wall (planned)
ctx.globalAlpha = 0.3;
ctx.fillStyle = colorMap.brown;
ctx.fillText('#', x * CELL_W, y * CELL_H);
ctx.globalAlpha = 1.0;
```

### 7.3 Client Rendering: Pilgrims

Pilgrims use lowercase letters to distinguish from player (`@`):

| Role | Char | Color |
|------|------|-------|
| Laborer | `t` | Brown |
| Acolyte | `a` | Gold |
| Hunter | `h` | Dark green |
| Smith | `s` | Grey |
| Patient | `p` | White (pale) |

They move on their own schedule (simple AI: work during day, sleep at night, flee from hostiles).

---

## 8. Summary

| Vocation | Building Style | Granularity | Permanence |
|----------|---------------|-------------|------------|
| **Craftsman** | Piece-by-piece components | High (individual walls/floors) | Permanent (stone) |
| **Priest** | Rite-based sanctification | Medium (radius-based) | Permanent (holy) |
| **Woodsman** | Temporary camps | Low (pre-fab lean-tos) | Temporary (expires) |

| Feature | Purpose |
|---------|---------|
| **Pilgrims** | Make settlement alive without breaking isolation tone |
| **Construction stages** | Create vulnerability and visual progress |
| **Mood system** | Emergent narrative through ambient text |
| **Automatic roles** | No micromanagement; pilgrims adapt to your base |
| **The Chronicle** | Records pilgrim lives and deaths as legacy |

The settlement is not a village. It is a **refuge that is slowly dying** unless you push back the dark. The pilgrims are not citizens. They are **witnesses**.

---

Document Version 1.0
The Wilds of Canaan - Building Granularity & Settlement Life Document

---

## 9. Structure Roster

This section catalogs all named structures in the game, their requirements, and how they are created. The method differs by Vocation: the Craftsman uses **blueprints** (ghost outlines filled piece by piece), the Priest uses **rites** (instant sanctification), and the Woodsman has no named structures.

### 9.1 Craftsman: Blueprint-Based Structures

The Craftsman learns **blueprints** from Lost Scriptures or by reaching new crafting tiers. A blueprint is a named recipe with a fixed footprint and material list. Placing a blueprint creates a **ghost outline** on the map. The player and any Laborer pilgrims then fill it in component by component.

**Blueprints vs. Freeform:**
- **Blueprint structures** grant structural bonuses (warmth, storage, defense) that freeform construction does not.
- **Freeform** (individual walls without a blueprint) is always available for improvisation, but lacks bonuses.
- A blueprint can be **rotated** (90-degree increments) before placement.
- A blueprint can be **canceled** before completion, returning 50% of reserved materials.

#### Tier 1: Stranded (Available from start)

| Blueprint | Size | Materials | Bonus | Char |
|-----------|------|-----------|-------|------|
| **Lean-To** | 2x2 | 4 wood, 2 hide | Basic shelter. Sleep 1. No warmth bonus. | `\` |
| **Firepit** | 1x1 | 2 wood | Cooking. Warmth in 2-tile radius. Expires in 1 day. | `@` |
| **Storage Cache** | 1x1 | 2 wood | Stores 10 items. No decay protection. | `C` |

#### Tier 2: Sanctuary (Unlocked after first chapel consecrated)

| Blueprint | Size | Materials | Bonus | Char |
|-----------|------|-----------|-------|------|
| **Longhouse** | 6x4 | 20 wood, 8 stone, 4 hide, 2 braziers | Sleep 4 pilgrims. +20% warmth recovery. | `H` |
| **Forge** | 4x4 | 12 stone, 4 iron, 1 anvil (crafted) | Smelt ore. Repair gear. Required for iron/steel tools. | `F` |
| **Storehouse** | 4x4 | 16 wood, 4 stone | Food decay -50%. Stores 100 items. | `S` |
| **Palisade Gate** | 3x1 | 6 wood | Defensive entrance. Can be barred from inside. | `G` |
| **Smokehouse** | 3x2 | 8 wood, 2 stone | Cures meat (prevents blight corruption). | `M` |

#### Tier 3: Fortified (Unlocked after defeating The Hollow Stag)

| Blueprint | Size | Materials | Bonus | Char |
|-----------|------|-----------|-------|------|
| **Watchtower** | 3x3 | 8 stone, 4 wood, 1 silver bell | Reveals 20-tile radius. Early warning for blight surges. | `T` |
| **Infirmary** | 4x4 | 12 wood, 4 stone, 2 beds (crafted) | Pilgrim healing +100%. Corruption recovery for resting patients. | `I` |
| **Dock** | 3x2 | 10 wood (over water) | Boat building. Fishing. Lake travel to new regions. | `D` |
| **Reinforced Wall** | 1x1 | 2 stone, 1 iron | +200% durability vs. freeform stone wall. Blight-immune. | `#` |
| **Greenhouse** | 5x5 | 16 wood, 8 stone, 4 glass (crafted) | Grow crops in winter. Requires Holy Ground beneath. | `O` |

#### Tier 4: Redemption (Unlocked after defeating The Crooked Man)

| Blueprint | Size | Materials | Bonus | Char |
|-----------|------|-----------|-------|------|
| **Bastion** | 8x8 | 40 stone, 10 iron, 4 silver, 2 mechanical wards | Ultimate defense. Blight cannot enter. Hostiles cannot breach walls. | `B` |
| **Great Forge** | 6x6 | 20 stone, 8 iron, 2 anvils, 1 bellows (crafted) | Steel crafting. Blessed weapon forging. | `f` |
| **Shipyard** | 6x4 | 24 wood, 8 iron, 4 tar (crafted) | Build the escape ship (Woodsman ending). | `Y` |
| **Vault** | 4x4 | 20 stone, 6 silver, 2 iron | Seals the Burning Eye (Craftsman ending). Requires all 5 Manifestations defeated. | `V` |

#### Tier 5: The Mission (Unlocked after defeating The Burning Eye - or required to attempt it)

| Blueprint | Size | Materials | Bonus | Char |
|-----------|------|-----------|-------|------|
| **Cathedral** | 10x10 | 60 stone, 20 silver, 10 iron, 4 stained glass (crafted), 1 great bell (crafted) | Required for Priest ending. Consecrates entire region. Faith regeneration for all pilgrims. | `C` |

**Note:** The Cathedral requires both Vocations. The Craftsman builds the shell; the Priest performs the Grand Consecration rite inside it. Solo players must learn cross-class abilities or attempt the ending without the full bonus.

---

### 9.2 Priest: Rite-Based Structures

The Priest does not use blueprints. He performs **rites** that create structures instantly. The "cost" is the ritual itself: a vulnerable, timed channel that consumes resources and Faith.

**Rite mechanics:**
- The Priest selects a rite and a target location.
- He channels for N seconds (vulnerable to interruption by hostiles).
- Upon completion, the structure appears instantly.
- If interrupted, resources are lost, Faith is drained, and the Priest gains Corruption.

#### Basic Rites (Available from start)

| Rite | Structure | Cost | Effect | Char |
|------|-----------|------|--------|------|
| **Consecrate Ground** | Holy Ground | 1 Holy Water, 3 Salt, -5 Faith | Blight cannot spread here. Required for all other Priest structures. | `+` |
| **Bless Flame** | Holy Brazier | 1 Holy Water, 2 Wood, -3 Faith | Light source. Blight repulsion in 3-tile radius. | `*` |
| **Lay Warding** | Circle of Salt | 10 Salt, -2 Faith | Temporary barrier. Hostiles cannot cross. Dissolves in rain/snow. | `o` |

#### Advanced Rites (Unlocked after first Manifestation defeated)

| Rite | Structure | Cost | Effect | Char |
|------|-----------|------|--------|------|
| **Erect Altar** | Altar | 5 Stone, 2 Silver, -10 Faith | Required for advanced blessings. Faith regeneration zone (5-tile radius). | `=` |
| **Establish Shrine** | Reliquary | 5 Silver, 1 Rare Incense, -15 Faith | Creates tiny Holy Ground bubble (3-tile radius) anywhere. Requires daily incense refuel. | `!` |
| **Consecrate Space** | Confessional | 4 Wood, 1 Silver, -8 Faith | Cures Corruption for pilgrims and player. One use per day per pilgrim. | `n` |
| **Raise Banner** | Blessed Standard | 2 Wood, 1 Silver, 1 Holy Water, -10 Faith | +10 Mood to all pilgrims in 10-tile radius. Hostiles avoid the area. | `P` |

#### Grand Rites (Unlocked after Tier 3)

| Rite | Structure | Cost | Effect | Char |
|------|-----------|------|--------|------|
| **Grand Consecration** | Cathedral Sanctum | 20 Holy Water, 10 Salt, 5 Silver, -50 Faith | Required to activate a Cathedral. Consecrates entire region permanently. | `+` (overlay) |
| **Seal the Eye** | Binding Circle | 20 Silver, 10 Iron, -30 Faith | Required for Craftsman ending. Traps the Burning Eye in place for the Vault sealing. | `0` |

---

### 9.3 The Chapel: A Soft Blueprint

The **Chapel** is unique: it is not a blueprint or a rite. It is **recognized** by the game when specific conditions are met.

**Chapel recognition rules:**
1. An enclosed space of at least 5x5 tiles.
2. Walls (`#`) on all sides, with one door (`+`).
3. An Altar (`=`) placed inside.
4. The floor is entirely Holy Ground (`+`).
5. At least one Holy Brazier (`*`) inside.

When recognized, the game announces:
```
[MSG] The space is sanctified. This is a Chapel.
[MSG] Pilgrims may pray here. Faith regenerates for all within.
```

**Bonuses granted:**
- +20% Faith regeneration for all inside.
- Pilgrims with `prayer` skill automatically become Acolytes.
- Required for Tier 2 blueprint unlocks (the Craftsman is "inspired" by the sanctified space).

**The Chapel is the first structure that requires both Vocations.** The Craftsman builds the shell; the Priest sanctifies it. Solo players must either:
- Play Craftsman and learn the Bishop's Fragment (limited consecration), or
- Play Priest and learn basic construction from Brother Smith's Codex (slow, expensive).

---

### 9.4 Woodsman: No Named Structures

The Woodsman has no blueprints and no rites. His "structures" are temporary camps that expire. This is intentional: the Woodsman is a nomad, not a settler.

| Camp | Duration | Effect | Char |
|------|----------|--------|------|
| **Lean-To** | 3 days | Basic shelter. Sleep 1. | `\` |
| **Salt Ring** | 3 days | Blight protection (2-tile radius). | `o` |
| **Hunting Blind** | Permanent (until destroyed) | Stealth bonus. Pilgrims cannot use. | `^` |
| **Firepit** | 1 day | Warmth + cooking. Must be relit daily. | `@` |
| **Smoke Rack** | Permanent | Cures meat. No blight protection. | `T` |
| **Reliquary** (via Lost Scripture) | Fuel-required | Tiny Holy Ground bubble. The Woodsman's only concession to permanence. | `!` |

---

### 9.5 Blueprint Ghost Rendering (Web Client)

When a Craftsman selects a blueprint, the client renders a **ghost outline** before construction begins:

```javascript
// Ghost outline rendering
function drawGhost(x, y, w, h, valid) {
    ctx.strokeStyle = valid ? '#00ff00' : '#ff0000';  // Green if placeable, red if blocked
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);  // Dashed line
    ctx.strokeRect(x * CELL_W, y * CELL_H, w * CELL_W, h * CELL_H);
    ctx.setLineDash([]);

    // Material checklist overlay
    ctx.fillStyle = valid ? '#ccffcc' : '#ffcccc';
    ctx.fillRect((x + w) * CELL_W + 5, y * CELL_H, 120, 80);
    ctx.fillStyle = '#000';
    ctx.font = '10px monospace';
    ctx.fillText('Longhouse', (x + w) * CELL_W + 8, y * CELL_H + 12);
    ctx.fillText('Wood: 20/20', (x + w) * CELL_W + 8, y * CELL_H + 24);
    ctx.fillText('Stone: 6/8', (x + w) * CELL_W + 8, y * CELL_H + 36);
    ctx.fillText('Hide: 4/4', (x + w) * CELL_W + 8, y * CELL_H + 48);
}
```

**Ghost states:**
- **Valid (green):** All required tiles are empty and on appropriate terrain.
- **Invalid (red):** Blocked by water, blight, existing structure, or wrong terrain.
- **Partially valid (yellow):** Some materials are missing from inventory.

**Placement flow in UI:**
```
+------------------------------------------------------------------+
| > build                                                          |
| Blueprint: [L]onghouse  [F]orge  [S]torehouse  [P]alisade...    |
| > l                                                              |
| Rotate: [R]otate  [C]ancel  [Enter]Confirm                      |
|                                                                  |
|    [Ghost outline rendered on map with material checklist]       |
|                                                                  |
| Materials: Wood 20/20  Stone 6/8  Hide 4/4  Brazier 2/2         |
| Status: NEEDS MORE STONE                                         |
+------------------------------------------------------------------+
```

---

### 9.6 Structure Interaction Matrix

| Structure | Craftsman | Priest | Woodsman | Pilgrims |
|-----------|-----------|--------|----------|----------|
| Longhouse | Builds | Blesses (optional) | Sleeps in | Sleeps in |
| Forge | Builds & uses | Cannot use | Cannot use | Smiths work here |
| Storehouse | Builds | Cannot use | Loots (temporary) | Laborers stock |
| Chapel | Builds shell | Sanctifies | Cannot use | Acolytes pray |
| Cathedral | Builds shell | Grand Consecration | Cannot use | All pray |
| Dock | Builds | Blesses (optional) | Uses heavily | Fishermen work |
| Watchtower | Builds | Blesses (optional) | Uses heavily | Scouts work |
| Infirmary | Builds | Blesses (optional) | Cannot use | Patients rest |
| Altar | Cannot build | Creates | Cannot use | Acolytes assist |
| Reliquary | Cannot build | Creates | Can learn (limited) | Cannot use |
| Lean-To | Can build (freeform) | Cannot use | Creates | Cannot use |
| Salt Ring | Cannot build | Creates | Creates | Cannot use |

---

### 9.7 Technical Implications (Protocol)

The protocol needs two new commands for blueprints:

| Command | Args | Description |
|---------|------|-------------|
| `BLUEPRINT` | `name x y rotation` | Player selected a blueprint and placed the ghost. |
| `CONFIRM` | `name x y` | Player confirmed placement. Ghost becomes planned construction. |
| `CANCEL` | `name x y` | Player canceled. Ghost removed. |
| `COMPLETE` | `name x y` | All components built. Structure is active. |

And one for Chapel recognition:

| Command | Args | Description |
|---------|------|-------------|
| `RECOGNIZE` | `chapel x y` | Game engine detected a Chapel at this location. |

---

## 10. Summary

| Vocation | Building Method | Named Structures | Key Feature |
|----------|----------------|------------------|-------------|
| **Craftsman** | Blueprints (ghost -> planned -> framed -> complete) | 15+ named structures | Structural bonuses, progression via unlocks |
| **Priest** | Rites (instant, vulnerable channel) | 8+ named structures | No construction stage, but vulnerable during rite |
| **Woodsman** | Temporary camps | 0 named structures | All expire, no permanence |

| Special Case | Description |
|--------------|-------------|
| **Chapel** | Soft blueprint: recognized when conditions met, not placed as object |
| **Cathedral** | Ultimate collaboration: Craftsman builds, Priest consecrates |
| **Ghost rendering** | Client shows dashed outline + material checklist before placement |

The settlement starts as a single firepit and grows into a compound of specialized buildings, each with a purpose and a story. The Craftsman's Forge is where silver weapons are born. The Priest's Chapel is where pilgrims are saved. The Watchtower is where someone first saw the Hollow Stag approaching. The buildings are not just mechanics. They are **memory**.

---

Document Version 1.1
The Wilds of Canaan - Building Granularity & Settlement Life Document
