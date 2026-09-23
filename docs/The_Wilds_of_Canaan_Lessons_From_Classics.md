# The Wilds of Canaan
## Lessons from the Classics: Design Analysis Document

---

## 1. Purpose

This document analyzes five foundational ASCII games - NetHack, Dwarf Fortress, Angband, Dungeon Crawl Stone Soup (DCSS), and Caves of Qud - to extract actionable design lessons for The Wilds of Canaan. The goal is not to copy these games, but to understand why they work and apply those principles to our unique survival-horror-crafting vision.

---

## 2. NetHack: The Depth of Interconnection

### 2.1 What NetHack Does

NetHack is a dungeon crawler where the depth comes not from content volume, but from **systemic interconnection.** A towel, a tin opener, a leash, and a cockatrice corpse are all useful because the systems interact in unexpected ways. The game is famous for problems that have multiple solutions - often bizarre ones.

### 2.2 Key Lesson: The Identification Game

NetHack\'s item identification system is one of the most elegant in gaming. When you find a "scroll labeled ELAM EBOW," you do not know what it does. You must identify it through:
- **Price identification:** Shopkeepers charge based on base price. A scroll that costs 20 zorkmids is different from one that costs 50.
- **Use-identification:** Using the item reveals its effect (with safeguards).
- **Process of elimination:** Once you identify "identify" (the cheapest scroll), you can name unknown scrolls by exclusion.

**The "No Cyanide Rule":** No unidentified item should be immediately fatal under reasonable circumstances. A cursed ring of blindness is dangerous, but not instantly lethal if you have curse-removal options. This encourages experimentation rather than paranoia.

**The "Two-Sided Coin Rule":** No item is completely useless. A potion of blindness protects against Medusa\'s gaze. A "bad" wand can be zapped at yourself for a beneficial effect. This means the random number generator never gives you garbage - it gives you puzzles.

### 2.3 Application to Canaan

**The Blight Identification Parallel:**
Resources in Canaan already have a "clean vs. blighted" ambiguity. We can deepen this:

| Current | NetHack-Inspired Enhancement |
|---------|------------------------------|
| Blighted wood is just worse | Blighted wood has **unique properties**: it burns with purple flame (frightens beasts), it crafts into "cursed" traps that affect demons differently |
| You always purify blighted meat | Some pilgrims **prefer** blighted meat (it sustains them longer but raises Corruption - a tradeoff) |
| Clean Springs are just better water | Water from different sources has **different properties**: Clean Spring water boosts Faith, melted snow is pure but causes hypothermia, rainwater is abundant but unpredictable |

**The "No Cyanide Rule" for Canaan:**
- Blighted food should never kill you instantly. It should raise Corruption slowly, giving you time to find a Priest or Confessional.
- A "cursed" tool (broken, corrupted) should still be usable - just with a penalty. A broken axe still chops wood, but slower and with risk of injury.
- Winter should not instantly kill. It should drain Warmth, which drains Stamina, which makes you vulnerable. There are always warning stages.

**The "Two-Sided Coin Rule" for Canaan:**
- The Woodsman\'s salt rings expire, but expired salt can be ground into "salt dust" that marks enemy patrol paths.
- A pilgrim who goes mad (Faith 0) cannot work, but their ravings sometimes reveal hidden resource locations ("The trees whisper of copper to the east").
- Corruption is bad, but at 25+ Corruption, you can see hidden blight concentrations on the map (you are attuned to the darkness).

---

## 3. Dwarf Fortress: The Power of Emergence

### 3.1 What Dwarf Fortress Does

Dwarf Fortress generates a world with history, geology, weather, civilizations, and individual personalities. The player manages a colony of dwarves who have needs, relationships, and mental breakdowns. The game is famous for stories that emerge from simple systems interacting: a kobold steals a masterpiece scepter, the dwarf who made it falls into depression, and the player discovers this hours later through the logs.

### 3.2 Key Lesson: Tarn Adams\' Four Principles

From Tarn Adams\' design philosophy:

**1. Avoid overplanning. Start simple, then iterate.**
> "This allows for emergent gameplay and unexpected outcomes to manifest, which make the game, and even its development, more enjoyable."

**2. Break down systems into basic elements and interactions.**
> "Instead of immediately focusing on a specific intended end-result, feel or look, of it. This helps in creating a realistic and functional experience from the ground up."

**3. Avoid unnecessary complexity. Operate at the level of what the player sees, or one layer below.**
> "This simplifies the finetuning and development process, preventing getting stuck on details that do not matter to the actual experience."

**4. Base systems on real-world analogues.**
> "Which can help improve the immersion and realism of a game."

### 3.3 Key Lesson: The Line Between Control and Autonomy

Tarn Adams describes the balance as: the player is the "official will of the fortress," while dwarves exercise autonomy outside their duties. This creates emergent narrative because the dwarves are **actors in their own stories.**

### 3.4 Key Lesson: ASCII as a Feature

> "Part of the reason Dwarf Fortress can include a breadth of mechanics unseen in other games is because complex mechanics are expressed in the most simple of visual forms."

The abstraction of ASCII means the game does not need to animate a dwarf crying. It just needs to log: "Urist McMaker has been unhappy lately. He lost a masterpiece scepter to a kobold." The player\'s imagination fills in the rest.

### 3.5 Application to Canaan

**Principle 1: Start Simple, Iterate**
- The Blight system starts as a simple 0-100 value that spreads. Later iterations add: blight surges, blight "memory" (re-consecrated ground is weaker), blight "personality" (different seed points behave differently).
- Pilgrims start as simple state machines (work -> eat -> sleep). Later iterations add: relationships (two pilgrims who survived a wolf attack together get a loyalty bonus), grudges (a pilgrim who saw another flee during a raid loses Faith), and personal quests (a pilgrim asks to build a shrine to their dead brother).

**Principle 2: Basic Elements**
- The "Mood" system is not a complex simulation. It is: Food + Safety + Recent Events + Faith = Mood. That\'s it. But the **combinations** create narrative:
  - High food + Low safety = "We eat well, but we know it cannot last."
  - Low food + High faith = "We are hungry, but God provides."
  - Low food + Low faith + Recent death = "Thomas is dead. The food is gone. The Eye is open."

**Principle 3: One Layer Below**
- The player sees: "The blight advanced 3 tiles."
- The layer below: The blight algorithm checks wind direction, humidity, and holy ground proximity. But the player never sees these numbers. They see the result.
- The player sees: "Thomas is unhappy."
- The layer below: Thomas\'s Faith is 20, he has not eaten in 2 days, and he witnessed a death. But the player just sees the mood text.

**Principle 4: Real-World Analogues**
- Blight spreads like mold: it needs moisture, darkness, and organic material. In Canaan, it spreads faster in forests, slower on stone, and not at all on consecrated ground.
- Pilgrims behave like real trauma survivors: they need routine, safety, purpose, and community. The game models these needs, not complex psychology.
- Winter kills like real winter: it does not deal damage. It drains your ability to recover, which makes you vulnerable to everything else.

**The Autonomy Line for Canaan:**
- The player gives **direct commands** to their own character (move, build, attack, rite).
- The player gives **indirect commands** to pilgrims ("focus on construction" or "focus on prayer" - a toggle, not micromanagement).
- Pilgrims make **autonomous decisions** based on their state: a desperate pilgrim might flee into the blight. A faithful pilgrim might perform Last Rites without being asked. A hungry pilgrim might eat blighted meat despite orders.
- The player is the **will of the settlement**, but the pilgrims are **actors in their own survival.**

**ASCII as a Feature for Canaan:**
- We do not need to animate a blight surge. We just need to change `"` to `=` faster, pulse the color, and play a sound.
- We do not need to animate a pilgrim\'s despair. We just need to change their character from `t` to `p` (laborer to patient), stop their movement, and add a message: "Thomas has stopped working. He stares at the blight line."
- The player\'s imagination does the heavy lifting. The game provides the prompt.

---

## 4. Angband: The Philosophy of Resistance

### 4.1 What Angband Does

Angband is a dungeon crawler where progress is defined by **resistance-based combat.** Enemies deal elemental damage, and gear provides fractional or binary resistances. The game is about building a kit that can survive deeper levels, not about player skill in execution.

### 4.2 Key Lesson: The Depth/Resistance Philosophy

Angband and its variants use a design philosophy where the game is not about adapting to what it gives you, but about **building resistance to what it throws at you.** Every new depth introduces a new damage type, and your goal is to find gear that counters it.

Variants like FAangband expanded this with:
- **Fractional resistances** (25%, 50%, 75%, 100%)
- **Item pros and cons** (a ring that gives fire resistance but lowers speed)
- **Sticky curses** (items that cannot be easily removed, creating commitment)

### 4.3 Application to Canaan

**The Four Damage Types as Resistance:**
Canaan already has Physical, Silver, Holy, and Corruption damage. We can deepen this into a resistance system:

| Resistance | Source | Effect |
|------------|--------|--------|
| **Blight Resistance** | Holy Ground, blessed armor, certain herbs | Reduces Corruption gain from blight tiles |
| **Fear Resistance** | High Faith, blessed standard, certain rites | Immunity to panic effects from demons |
| **Cold Resistance** | Fur armor, braziers, warm food | Reduces Warmth drain in winter |
| **Drowning Resistance** | Iron hauberk, swimming skill | Reduces grab duration from Drowned |
| **Despair Resistance** | Chapel proximity, acolyte chanting, high Mood | Prevents pilgrim suicide/fleeing |

**Item Pros and Cons:**
- A "Blessed Fur Cloak" gives +20% warmth and +10% blight resistance, but is flammable (takes double damage from fire/braziers).
- A "Silver Mace" deals +50% vs. demons, but degrades 2x faster and is soft (cannot break stone).
- A "Reliquary" creates Holy Ground anywhere, but requires daily rare incense and attracts demons (they are drawn to holy objects).

**Sticky Commitments:**
- A pilgrim who is Blessed cannot be un-Blessed. If they later despair, they become a **Prophet of Doom** - a hostile who uses holy magic against you.
- A Craftsman who builds a Cathedral cannot tear it down. It stands as a monument, even if you regret the resources spent.
- A Woodsman who learns the Bishop\'s Fragment (cross-class consecration) permanently loses 10 max Stamina (the forest rejects his divided loyalty).

---

## 5. DCSS: The Art of Accessibility

### 5.1 What DCSS Does

Dungeon Crawl Stone Soup is a tactical roguelike that won "Roguelike of the Year" in 2008 by beating Dwarf Fortress and NetHack. Its design philosophy is: **"create a balanced, tactical game that limits grinding and reliance on out-of-game sources of information."**

### 5.2 Key Lesson: Accessibility Without Dumbing Down

DCSS achieves depth without cruelty:
- **Hints system:** In-game tooltips explain mechanics without breaking immersion.
- **Auto-explore:** Press `o` and the character explores the level automatically, stopping at enemies or items. This eliminates the tedium of empty walking.
- **Auto-fight:** Press `tab` and the character attacks the nearest enemy with basic tactics. This eliminates repetitive combat commands.
- **Standardized glyphs:** All bees use `k`, all ants use `a`. No confusion. Threat level is indicated by color and number overlays, not by obscure symbols.
- **Mouse support:** Full mouse control for players who prefer it.

### 5.3 Key Lesson: Limit Grinding

DCSS actively prevents grinding:
- Monsters do not respawn. Once a level is cleared, it is empty.
- Hunger is present but not punishing. You cannot starve to death by exploring too long.
- The game pushes forward. Staying on early levels does not help you.

### 5.4 Application to Canaan

**Accessibility Features:**
- **Auto-gather:** The Woodsman can press `G` to automatically gather all visible resources of a type within 5 tiles, stopping if hostiles appear. This eliminates the "press G 50 times" tedium.
- **Auto-path:** Click a destination on the mini-map and the character paths there, avoiding blight and hostiles. The Woodsman\'s Read the Woods ability makes this path smarter (avoiding patrol routes).
- **Contextual hints:** Hovering over a blighted tile shows: "Blighted (level 3). Corruption +1 per turn. Purify with Holy Water."
- **Standardized threat indicators:** All beasts use lowercase (`w` for wolf, `b` for bear). All demons use uppercase (`W` for Wendigo, `S` for Shadow). All undead use Greek (`z` for Drowned, `Z` for Revenant). Threat level is color + a subtle number overlay (1-5 stars).

**Limiting Grinding:**
- Renewable resources have **regen caps.** A forest tile can only regen 3 trees total. After that, it is fallow for 30 days. You cannot farm one spot forever.
- Pilgrims have **efficiency curves.** A Laborer works at 100% for 3 days, then 75%, then 50%. They need rest, or they burn out. You cannot work them forever.
- The **Mood system** prevents turtling. Staying in your base for 10 days without progress causes Mood to drop ("We are hiding, not living"). The game pushes you to venture out.

---

## 6. Caves of Qud: The Power of Framing

### 6.1 What Caves of Qud Does

Caves of Qud is a science-fantasy roguelike with a procedural world, static storyline backbone, and systems-driven narrative. It is famous for letting players become absurdly powerful through bizarre, flavorful means: cloning yourself 30 times, taming a train of gorillas, or disarming a chrome pyramid of its missile rack.

### 6.2 Key Lesson: "Before You Fix a Leak, Ask if It\'s a Fountain"

Jason Grinblat\'s design talk argues that bugs and unintended interactions should not always be fixed. Sometimes they are **fountains** - sources of emergent narrative that enrich the game. The framing of an interaction matters more than its intended design.

> "When they aren\'t directly disrupting play, bugs can cause unintended interactions between the systems that underlie a game, leading to emergent narratives while laying bare the artifice of the medium."

### 6.3 Key Lesson: Static Backbone + Procedural Flesh

Caves of Qud uses a hybrid approach:
- **Static:** The main quest, key locations, and core lore are hand-crafted.
- **Procedural:** Dungeons, wilderness, history, and side content are generated.

This gives players "bones to hang a story on" - familiar anchor points in an unpredictable world.

### 6.4 Key Lesson: Authored Systems, Not Random Events

Brian Bucklew emphasizes that Qud\'s systems are not random. They are **authored to produce certain types of stories:**

> "Those stories are still authored, right? It is true that they\'re being produced by systems, but those systems aren\'t random. They\'re not random things that are happening, those are carefully authored systems by our narrative team to produce the kind of stories that the players traverse through."

### 6.5 Application to Canaan

**The Fountain Principle:**
- If a pilgrim somehow survives standing in blight for 5 days (a bug, or edge case), do not fix it. Frame it: "Thomas has been touched by the blight. He does not die. He speaks in tongues. Other pilgrims fear him." He becomes a **Blight-Touched** - a unique NPC type with pros and cons.
- If a player builds a Chapel without walls (just an altar on holy ground), do not enforce the 5x5 rule strictly. Frame it: "This is a Humble Shrine. It grants half the Chapel bonus, but the Priest says it is more pious."
- If a Woodsman\'s camp expires while he is sleeping in it, do not just dump him on the ground. Frame it: "The lean-to collapsed in the night. You wake covered in snow. Your bedroll is soaked."

**Static Backbone + Procedural Flesh:**
- **Static:** The 5 Manifestations, the 3 endings, the Vocation abilities, the seasonal cycle, and the core crafting tiers. These are always the same.
- **Procedural:** World geometry, resource placement, blight seed points, Lost Scripture locations, pilgrim spawn points, and Chronicle entries. These change every seed.
- This gives players: "I know I need to beat the Drowned Choir to get silver, but I don\'t know where the Choir will be or what the shoreline looks like."

**Authored Systems for Canaan:**
- The Mood system is not random. It is authored to produce specific narrative arcs:
  - Hopeful -> Cautious -> Desperate -> Doomed
  - Each transition has specific trigger conditions and specific text.
  - The system is designed to tell stories of **gradual despair**, not random sadness.
- The Pilgrim event system is not random. It is authored:
  - A Laborer who witnesses 3 deaths becomes a Patient (trauma).
  - An Acolyte who performs 5 Last Rites becomes a Blessed (promotion).
  - A Hunter who brings back blighted meat 3 times is "cautioned" by the Priest (warning event).
- The Blight surge system is authored:
  - Surges happen after Day 20, 40, and 60.
  - Each surge has a "personality" based on the seed: some spread in lines, some in blobs, some target holy ground specifically.
  - The player learns to read the seed\'s "personality" over multiple runs.

---

## 7. Synthesis: The Canaan Design Philosophy

From these five games, we extract a unified philosophy:

### 7.1 The NetHack Principle: Interconnection Over Content

**Do not add more items. Add more interactions between existing items.**

- 20 resources with 50 interactions > 50 resources with no interactions.
- The Woodsman\'s salt + the Priest\'s holy water = "Blessed Salt" (permanent warding, but requires both Vocations).
- Blighted wood + Craftsman forge = "Corrupted Charcoal" (burns with demon-repelling smoke, but raises Corruption of the user).
- A dead pilgrim\'s body + Priest Last Rites + Craftsman stone tomb = "Sanctified Grave" (permanent +5 Mood to settlement).

### 7.2 The Dwarf Fortress Principle: Emergence From Simplicity

**Complex stories come from simple rules interacting, not from complex rules.**

- Pilgrims have 5 stats, 5 roles, and 3 needs. That\'s it.
- But the combinations create: a Laborer who becomes a Patient who becomes a Prophet of Doom who leads other pilgrims astray.
- The Blight has 1 rule: spread to adjacent tiles. That\'s it.
- But the combinations create: a blight surge that breaches a salt line that panics a pilgrim who flees into the forest who attracts a wolf pack that attacks the settlement while the Priest is channeling a rite.

### 7.3 The Angband Principle: Resistance as Progress

**Progress is not about getting stronger. It is about getting more prepared.**

- The player does not gain levels. They gain resistances, tools, and knowledge.
- A player who has faced the Hollow Stag once knows: it charges, it corrupts ground, it fears salt. They prepare differently on run 2.
- A player who has survived winter once knows: you need 30 days of food, a greenhouse, and fur armor. They prepare differently on run 2.
- The Chronicle is the ultimate resistance: it gives you knowledge that no gear can provide.

### 7.4 The DCSS Principle: Respect the Player\'s Time

**Eliminate tedium without eliminating challenge.**

- Auto-gather for the Woodsman. Auto-path for all. Auto-repeat for construction ("keep building walls until materials run out").
- But never auto-combat. Never auto-rite. Never auto-purify. The dangerous decisions remain manual.
- Standardized, readable glyphs. No guessing what `~` means. It is water. Always.

### 7.5 The Caves of Qud Principle: Frame the Unexpected

**Bugs and edge cases are narrative opportunities.**

- If the systems produce an unexpected result, do not patch it out. Ask: is this a fountain?
- A pilgrim who should have died but didn\'t becomes a legend.
- A base that should have fallen but didn\'t becomes a miracle.
- A player who survived Corruption 100 becomes the Blight-Touched - a new starting condition for future runs.

---

## 8. Anti-Patterns to Avoid

| Game | Pattern | Why Canaan Should Avoid It |
|------|---------|---------------------------|
| **NetHack** | Obscure interactions require out-of-game spoilers | Canaan should have in-game hints (DCSS-style). No "dipping a long sword in a fountain at full moon" secrets. |
| **Dwarf Fortress** | Interface complexity as a barrier | Canaan is web-first with mouse support. No memorizing keybinds. No nested menus 5 levels deep. |
| **Angband** | Endless grinding for resistances | Canaan limits grinding via regen caps and Mood decay. You cannot farm one spot forever. |
| **DCSS** | Over-standardization kills flavor | Canaan keeps some ambiguity. The blight has seed-specific "personalities." Pilgrims have unique names in The Chronicle. |
| **Caves of Qud** | So much weirdness that coherence suffers | Canaan keeps a consistent tone: 17th-century frontier horror. No chrome pyramids. No cloning. The weirdness is demonic, not sci-fi. |

---

## 9. The Canaan Checklist

Before any feature is added to Canaan, it should pass this checklist derived from the classics:

| Check | Question | Source |
|-------|----------|--------|
| **Interconnection** | Does this feature interact with at least 3 other systems? | NetHack |
| **Emergence** | Could this feature create an unexpected but meaningful story? | Dwarf Fortress |
| **Resistance** | Does this feature give the player a new way to prepare, not just a bigger number? | Angband |
| **Accessibility** | Can a new player understand this feature in under 30 seconds? | DCSS |
| **Framing** | If this feature breaks or produces an edge case, is it a fountain or a leak? | Caves of Qud |
| **No Cyanide** | Can this feature kill a player instantly without warning? If yes, redesign. | NetHack |
| **Two-Sided Coin** | Is there a situation where this "bad" thing is actually useful? If no, add one. | NetHack |
| **Autonomy** | Does this feature respect the line between player control and NPC autonomy? | Dwarf Fortress |
| **Tedium** | Does this feature require repetitive action? If yes, add automation. | DCSS |
| **Tone** | Does this feature fit the 17th-century frontier horror tone? If no, cut it. | Canaan-specific |

---

## 10. Summary

| Game | Core Lesson | Canaan Application |
|------|-------------|-------------------|
| **NetHack** | Interconnection creates depth | Resources have multiple uses; "bad" things have hidden upsides; identification is a game |
| **Dwarf Fortress** | Simple systems create complex stories | Mood + Pilgrims + Blight = emergent despair narratives; ASCII lets imagination do the work |
| **Angband** | Resistance is progress | Four damage types with fractional resistances; item pros and cons; sticky commitments |
| **DCSS** | Accessibility without dumbing down | Auto-gather, auto-path, standardized glyphs, in-game hints, no grinding |
| **Caves of Qud** | Frame the unexpected | Edge cases become unique NPCs; static backbone + procedural flesh; authored systems |

The Wilds of Canaan is not a clone of any of these games. It is a **synthesis:** the interconnection of NetHack, the emergence of Dwarf Fortress, the preparation-focus of Angband, the accessibility of DCSS, and the narrative framing of Caves of Qud - all in service of a unique vision: survival horror on the 17th-century frontier, where faith is your only weapon against the dark.

---

Document Version 1.0
The Wilds of Canaan - Lessons from the Classics: Design Analysis Document
