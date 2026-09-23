# The Wilds of Canaan
## Post-Release & Live Operations Document

---

## 1. Philosophy

The 12-week prototype is not the end. It is the foundation. This document outlines what happens after the prototype is proven — how the game grows, sustains, and serves its community.

**Principles:**
- **The core game is sacred.** No patch should break a seed. No update should invalidate a player's knowledge.
- **Content is modular.** Tile packs, new regions, and new Manifestations are additions, not replacements.
- **The community is the second designer.** Player stories, seeds, and Chronicles shape what gets built next.

---

## 2. Release Roadmap

### 2.1 Phase 1: The Prototype (Months 1-3)

**Deliverable:** Browser-only, single-player, 1 Manifestation, 3 Vocations, 1 region.

**Goals:**
- Prove the core loop is fun.
- Gather 100+ playtesters.
- Validate the Chronicle as a retention mechanic.
- Test balance (survival curve, Vocation parity, blight speed).

**Success criteria:**
- Average session length > 45 minutes.
- 30% of players start a second run within 24 hours.
- 10% of players try all 3 Vocations.
- Zero critical bugs (crash, save corruption, soft-lock).

### 2.2 Phase 2: The Full Game (Months 4-9)

**Deliverable:** All 5 Manifestations, all 5 regions, 3 endings, mod support.

**New content:**
- **Regions 2-5:** Black Pines, Frozen Straits, The Mire, The Bluffs.
- **Manifestations 2-5:** The Hollow Stag, The Leviathan's Shadow, The Crooked Man, The Burning Eye.
- **Endings:** The Sanctuary, The Passage, The Bastion.
- **Mod system:** Tile packs, custom seeds, custom Manifestations.
- **Settings:** Full accessibility suite, keybinds, difficulty presets.

**Technical:**
- Port engine to Go.
- Deploy backend for cloud saves and leaderboards.
- Steam page, itch.io page, Discord server.

### 2.3 Phase 3: The Living World (Months 10-18)

**Deliverable:** Post-launch content, community features, multiplayer.

**Content updates:**
- **Seasonal events:** Winter Solstice (harder winter), The Longest Night (endless night mode).
- **New Vocations:** The Hermit (solo survival specialist), The Missionary (pilgrim-focused).
- **New Manifestations:** Community-designed bosses (contest winners).
- **New regions:** Procedural expansions beyond the Bluffs.

**Community features:**
- **Seed leaderboards:** Longest survival per seed, per Vocation.
- **Chronicle sharing:** Browse other players' Chronicles. Vote on best stories.
- **Ghost replays:** Watch top players' runs on any seed.
- **Weekly challenges:** Fixed seed, fixed Vocation, compete for high score.

**Multiplayer (co-op):**
- 2-3 players, shared world.
- Each player controls one Vocation (asymmetric co-op).
- Shared base, shared resources, shared blight.
- The ultimate test: can a Priest, Woodsman, and Craftsman survive together?

---

## 3. Monetization

### 3.1 The Base Game

**Price:** $15-20 USD.

**Includes:**
- All 5 regions
- All 5 Manifestations
- All 3 endings
- All 3 Vocations
- Mod support
- Free updates (bug fixes, balance patches, seasonal events)

### 3.2 Tile Packs (Cosmetic DLC)

| Pack | Price | Content |
|------|-------|---------|
| **The Holy Pack** | $3 | Stained glass aesthetic, cathedral tiles, angelic motifs |
| **The Wild Pack** | $3 | Overgrown ruins, mossy stones, nature reclaiming |
| **The Dark Pack** | $3 | Gothic horror, blood tiles, occult symbols |
| **The Founders Pack** | Free | ASCII-only (default). Ships with base game. |

**Why cosmetic only:** The game is balanced around information (blight level, terrain type). Cosmetic packs cannot change gameplay. They only change how information is presented.

### 3.3 Soundtrack DLC

| Pack | Price | Content |
|------|-------|---------|
| **The Choir** | $5 | Extended chanting, seasonal music, Manifestation themes |
| **The Silence** | Free | Ambient only (default). Ships with base game. |

### 3.4 What Is NOT Monetized

- **Vocations:** All 3 (or more) are base game. Never locked behind paywall.
- **Regions:** All 5 are base game.
- **Manifestations:** All 5 are base game.
- **Endings:** All 3 are base game.
- **Mods:** Free. Community-created content is free.
- **Seeds:** Free. Community-shared seeds are free.
- **Chronicle sharing:** Free.
- **Cloud saves:** Free (with account).
- **Multiplayer:** Free (with base game).

**The rule:** Pay once, play forever. DLC is cosmetic or audio only.

---

## 4. Community Engagement

### 4.1 The Seed of the Week

Every Monday, the developers publish a **featured seed**:
- Fixed seed string.
- Fixed starting Vocation (optional challenge).
- Community competes for longest survival.

**Leaderboard:**
```
Seed of the Week: "The Frozen Choir" (seed: frozen_choir_2024)

Rank | Player        | Vocation  | Days | Cause
-----|---------------|-----------|------|------
1    | WildernessDan | Craftsman | 47   | The Burning Eye
2    | FaithKeeper   | Priest    | 41   | Starvation
3    | TreeReader    | Woodsman  | 38   | Wolves
...  | ...           | ...       | ...  | ...
```

**Prize:** Bragging rights. Name in the game credits. Exclusive tile pack (cosmetic).

### 4.2 The Chronicle Archive

A web gallery of player-submitted Chronicles:
- Browse by seed, Vocation, cause of death.
- Vote on best stories.
- "Featured Chronicles" displayed on the title screen (rotating).

**Submission:** One-click export from death screen. Upload to archive. Moderated for spam.

### 4.3 Developer Blog

Monthly blog posts covering:
- Balance changes (with data).
- New content teasers.
- Community highlights (best Chronicles, best seeds).
- Technical deep dives (how the blight algorithm works, how procedural generation works).

### 4.4 Discord Integration

- **Bot commands:** `!seed 7f3a9c` — shows seed stats. `!leaderboard` — current rankings.
- **Role rewards:** "Survived Winter" (role for anyone who survived past Day 30). "Banished the Eye" (role for defeating Manifestation 5).
- **Dev presence:** Weekly AMA. Bug reports channel. Suggestions channel.

---

## 5. Content Update Schedule

### 5.1 Patch Cycle

| Type | Frequency | Content |
|------|-----------|---------|
| **Hotfix** | As needed | Crash fixes, save corruption fixes, critical balance issues. |
| **Balance Patch** | Monthly | Number tuning based on telemetry. No new content. |
| **Content Update** | Quarterly | New Manifestation, new region, or new Vocation. |
| **Major Expansion** | Yearly | Large content drop (e.g., multiplayer, campaign mode). |

### 5.2 Year 1 Content Plan

| Month | Update | Content |
|-------|--------|---------|
| **M1-3** | Launch | Base game: 5 regions, 5 Manifestations, 3 endings. |
| **M4** | Balance 1 | Winter difficulty tuned. Wolf AI improved. |
| **M5** | Content 1 | New Vocation: The Hermit. |
| **M6** | Content 2 | New Manifestation: community-designed (contest winner). |
| **M7** | Summer Event | The Longest Day (endless summer mode, heat mechanics). |
| **M8** | Balance 2 | Pilgrim AI overhaul. Mood system refined. |
| **M9** | Content 3 | New region: The Ashlands (post-Bluffs volcanic area). |
| **M10** | Content 4 | Multiplayer beta (2-player co-op). |
| **M11** | Autumn Event | The Harvest (abundant resources, but Manifestations are stronger). |
| **M12** | Major 1 | Multiplayer full release. Campaign mode (5 connected missions). |

---

## 6. Mod Support

### 6.1 The Mod System

Mods are **JSON + image files** in a zip folder. No code required.

```
my_mod.zip
  mod.json           # Metadata
  glyphs.json        # Tile mapping overrides
  sprites/
    pine_tree.png
    pine_tree_dead.png
    water_1.png
    water_2.png
  audio/
    wind_spring.ogg
    consecrate_bell.ogg
  ui/
    style.css        # Optional: custom UI colors
```

**mod.json:**
```json
{
  "id": "wilderness_reborn",
  "name": "Wilderness Reborn",
  "version": "1.0.0",
  "author": "WildernessDan",
  "description": "Overgrown ruins and nature-reclaimed tiles.",
  "replaces": {
    "forest:clean": "sprites/pine_tree.png",
    "forest:blighted": "sprites/pine_tree_dead.png",
    "water:open": "sprites/water_1.png"
  },
  "audio_replaces": {
    "ambient_wind_spring": "audio/wind_spring.ogg"
  }
}
```

### 6.2 Mod Distribution

- **In-game browser:** Browse, download, enable mods from within the game.
- **Steam Workshop:** One-click subscribe.
- **itch.io / GitHub:** Manual download and drop into `mods/` folder.

### 6.3 Mod Validation

```typescript
function validateMod(mod: Mod): boolean {
    // Check required files
    if (!mod.glyphs && !mod.replaces) {
        return false;  // Must replace something
    }

    // Check image sizes (must match tile_size)
    for (const [key, path] of Object.entries(mod.replaces)) {
        const img = loadImage(path);
        if (img.width !== 16 || img.height !== 16) {
            console.warn(`Mod ${mod.id}: ${path} is not 16x16`);
            return false;
        }
    }

    // Check for malicious content (no script tags in JSON)
    if (JSON.stringify(mod).includes('<script')) {
        return false;
    }

    return true;
}
```

### 6.4 Official Mods

Developers release official mods as examples:
- **The ASCII Pack:** Pure ASCII, no sprites. Demonstrates minimal mod.
- **The 16-Bit Pack:** SNES-style pixel art. Demonstrates sprite replacement.
- **The Horror Pack:** Dark, gritty, blood-stained. Demonstrates audio replacement.

---

## 7. Platform Expansion

### 7.1 Steam (PC)

- **Release:** Month 3 (after prototype proves fun).
- **Features:** Achievements, cloud saves, Steam Workshop, controller support.
- **Price:** $15-20.

### 7.2 itch.io (PC / Web)

- **Release:** Month 2 (prototype lives here permanently).
- **Features:** Browser demo (free), downloadable full game (paid).
- **Price:** $15-20, or "pay what you want" for supporters.

### 7.3 Mobile (Future)

- **Release:** Month 12+.
- **Challenges:** Touch controls, smaller viewport, battery life.
- **Solution:** Touch-optimized UI, auto-save every turn, reduced particle effects.

### 7.4 Console (Future)

- **Release:** Month 18+.
- **Platforms:** Nintendo Switch (ideal for turn-based), PlayStation, Xbox.
- **Challenges:** Certification, controller-only input, performance.
- **Solution:** Go backend for cloud saves, full controller support from Day 1.

---

## 8. Long-Term Sustainability

### 8.1 The Team

**Minimum viable team (post-prototype):**
| Role | FTE | Responsibility |
|------|-----|---------------|
| **Game Designer** | 1.0 | Balance, content design, community engagement |
| **Programmer** | 1.0 | Engine, backend, mod support |
| **Artist** | 0.5 | Tile packs, promotional art |
| **Audio Designer** | 0.5 | Sound effects, music, ambient |
| **Community Manager** | 0.5 | Discord, social media, support |

**Total: 3.5 FTE.** Sustainable at ~5,000 copies sold.

### 8.2 Revenue Projections

| Milestone | Copies | Revenue (at $15) | Notes |
|-----------|--------|-------------------|-------|
| **Break-even** | 5,000 | $75,000 | Covers 1 year of development |
| **Sustainable** | 20,000 | $300,000 | Funds Year 2 content |
| **Success** | 50,000 | $750,000 | Funds multiplayer + console ports |
| **Hit** | 100,000 | $1.5M | Franchise potential |

### 8.3 The 5-Year Vision

| Year | Goal |
|------|------|
| **Year 1** | Launch base game. Build community. Prove monetization. |
| **Year 2** | Multiplayer full release. First console port (Switch). |
| **Year 3** | Campaign mode (5 connected missions, narrative-driven). |
| **Year 4** | Canaan 2 (sequel, new setting, new mechanics). |
| **Year 5** | Canaan MMO (shared persistent world, guilds, territory control). |

**Year 5 is aspirational.** Years 1-2 are the focus.

---

## 9. Summary

| Phase | Timeline | Focus |
|-------|----------|-------|
| **Prototype** | Months 1-3 | Prove fun, gather feedback, test balance |
| **Full Game** | Months 4-9 | Complete content, mod support, Steam launch |
| **Living World** | Months 10-18 | Community features, multiplayer, content updates |
| **Expansion** | Years 2-3 | Console ports, campaign mode, sequel planning |

| Revenue Model | Details |
|--------------|---------|
| **Base game** | $15-20, one-time purchase |
| **Tile packs** | $3 each, cosmetic only |
| **Soundtrack** | $5, optional |
| **Never monetized** | Vocations, regions, Manifestations, endings, mods, seeds |

| Community Pillar | Method |
|-----------------|--------|
| **Seed of the Week** | Weekly challenge, leaderboard, prizes |
| **Chronicle Archive** | Player story sharing, voting, featured stories |
| **Mod Support** | JSON-based, Steam Workshop, in-game browser |
| **Developer Blog** | Monthly transparency, data-driven balance |
| **Discord** | Real-time community, dev presence, role rewards |

The Wilds of Canaan is not a game you finish. It is a game you survive, you remember, and you return to — again and again, as the world grows and the darkness deepens.

---

Document Version 1.0
The Wilds of Canaan - Post-Release & Live Operations Document
