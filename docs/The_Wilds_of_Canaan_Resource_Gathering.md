# The Wilds of Canaan
## Resource Gathering Document

---

## 1. Philosophy

Resource gathering is not a chore between fights. It is the **rhythm of survival.** The seasons dictate what is available. The blight dictates what is safe to take. Your Vocation dictates what you see.

**Core principles:**
- **The wilderness provides, but reluctantly.** Resources are scattered, seasonal, and often tainted.
- **Tools matter.** A flint knife and a silver axe are not the same. Tools degrade and must be maintained.
- **Blight corrupts everything.** Wood from a blighted forest rots faster. Meat from a blighted deer poisons. Water from a blighted shore is undrinkable.
- **The Woodsman sees what others miss.** Tracking, foraging, and hunting are his domain.
- **Winter is a reckoning.** If you did not gather in autumn, you will starve in winter.

---

## 2. The Resource Types

### 2.1 Raw Materials

| Resource | Source | Tool Required | Base Yield | Season |
|----------|--------|---------------|------------|--------|
| **Pine Wood** | Forest (`^`) | Axe or Flint Knife | 2-4 units | All |
| **Oak Wood** | Deep forest (`^`) | Axe | 3-5 units | Spring-Summer |
| **Birch Bark** | Forest edge (`^`) | Knife | 1-2 units | Spring |
| **Flint** | Rocky shore (`.`) | Pick or Hammer | 1-2 units | All |
| **Stone** | Rocky ground (`.`) | Pick | 2-4 units | All |
| **Copper Ore** | Shallows cliffs | Pick | 1 unit | All |
| **Iron Ore** | Black Pines depths | Pick | 1 unit | All |
| **Silver Ore** | Drowned ruins | Pick | 1 unit | All |
| **Clean Water** | Clean Springs (`~`) | Waterskin | 1 unit | All |
| **Salt** | Frozen Straits (ice) | Pick | 1-3 units | Winter |
| **Clay** | The Mire (`,`) | Hands | 2-3 units | Spring-Summer |
| **Tar** | Pine forest (rare) | Bucket (crafted) | 1 unit | Summer |

### 2.2 Organic Resources

| Resource | Source | Tool Required | Base Yield | Season |
|----------|--------|---------------|------------|--------|
| **Berries** | Forest undergrowth | Hands | 1-2 food | Summer |
| **Mushrooms** | Forest floor (dark) | Hands | 1-2 food | Autumn |
| **Wild Herbs** | Forest edge | Hands | 1-2 units | Spring-Summer |
| **Pine Nuts** | Pine forest | Hands | 1 food | Autumn |
| **Fish** | Water (`~`) | Net or Spear | 1-3 food | Spring-Autumn |
| **Venison** | Deer (hostile or trap) | Bow or Spear | 4-6 food | All |
| **Wolf Meat** | Wolves | Bow or Spear | 2-3 food | All |
| **Hide** | Deer, wolves, bears | Knife | 1 unit | All |
| **Fur** | Wolves, bears | Knife | 1 unit | Winter |
| **Feathers** | Birds (ambient) | Hands | 1 unit | Spring |

### 2.3 Special / Crafted Resources

| Resource | Source | Method | Notes |
|----------|--------|--------|-------|
| **Holy Water** | Altar + Clean Water | Blessing rite | Required for consecration. Priest only. |
| **Drowned Silver** | Drowned Choir (boss) | Defeat reward | First holy metal. Unlocks Tier 2. |
| **Rare Incense** | The Mire (rare herb) | Drying rack | Fuels Reliquary. Required for late rites. |
| **Blighted Wood** | Blighted forest (`"`) | Axe | Weak. Corrupts on use. Can be purified. |
| **Blighted Meat** | Blighted beasts | Knife | Poisonous. Can be purified by Priest. |
| **Blighted Ore** | High-blight areas | Pick | Must be purified before smelting. |

---

## 3. Gathering Mechanics

### 3.1 The Basic Action

Most gathering is a single keypress on the correct tile:

```
> You stand before a pine tree.
> [G]ather  [C]hop  [L]ook  [M]ove
> g
You gather 3 pine wood. Your flint knife dulls.
```

**No mini-games.** No timing bars. The decision is where to gather, not how to click.

### 3.2 Tool Requirements & Bonuses

| Tool | Required For | Bonus | Degradation |
|------|-------------|-------|-------------|
| **Flint Knife** | Nothing (bare hands equivalent) | None | Very slow |
| **Iron Knife** | Butchering, bark, herbs | +1 yield on organic | Slow |
| **Stone Axe** | Wood | +1 wood per chop | Medium |
| **Iron Axe** | Wood, advanced wood | +2 wood, can fell oak | Medium |
| **Silver Axe** | Wood (blessed) | +2 wood, auto-purifies blighted wood | Fast |
| **Flint Pick** | Stone, ore | None | Medium |
| **Iron Pick** | Stone, ore, advanced ore | +1 ore, can mine iron | Medium |
| **Hunting Bow** | Deer, wolves (range) | First strike bonus | Slow (string) |
| **Fishing Net** | Fish | +1 fish, reusable | Slow |
| **Fishing Spear** | Fish | Single fish, retrievable | Slow |
| **Waterskin** | Water | Carry 5 units | N/A (container) |
| **Bucket** | Tar, water | Carry 3 units | N/A |

**Tool degradation:** Each use reduces condition by 1-5%. At Broken (25%), tools have a 50% chance to fail the action. At Ruined (0%), the action cannot be performed.

**The Craftsman maintains tools.** A Craftsman can repair a tool in 1 turn with 1 iron scrap or 1 wood (depending on tool type). Other Vocations must return to a forge or use a repair kit (consumed).

### 3.3 The Woodsman: Master Gatherer

The Woodsman has three gathering-specific abilities:

**Read the Woods (`R`):**
```
> r
The forest reveals itself:
  3 oak trees (southeast, 8 tiles)
  1 copper vein (south, 12 tiles)
  2 deer trails (nearby)
  Blight concentration: moderate (east)
  Clean Spring: none detected in range
```

This is not a map reveal. It is **directional intelligence.** The Woodsman knows where to go, not the exact path.

**Forager's Eye (passive):**
- Berries, mushrooms, and herbs are visible from 2 tiles away (others must be adjacent).
- Blighted resources are flagged with a red tint before gathering.
- Rare resources (tar, rare herbs) have a subtle shimmer.

**Clean Spring Detection (passive):**
- Clean Springs emit a faint sound/hint when the Woodsman is within 10 tiles.
- Other classes must stumble upon them or find them via Lost Scripture maps.

### 3.4 The Priest: Purification

The Priest does not gather efficiently. But he **cleanses** what others cannot use.

**Purify Resource (rite):**
```
> rite purify
Target: [W]ood  [M]eat  [O]re  [Wa]ter
> w
You lay hands on the blighted wood. It smokes, then steams.
The corruption is driven out. 3 blighted wood -> 3 pine wood.
Cost: 5 Faith, 1 Holy Water.
```

**What can be purified:**
- Blighted wood -> Normal wood
- Blighted meat -> Normal meat (but still low quality)
- Blighted ore -> Normal ore (required before smelting)
- Blighted water -> Normal water (but wasteful; better to find Clean Springs)

**What cannot be purified:**
- Already corrupted resources (Hell-tier blight)
- Resources from Manifestation zones
- The meat of a Wendigo (it is demon, not blighted)

### 3.5 The Craftsman: Processing

The Craftsman does not gather faster. He **extracts more** from what is gathered.

**Smelting (at Forge):**
- Copper Ore -> Copper Ingot (2 ore = 1 ingot)
- Iron Ore -> Iron Ingot (3 ore = 1 ingot)
- Silver Ore -> Silver Ingot (2 ore = 1 ingot)
- Blighted Ore must be purified first, or the ingot is corrupted (useless for holy items, dangerous for tools)

**Tanning (at Smokehouse):**
- Hide -> Leather (1 hide + 1 wood + 1 day)
- Fur -> Treated Fur (1 fur + 1 salt + 1 day)

**Drying (at Smokehouse):**
- Meat -> Jerky (2 meat + 1 wood + 1 day, no decay)
- Herbs -> Dried Herbs (1 herb + 1 day, medicinal use)
- Fish -> Dried Fish (1 fish + 1 wood + 1 day, no decay)

**Craftsman bonus:** 20% less material cost for all processing. 10% chance of bonus yield.

---

## 4. Blight & Resource Quality

### 4.1 The Blight Gradient

Resources gathered from blighted tiles carry the blight level of their source:

| Source Blight | Resource State | Effect |
|---------------|---------------|--------|
| 0-20 (Clean) | Pristine | Normal stats, normal decay |
| 21-40 (Tainted) | Tainted | -10% effectiveness. Slightly faster decay. |
| 41-60 (Blighted) | Blighted | -25% effectiveness. Corrupts on use (if organic). Must be purified. |
| 61-80 (Corrupted) | Corrupted | -50% effectiveness. Unusable for crafting without purification. Organic is poisonous. |
| 81-100 (Hell) | Cursed | Cannot be purified. Using it raises Corruption by 5. Destroy it. |

### 4.2 Visual Indicators (Client)

When a resource is on a blighted tile, the client renders it with a tint:

```
Clean tree:      ^  (dark green)
Tainted tree:    ^; (grey-green)
Blighted tree:   ^" (purple stem)
Corrupted tree:  ^= (dark purple, withered)
```

The Woodsman's Forager's Eye reveals this before gathering. Others learn by trial and error—or by watching their Corruption rise.

### 4.3 Purification Methods

| Method | Cost | Effectiveness | Speed |
|--------|------|---------------|-------|
| **Priest rite** | 5 Faith + 1 Holy Water | 100% (all tiers) | Instant |
| **Purifying fire** | 2 wood | 100% (wood only) | 1 hour |
| **Smokehouse** | 1 wood | 50% (meat only) | 1 day |
| **Clean Spring soak** | Time | 100% (ore only) | 1 day |
| **Sunlight** | Time | 25% (all) | 3 days |

---

## 5. Farming & Renewable Resources

### 5.1 The Farm Plot

Farming is only possible on **Holy Ground** (`+`). This makes the Priest essential for agriculture, or forces the Woodsman to find rare Clean Springs.

**Farm plot (blueprint):**
- Size: 2x2
- Materials: 4 wood, 2 stone
- Must be placed on Holy Ground
- Yields 4 crops per harvest

**Crops:**
| Crop | Plant | Harvest | Yield | Season |
|------|-------|---------|-------|--------|
| **Potatoes** | Spring | Autumn | 4-6 food | All seasons (stored in cellar) |
| **Turnips** | Spring | Summer | 2-3 food | Spring-Summer |
| **Beans** | Spring | Autumn | 3-4 food | Summer-Autumn |
| **Wheat** | Autumn | Summer | 2-3 food (grain) | Requires greenhouse (Tier 3) |
| **Herbs** | Spring | Summer | 2-3 herbs | Spring-Summer |

**Farm decay:** If a farm plot is on Holy Ground that reverts to blight (Priest dies, salt runs out), the crops wither in 1 day. This is a **catastrophic** event for a settlement.

### 5.2 Renewable Wild Resources

Some resources regenerate slowly:

| Resource | Regen Rate | Condition |
|----------|-----------|-----------|
| **Berries** | 7 days | Must be in forest, not blighted |
| **Mushrooms** | 14 days | Must be in dark forest, not blighted |
| **Fish** | 3 days | Must be in water, not overfished |
| **Herbs** | 10 days | Must be in forest edge, not blighted |
| **Deer** | 14 days | Must have forest cover, not hunted to extinction |
| **Wood (trees)** | 30 days | Must not be clear-cut. Stumps remain. |

**Overharvesting:** If a region's renewable resources are depleted, the game announces:
```
[MSG] The forest here is silent. Nothing grows. Nothing walks.
```
The region enters a **fallow** state for 30 days. No berries, no deer, no fish.

### 5.3 The Greenhouse (Tier 3)

The Craftsman's Greenhouse blueprint allows farming in winter:
- Size: 5x5
- Materials: 16 wood, 8 stone, 4 glass (crafted from sand/clay)
- Must be on Holy Ground
- Crops grow in winter at 50% speed
- Requires a brazier inside (fuel: 1 wood per day)

This is the **only** way to grow fresh food in winter. Without it, you survive on stored jerky, dried fish, and pine nuts.

---

## 6. Hunting

### 6.1 The Hunt

Hunting is not "press G on a deer tile." Deer are **mobile entities** on the map that flee from the player.

**Hunt flow:**
1. **Spot:** Deer are visible at 8 tiles. They graze, moving slowly.
2. **Stalk:** Move behind cover (forest tiles block their line of sight). Crouch (slower movement, less detection).
3. **Strike:** Bow shot from cover, or spear charge from adjacent tile.
4. **Retrieve:** The corpse drops 1-2 tiles from the kill. Must be butchered with a knife.

**Detection radius:**
| Action | Detection Radius |
|--------|-----------------|
| Standing in open | 8 tiles |
| Walking in open | 6 tiles |
| Walking in forest | 4 tiles |
| Crouching in forest | 2 tiles |
| Using Woodsman blind | 1 tile |

**Flee behavior:** If detected, deer flee at 2 tiles per turn toward the nearest forest edge. If cornered against water or blight, they panic (stand still for 1 turn).

### 6.2 Trap Hunting

The Woodsman and Craftsman can place **baited traps**:
- Place trap on forest tile.
- Add bait (berries or meat).
- Wait. Deer pathing is attracted to bait within 5 tiles.
- Trap triggers automatically. Deer is killed or immobilized.

**Trap types for hunting:**
| Trap | Catch Rate | Yield | Notes |
|------|-----------|-------|-------|
| **Snare** | 60% | Immobilized deer | Must finish with weapon. Reusable. |
| **Pit Trap** | 80% | Dead deer | Must retrieve from pit. One use. |
| **Baited Deadfall** | 90% | Dead deer + damaged hide | One use. Damages pelt. |

### 6.3 Dangerous Game

**Wolves** hunt in packs of 2-4. They are not prey; they are predators. They stalk the player. Hunting them is defensive, not foraging.

**Bears** are solitary, territorial, and deadly. They do not flee. They charge. A bear yields 8-10 meat and 2 hides, but killing one without traps or a group is nearly impossible.

**The Hollow Stag** is not hunted. It hunts you.

---

## 7. Fishing

### 7.1 The Catch

Fish are abstracted as tile resources, not mobile entities (unlike deer). Water tiles have a hidden fish stock.

**Methods:**
| Method | Tool | Yield | Speed | Notes |
|--------|------|-------|-------|-------|
| **Hand fishing** | None | 1 fish / 3 tries | Slow | Only in shallow water. |
| **Spear fishing** | Spear | 1 fish / try | Normal | Must be adjacent to water. |
| **Net fishing** | Net | 1-3 fish / try | Fast | Cast from shore. Reusable. Net degrades. |
| **Ice fishing** | Spear + hole | 1 fish / try | Normal | Winter only. Must cut hole in ice. |

**Blighted water:** Fish from blighted water are automatically blighted. They can be purified, but most players avoid blighted shorelines.

**Overfishing:** A water tile depleted of fish takes 7 days to restock. A settlement dependent on a single lake will eventually starve.

---

## 8. Water & Thirst

### 8.1 Water Sources

| Source | Quality | Method | Risk |
|--------|---------|--------|------|
| **Clean Spring** | Pristine | Waterskin | None. Rare. |
| **Lake (open)** | Clean | Waterskin | None. May be blighted near shore. |
| **River (flowing)** | Clean | Waterskin | None. Harder to find. |
| **Snow** | Tainted | Melt (fire + container) | Time cost. Requires fuel. |
| **Rain** | Clean | Open container | Unreliable. Seasonal. |
| **Blighted shore** | Blighted | Waterskin | Corruption +1 per drink. |
| **The Mire** | Corrupted | None | Do not drink. |

### 8.2 Thirst Mechanics

- Thirst is not a separate stat. It is folded into **Hunger** and **Health**.
- Without water for 2 days: Hunger decays 2x faster. Stamina does not regenerate.
- Without water for 4 days: Health begins to decay.
- Salt water (ocean/sea) cannot be drunk. It increases thirst.

**The Woodsman finds water.** The Priest blesses it. The Craftsman builds containers.

---

## 9. Seasonal Gathering Calendar

| Season | Available | Scarce | Danger |
|--------|-----------|--------|--------|
| **Spring** | Herbs, berries (late), fish, birch bark, clay | Wood (wet), stone (snow-covered), salt | Thaw floods. Unstable ice. |
| **Summer** | Berries, fish, deer, wood, herbs, pine nuts (late) | Salt, fur | Wolves active. Long days. |
| **Autumn** | Mushrooms, pine nuts, fish (fat), deer (fat), wood | Berries (done), herbs (done) | Last chance to stockpile. Blood Moon possible. |
| **Winter** | Ice fish, snow (melted), salt, stored food only | Everything fresh | Starvation. Freezing. Blight surges. The Long Night. |

**The autumn stockpile is survival.** A player who does not gather 30+ days of food before winter is dead. The game does not warn you. The forest warns you: berries stop growing, mushrooms wither, deer grow lean.

---

## 10. Inventory & Weight

### 10.1 Carrying Capacity

All Vocations have the same base capacity: **50 weight units.**

| Item | Weight |
|------|--------|
| Wood (1 unit) | 2 |
| Stone (1 unit) | 3 |
| Ore (1 unit) | 3 |
| Food (1 unit) | 1 |
| Meat (1 unit) | 2 |
| Hide/Fur | 2 |
| Water (1 unit) | 1 |
| Tools | 3-5 |
| Weapons | 2-4 |
| Armor | 4-8 |
| Holy Water | 1 |
| Salt | 1 |

**Overburdened:** At 50+ weight, movement costs 2 AP per tile. Cannot sprint.
**Encumbered:** At 40+ weight, Stamina regen halved.

**The Woodsman carries more efficiently.** His pack is organized. He can carry 60 weight units. This is his gathering advantage: he brings more back per trip.

### 10.2 Storage

| Container | Capacity | Notes |
|-----------|----------|-------|
| **Inventory** | 50 (60 Woodsman) | Personal carry |
| **Storage Cache** | 10 | Temporary outdoor storage. No decay protection. |
| **Storehouse** | 100 | -50% food decay. Organized. |
| **Cellar** | 50 | -75% food decay. Requires Storehouse + dig. |
| **Reliquary** | 5 | Stores holy items only. Blight-proof. |

---

## 11. Protocol Extensions for Gathering

The rendering protocol needs these additions for resource gathering:

| Command | Args | Description |
|---------|------|-------------|
| `RESOURCE` | `x y type amount blight_level` | A gatherable resource exists at this tile. |
| `DEPLETED` | `x y type` | Resource exhausted. Tile reverts to base terrain. |
| `REGEN` | `x y type days_remaining` | Resource will regenerate in N days. |
| `GATHER` | `x y type amount tool_durability` | Player gathered something. |
| `PURIFY` | `x y type success` | Priest purified a resource. |
| `HARVEST` | `x y crop_type amount` | Farm plot harvested. |
| `WITHER` | `x y` | Farm plot or resource died from blight. |

---

## 12. Summary

| Vocation | Gathering Strength | Gathering Weakness | Unique Ability |
|----------|-------------------|-------------------|----------------|
| **Woodsman** | Master | Cannot purify | Read the Woods, Forager's Eye, +10 carry weight |
| **Priest** | Poor | Slow, no tool bonuses | Purification rites, holy water creation |
| **Craftsman** | Average | No detection bonuses | Processing efficiency, tool maintenance, smelting |

| System | Purpose |
|--------|---------|
| **Blight gradient** | Forces players to choose: risk corruption for resources, or travel further for clean ones |
| **Tool degradation** | Craftsman essential for sustained gathering |
| **Seasonal calendar** | Creates urgency. Autumn stockpile or winter death |
| **Renewable regen** | Prevents infinite farming of one spot. Forces exploration |
| **Overharvesting** | Punishes exploitation. Regions can be depleted |
| **Farming (Holy Ground)** | Ties agriculture to Priest. Settlement location matters |
| **Hunting (mobile)** | Different from static gathering. Requires skill, not just time |

The forest does not want to give you its resources. You must take them, clean them, store them, and hope they last until spring.

---

Document Version 1.0
The Wilds of Canaan - Resource Gathering Document
