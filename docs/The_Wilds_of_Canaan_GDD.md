# The Wilds of Canaan
## Game Design Document

---

### 1. Overview

**Genre:** ASCII Survival-Crafter / Frontier Horror  
**Inspiration:** *Valheim* (crafting/building loop), *The Witch* (2015) (folk horror tone), 17th-century Great Lakes frontier  
**Platform:** Terminal / ASCII engine  
**Players:** Single-player only  
**Core Fantasy:** You are a survivor of a doomed expedition to a cursed land. The forests are hungry, the lakes remember the dead, and the night brings things that wear the shapes of men. Build sanctuaries, consecrate the ground beneath them, and survive the Long Night.

---

### 2. The Title

**The Wilds of Canaan**

Canaan is the Biblical Promised Land—the destination of Exodus, the land "flowing with milk and honey," but also a territory described as devouring its own inhabitants, filled with "giants in the earth," and requiring divine mandate to enter. It carries exactly the theological weight intended: a place of promised bounty that is, in reality, hostile, cursed, and spiritually dangerous.

The irony is the hook. In Scripture, Canaan was already inhabited by established nations; the drama was displacement and judgment. In this game, the land is *empty of humanity* but saturated with supernatural evil. The player isn't a conqueror displacing people—they're an inheritor entering a land that God promised but the Devil claimed. The title suggests: *This was supposed to be holy ground. Something went wrong.*

"Wilds" instead of "Wilderness" is intentional. "Wilderness" sounds biblical and dignified (40 years in the wilderness). "Wilds" sounds feral, untamed, and slightly archaic—like a 17th-century chronicler's word. It evokes maps with blank spaces marked *Here Be Dragons*.

**Tone:** It reads like a document. A Puritan's journal entry. A Jesuit's field report. A lost expedition's log. That documentary quality grounds the ASCII aesthetic—this is a game that looks like it could be played on a terminal in a monastery basement.

---

### 3. Core Design Pillars

1. **The Priest is terrain.** Not just support—he changes where the game can be played.
2. **Darkness is a substance.** The Blight is a literal environmental threat that spreads, corrupts, and kills.
3. **Asymmetric Pilgrimage.** Three distinct Vocations create three genuinely different campaigns.
4. **Survival is worship.** Building, farming, and enduring are acts of faith. The game rewards order, not conquest.
5. **The evil is literal.** The enemy is Hell, not people. You are a refugee, not a conqueror.

---

### 4. The World: Geography Without History

Fictionalized Great Lakes geography with zero real-world cultures. No villages. No other humans. Only ruins of previous expeditions, abandoned chapels, and the things that killed them.

| Region | Description | Threat Level |
|--------|-------------|--------------|
| **The Shallows** | Rocky coast, shipwreck debris. Starting area. | Mild blight |
| **The Black Pines** | Dense forest. Wendigo-spirits, corrupted game. | Moderate blight |
| **The Frozen Straits** | Lake ice and open water. Drowned dead, leviathan shadows. | High blight on ice |
| **The Mire** | Swampy lowlands. Fungal corruption, despair demons. | Unstable ground, high blight |
| **The Bluffs** | High ground, wind-scoured. Final tier. | Extreme blight |

**Procedural generation:** Great Lakes-style peninsulas, large water bodies, dense interior forests.

**Seed-based uniqueness:** Each playthrough generates from a numeric seed that determines:
- Great Lakes geometry (peninsula shapes, water bodies, forest density)
- Resource placement (copper veins, oak groves, clay deposits, Clean Springs)
- Blight seed points (where corruption starts spreading from)
- Lost Scripture locations (which ruins hold which fragments)
- Pilgrim spawn points (where survivors are found)
- Manifestation arena layout (shoreline geometry for the Drowned Choir, etc.)

The seed does NOT change: the 5 region types always exist, winter always arrives on Day 30, tier unlock order is fixed, and fundamental scarcity ratios are consistent. Two different seeds create different logistics puzzles within the same design language.

---

### 5. The Blight & Consecration System

**Environmental Blight** is a numerical value (0-100) on every tile. High blight means:
- Hostile spawns (shadows, corrupted beasts, demons)
- Building decay
- Agriculture failure
- Personal **Corruption** gain for players standing in it
- Visual: Purple/black fog (`"` or `~` in ASCII) that physically obscures vision

**Consecration:** The Priest can perform a rite to permanently lower blight in a radius, creating **Holy Ground**.
- Holy Ground is the *only* place advanced structures can be built.
- Crops grow only on Holy Ground.
- Beds/sleeping only restore sanity on Holy Ground.
- Consecration costs: Holy Water (Priest crafts from clean water + prayer), Salt (rare resource), and a small permanent Faith cost.

**This makes the Priest a terraformer.** In a multiplayer context, the Woodsman finds resources, the Craftsman builds structures, and the Priest makes the *land* playable. In single-player, each Vocation solves this problem differently.

---

### 6. The Three Vocations (Classes)

At character creation, you choose **one** Vocation. This defines your entire early game. All basic survival actions—chopping wood, building shelters, cooking food—are available to everyone. But advanced systems are gated by Vocation.

#### **Priest** — *The Voice and the Ward*
- **Consecration:** Only class that can create Holy Ground natively. Radius and speed scale with gear.
- **Healing:** Restores Health and **Faith** (sanity stat) to self. Cures personal Corruption.
- **Exorcism:** Can "Banish" in an AoE—pushes back blight temporarily, stuns demons, forces possessing spirits out of animals.
- **Blessing:** Blesses water (Holy Water), weapons (silver → blessed silver), and crops.
- **Unique Ability — *Last Rites*:** If you die, a prepared Last Rites kit prevents you from rising as a hostile Revenant (in Chronicle legacy).
- **Solo Identity:** Sanctuary Builder
- **The Blight Problem:** *Solved.* You consecrate naturally.
- **The Manifestation Problem:** *Hard.* You fight like a candle in a windstorm—fragile, dependent on wards and timing.

#### **Woodsman** — *The Eyes and the Spear*
- **Movement:** 25% faster in forest. Ignores movement penalty from shallow snow.
- **Tracking:** Reveals enemy patrol paths, blight concentration, and hidden corrupted game.
- **Combat:** Bonus to bows, spears, and traps. Can craft hunting blinds and lean-tos.
- **Unique Ability — *Read the Woods*:** Expends a small offering (herbs/salt) to reveal a large area's blight level and enemy positions on the map.
- **Solo Identity:** Nomadic Hunter
- **The Blight Problem:** *Unsolved.* You cannot consecrate. Must find rare "Clean Ground" or use consumable wards.
- **The Manifestation Problem:** *Solved.* You track, trap, and kill efficiently.

#### **Craftsman** — *The Hands and the Wall*
- **Building:** Can build all advanced structures (smithy, chapel, dock, palisade). Structures have +50% durability and +30% blight resistance.
- **Repair:** Can repair tools, weapons, and holy items. Silver weapons degrade fast and require maintenance.
- **Crafting:** Reduced material costs for tools. Only class that can process ore into metal efficiently.
- **Unique Ability — *Fortify*:** Temporarily makes a structure immune to blight and enemy damage for one night. Costs rare materials.
- **Solo Identity:** Fortification Engineer
- **The Blight Problem:** *Managed.* You can't purify land, but you build structures that resist blight longer.
- **The Manifestation Problem:** *Neutral.* You build siege engines and silver traps, but need prepared ground.

---

### 7. How Each Vocation Solves Base-Building

**Priest:** Consecrates normally. Base-building is straightforward. Combat and resource gathering are the bottlenecks. You rely on traps, defensive wards, and luring enemies into Holy Ground rather than fighting fair.

**Woodsman:** Cannot consecrate. Must instead:
- Find **Clean Springs**—rare, small patches of naturally low-blight land (1-2% of the map).
- Build **temporary** camps using portable warding salt. These last 3-5 days before the salt burns out.
- Eventually craft a **Reliquary** (late-game) that creates a tiny bubble of Holy Ground, but requires constant refueling with rare incense.
- **Playstyle:** Nomadic. You have 3-4 satellite camps and rotate between them. You are the hunter, not the farmer.

**Craftsman:** Cannot consecrate. Instead:
- Builds with **Blight-Resistant Materials**. Stone and tar resist corruption; wood rots. Your base is a fortress of stone and silver nails.
- Crafts **Mechanical Wards**—clockwork prayer wheels, wind-chime detectors, salt-sprinkler turrets. These don't purify the land; they *push back* the blight in a radius mechanically.
- **Playstyle:** Turtle. You build incredibly dense, heavily fortified compounds. You don't expand; you dig in.

---

### 8. Cross-Class Learning (Lost Scriptures)

You are alone, but you are not *hopelessly* locked. Throughout the world, you find **Lost Scriptures**—journals, psalters, and field manuals left by dead members of other expeditions. These grant limited access to other Vocations.

**Examples:**
- **The Woodsman's Psalm** (found in hunting blinds): Learn basic *Read the Woods*. Track enemy patrols. Small radius.
- **Brother Smith's Codex** (found in ruined forges): Learn basic repair. Maintain silver weapons, but not *Fortify*.
- **The Bishop's Fragment** (found in abandoned chapels): Expand consecration radius by 10%, or learn to bless water (slowly).

**Rules:**
- You can learn up to **two** secondary abilities total.
- They operate at 40% efficiency compared to a native Vocation.
- They cannot be leveled. A Woodsman who learns consecration will always be a bad Priest.

This means a late-game Woodsman *can* establish a small sanctuary, but it's agonizingly slow and resource-intensive. He'll never build a cathedral. A late-game Priest *can* learn to track, but he'll never stalk a Wendigo across three biomes. The asymmetry holds, but the edge cases are survivable.

---

### 9. Survival Stats

| Stat | Function | Recovery |
|------|----------|----------|
| **Health** | Standard vitality | Rest, healing salves, Priest prayer |
| **Hunger** | Food requirement | Food |
| **Warmth** | Critical in winter. Below threshold, stats degrade, then health | Fire, clothing, shelter quality |
| **Faith** | Sanity/morale. Drops in blight, darkness, when witnessing horrors | Holy Ground, prayer, reading found scripture, sacraments |
| **Corruption** | Personal blight. Gains from cursed wounds, blighted food, dark areas | Priest confession, purifying fire, rare herbs |

**Blighted Food:** You can eat corrupted meat from blighted animals. It fills hunger but gives Corruption. The Priest can purify it. This creates a risk/reward loop when starving in winter.

---

### 10. Crafting Tiers

1. **Stranded (Flint & Bark):** Basic axe, lean-to, campfire, spear. Survive the first night.
2. **Sanctuary (Copper & Pine):** Chapel (unlocks consecration for Priests), forge, palisade, longhouse.
3. **Fortified (Iron & Oak):** Stone walls, silver weapons, dock/boat, greenhouse. Requires defeating Hollow Stag.
4. **Redemption (Steel & Blessed Relics):** Cathedral, exorcism gear, holy armor, advanced wards. Endgame.

**Key twist:** Metal tools require clean ore. Blighted ore (found in high-blight areas) must be purified by the Priest before the Craftsman can smelt it.

---

### 11. The Manifestations (Bosses)

You don't "unlock biomes." You **push back the darkness** enough to survive deeper regions. Each major area has a **Manifestation**—a regional demon that must be ritually defeated to access the next tier of resources.

| Tier | Manifestation | Location | Requirement | Reward |
|------|--------------|----------|-------------|--------|
| **1. Shipwrecked** | *The Drowned Choir* | Coastal shallows | Build first chapel, craft holy water | Unlock: Safe boat travel, "Drowned Silver" (first holy metal), tier 2 tools |
| **2. The Long Dark** | *The Hollow Stag* | Deep woods | Survive first Blood Moon event | Unlock: True Sight (see hidden blight), cold-weather gear, tier 3 building (stone) |
| **3. Frozen Faith** | *The Leviathan's Shadow* | Lake ice | Cross open ice, maintain 3 consecrated braziers | Unlock: Advanced forging (iron/steel), lake agriculture, tier 4 weapons |
| **4. Despair** | *The Crooked Man* | The Mire | Enter with >80% personal Faith | Unlock: Blessed agriculture, exorcism gear, cathedral-tier building |
| **5. The Last Night** | *The Burning Eye* | The Bluffs | All previous rites completed | Endgame: Final confrontation or escape |

**Solo Boss Strategy Examples:**

**The Drowned Choir (Tier 1):**
- *Priest:* Build a chapel on the shore. Lure the Choir to your consecrated ground. Defensive siege—keep braziers lit while performing the 3-minute Banishment rite.
- *Woodsman:* Track the Choir's patrol route across the shallows. Place traps during the day. At night, kite it into shallow water traps and silver-tipped stakes.
- *Craftsman:* Build a reinforced dock with a mounted scissor-trap. The Choir must physically crash into your architecture to be damaged.

**The Hollow Stag (Tier 2):**
- *Priest:* Prepare a *Circle of Salt* in a clearing and trap it inside, then perform an exorcism while it rages against the boundary.
- *Woodsman:* Outrun it. The fight is a chase through the forest, using tracking to predict ambushes and shooting between trees.
- *Craftsman:* Build a palisade with a single gate. Bait it into charging the gate, where a counter-weighted silver spike waits.

Each Manifestation has **three valid solutions**, but only one is "natural" to your Vocation. The others are possible but require preparation that feels like solving a puzzle with the wrong-shaped piece.

---

### 12. The Bestiary

| Creature | Symbol | Behavior | Weakness |
|----------|--------|----------|----------|
| Corrupted Wolf | `w` | Packs, stalks at edge of vision | Fire, silver |
| Wendigo | `W` | Mimics human screams, lures you into blight | Holy Ground, consecrated weapons |
| Drowned | `z` | Water spawn, drag you under | Blessed boats, Priest banishment |
| Shadow | `s` | Only visible in peripheral light (ASCII color flicker) | Light sources, exorcism |
| The Hollow Stag | `D` | Boss. Charges, summons blizzard, corrupts ground | Silver spears, rites performed on Holy Ground |
| Revenant | `Z` | Former player/NPC. Uses their gear against you. | Last Rites (Priest), fire |

---

### 13. ASCII Aesthetic

- **Color palette:** Gold/white for holy/consecrated. Purple/black for blight. Cyan for ice/water. Red for hostiles. Green for clean forest.
- **Fog of war:** Blight physically obscures the map with `"` or `~` characters.
- **UI:** Side panel showing Faith, Warmth, Hunger, Blight Exposure, and current season.
- **Map:** Procedural. Great Lakes-style peninsulas, large water bodies, dense interior forests.

---

### 14. Permadeath & The Chronicle

**Ironman mode by default** (one save file, deleted on death), with an optional "Pilgrim" mode for learning.

**The Chronicle:** Every in-game day, your character automatically writes a journal entry based on what you did.

> *"Day 14. The blight has reached the potato cellar. I can hear the Drowned Choir at the edge of the ice. I have enough salt for one more ward. If I do not find Clean Ground by the new moon, I will have to attempt the Rite unprepared."*

When you die, the journal is preserved. New characters can find the **Chronicle of [Name]** in the world, granting:
- A partial map of where that character explored.
- One random Lost Scripture they had learned.
- A warning: *"Do not go north of the Mire. The Crooked Man is not a legend."*

This creates legacy without roguelike meta-progression. You don't get stronger on respawn—you get *wiser*.

---

### 15. The Endgame: Three Paths to Redemption

The final Manifestation, *The Burning Eye* on the Bluffs, is the same for all. But your Vocation determines what "victory" looks like:

| Vocation | Ending |
|----------|--------|
| **Priest** | *The Sanctuary.* You consecrate the Bluffs entirely. The land is healed. You establish a permanent monastery. The Wilds of Canaan become holy ground. |
| **Woodsman** | *The Passage.* You don't defeat the Eye—you *escape* it. You build a ship capable of crossing the northern straits, leaving the cursed land behind. A new Canaan awaits. |
| **Craftsman** | *The Bastion.* You don't heal the land; you *imprison* the evil. You construct a vault of stone and silver, sealing the Eye beneath a cathedral of engineering. The Wilds remain cursed, but contained. |

This means three distinct endings, encouraging three full playthroughs.

---

### 16. Development Roadmap

| Phase | Goal | Timeline |
|-------|------|----------|
| **Prototype** | ASCII map, one Vocation (Priest), hunger/cold, basic building, wolves, day/night, Blight/Consecration loop | 2-3 months |
| **Alpha** | All 3 Vocations, Blight/Consecration system fully realized, 1st Manifestation, 2 tiers of crafting, seasons | 4-6 months |
| **Beta** | Full 5 Manifestations (all 3 solutions each), all regions, complete bestiary, The Chronicle, Lost Scriptures | 6-9 months |
| **1.0** | Polish, random events (e.g., "The False Pilgrimage"—a demon pretending to be a survivor), mod support | 3 months |

**Critical Path:** The Blight/Consecration loop is the core mechanic. Everything else—classes, bosses, crafting—hangs on that loop working. Build a 20x20 ASCII grid where blight spreads, the Priest pushes it back, and structures decay in high blight. If that loop feels good, the rest will follow.

---

### 17. Design Notes & Philosophy

**Christian tone without colonialism:** Your "mission" is to survive and sanctify *cursed ground*. The enemy is literal Hell, not people. You are a refugee, not a conqueror. The 1600s Christian mindset is preserved (they genuinely believed the woods were haunted by demons) without making the game about destroying a people.

**Class interdependence (adapted for solo):** The asymmetry creates replayability. One player buys the game and gets three genuinely different campaigns. The cross-class Scripture system softens the edges without breaking the asymmetry.

**The Priest is revolutionary:** No other survival game makes the support class a literal requirement for map expansion. That is the unique mechanic.

**ASCII as an asset:** The abstraction lets players fill in the horror with their imagination. A `"` character shifting from grey to purple is more unsettling than a low-poly zombie.

---

*Document Version 1.0*  
*The Wilds of Canaan — Game Design Document*
