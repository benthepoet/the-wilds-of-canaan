# The Wilds of Canaan
## Development Workflow & Subagent Strategy

---

## 1. Philosophy

Subagents are tools, not replacements. They excel at isolated tasks with bounded context. They fail at integration, architecture, and cross-system design. The main agent retains ownership of the game vision; subagents handle grunt work, research, and content generation.

**Token efficiency rules:**
- **Never give a subagent the full GDD.** Give it only the section relevant to its task.
- **Never ask a subagent to design systems.** Ask it to implement, review, or generate content within a system you designed.
- **Always validate subagent output.** Do not paste subagent code into the codebase blindly.
- **Batch subagent tasks.** One long subagent session is cheaper than five short ones (context setup cost).

---

## 2. The Main Agent's Responsibilities

The main agent (you) owns:

| Responsibility | Why It Stays Central |
|---------------|---------------------|
| **Architecture decisions** | Protocol design, engine structure, data flow. Changing this ripples through everything. |
| **Cross-system integration** | How blight affects combat, how Mood affects pilgrim AI, how seasons affect gathering. These are intersections. |
| **Balance tuning** | Numbers require holistic understanding. A subagent cannot know that wolf damage + blight spread + food scarcity create a death spiral. |
| **Code review & merge** | Only the main agent knows if a subagent's output fits the existing codebase. |
| **Asset direction** | Audio, visual, and narrative tone must be consistent. Subagents generate; the main agent curates. |
| **Playtest interpretation** | "Players die too fast" requires understanding which of 10 systems is the actual culprit. |

---

## 3. The Subagent Strategy

### 3.1 What Subagents Do Well

| Task Type | Example | Context Needed | Expected Output |
|-----------|---------|---------------|----------------|
| **Content generation** | Write 20 Chronicle death entry templates | Chronicle doc (Section 2.3) | 20 text strings, tagged by Vocation/season |
| **Content generation** | Write bestiary descriptions for all hostiles | Combat doc (Section 6) | Descriptive text + audio cue notes |
| **Code generation** | Implement the Blight spread algorithm | Technical Architecture (Section 9.2) + GDD (Section 5) | TypeScript function, typed, commented |
| **Code generation** | Implement the inventory UI component | ASCII Visual Design (Section 3) + Input doc | React/Vanilla JS component |
| **Research** | Find the best Web Audio API patterns for procedural wind | None (general knowledge) | Summary + code examples |
| **Review** | Review the combat system for edge cases | Combat doc | List of edge cases + suggested fixes |
| **Asset lists** | Catalog all audio files needed with filenames | Audio Design doc | JSON list: {id, filename, duration, priority} |
| **Test generation** | Write unit tests for the crafting system | Building doc (Section 9) + Resource Gathering doc | Test cases with assertions |
| **Documentation** | Generate API docs from protocol types | Technical Architecture (Section 3) | Markdown table of protocol commands |

### 3.2 What Subagents Do Poorly

| Task Type | Why It Fails | What To Do Instead |
|-----------|-------------|-------------------|
| **System design** | Lacks holistic context. Proposes solutions that break other systems. | Main agent designs. Subagent implements. |
| **Architecture refactoring** | Cannot trace ripple effects across 17 documents. | Main agent refactors. Subagent tests. |
| **Cross-system balance** | Tunes one system without seeing downstream effects. | Main agent tunes. Subagent runs simulations. |
| **Narrative arc design** | Does not understand the emotional tone of Canaan. | Main agent arcs. Subagent writes individual entries. |
| **Visual direction** | Generates inconsistent art descriptions. | Main agent defines palette and style. Subagent lists assets. |

---

## 4. The 12-Week Workflow

### Phase 1: Foundation (Weeks 1-2)

**Main Agent:**
- Design the engine core architecture (World, Tile, Entity classes).
- Design the protocol format.
- Implement procedural map generation.
- Set up the build pipeline (TypeScript, bundler, dev server).

**Subagent (1 session, ~4K tokens):**
- **Task:** Research and summarize Web Worker best practices for game engines.
- **Input:** "I am building a browser-based ASCII game engine in TypeScript. The engine runs in a Web Worker and communicates with a Canvas renderer via postMessage. What are the best practices for: (1) memory management in Workers, (2) efficient serialization for postMessage, (3) handling Worker crashes gracefully?"
- **Output:** 3-section summary with code snippets.
- **Integration:** Main agent reviews, applies relevant patterns to engine setup.

**Token budget:** Main agent ~15K, Subagent ~4K. Total: ~19K.

---

### Phase 2: Browser Client (Weeks 3-4)

**Main Agent:**
- Implement the Canvas renderer (dynamic viewport, zoom, cell drawing).
- Implement the input system (keyboard + mouse).
- Implement the protocol parser.
- Set up localStorage save/load.
- Deploy to GitHub Pages.

**Subagent (1 session, ~5K tokens):**
- **Task:** Generate the glyph mapping JSON file (ASCII mode).
- **Input:** "Here is the terrain palette and creature list from the ASCII Visual Design doc. Generate a complete `glyphs_ascii.json` file with all tile:state combinations, their characters, foreground colors, and background colors. Follow the format in the Technical Architecture doc."
- **Output:** Complete JSON file.
- **Integration:** Main agent loads JSON, tests rendering, fixes any missing entries.

**Token budget:** Main agent ~20K, Subagent ~5K. Total: ~25K.

---

### Phase 3: Gathering & Tools (Week 5)

**Main Agent:**
- Implement resource spawning and regeneration.
- Implement tool system (crafting, degradation).
- Implement inventory and weight.
- Implement hunger/thirst.

**Subagent (1 session, ~4K tokens):**
- **Task:** Write all item descriptions and tool stat blocks.
- **Input:** "From the Resource Gathering doc and Combat doc, write a complete `items.json` file containing: all tools, all weapons, all armor, all consumables. Each entry needs: id, name, description, weight, durability, effects."
- **Output:** JSON file with ~40 items.
- **Integration:** Main agent loads into item database, adjusts balance numbers.

**Token budget:** Main agent ~12K, Subagent ~4K. Total: ~16K.

---

### Phase 4: The Blight & The Priest (Week 6)

**Main Agent:**
- Implement blight spread algorithm.
- implement consecration rite.
- Implement Corruption stat and effects.
- Implement first hostile (wolf AI).

**Subagent (1 session, ~3K tokens):**
- **Task:** Generate wolf AI behavior tree pseudocode.
- **Input:** "Design a behavior tree for a wolf pack in a turn-based ASCII survival game. The wolf has states: idle, stalking, surrounding, attacking, fleeing. It should coordinate with pack members. It should fear fire and water. Output as pseudocode or a state machine diagram in text."
- **Output:** Behavior tree pseudocode.
- **Integration:** Main agent implements in TypeScript, adjusts for grid-based movement.

**Token budget:** Main agent ~15K, Subagent ~3K. Total: ~18K.

---

### Phase 5: Building & The Craftsman (Week 7)

**Main Agent:**
- Implement blueprint system (ghost, planned, framed, complete).
- Implement freeform building.
- Implement construction stages rendering.
- Implement pilgrim system (basic AI, Laborer role).

**Subagent (1 session, ~5K tokens):**
- **Task:** Write all blueprint definitions and material costs.
- **Input:** "From the Building doc, write a complete `blueprints.json` file with all 15+ Craftsman blueprints. Each needs: id, name, size (w x h), materials (with counts), bonus description, unlock tier, and ASCII char."
- **Output:** JSON file.
- **Integration:** Main agent loads into blueprint database.

**Token budget:** Main agent ~18K, Subagent ~5K. Total: ~23K.

---

### Phase 6: Winter & The Woodsman (Week 8)

**Main Agent:**
- Implement season system and transitions.
- Implement winter mechanics (snow, ice, warmth drain).
- Implement Woodsman Vocation (speed, tracking, camps).
- Implement Blood Moon event.
- Implement Wendigo AI.

**Subagent (1 session, ~4K tokens):**
- **Task:** Generate all seasonal ambient text and Mood shift messages.
- **Input:** "From the Building doc (Mood system) and GDD (seasons), write a complete set of ambient text messages for: (1) each season transition, (2) each Mood tier shift (Hopeful->Cautious->Desperate->Doomed), (3) 10 random daily messages per season. Tag each by Vocation if Vocation-specific."
- **Output:** ~60 text strings in JSON format.
- **Integration:** Main agent loads into message database, hooks into Mood system.

**Token budget:** Main agent ~18K, Subagent ~4K. Total: ~22K.

---

### Phase 7: The First Manifestation (Week 9)

**Main Agent:**
- Implement the Drowned Choir boss entity.
- Implement boss arena mechanics.
- Implement 3 solution paths (Priest rite, Woodsman traps, Craftsman siege).
- Implement boss loot and Tier 2 unlock.
- Implement Chronicle system (basic).

**Subagent (1 session, ~4K tokens):**
- **Task:** Write the Drowned Choir's combat dialogue and Chronicle entries.
- **Input:** "Write: (1) 5 telegraph messages the Drowned Choir emits before spawning, (2) 3 Chronicle entries describing encounters with the Choir (different Vocations), (3) 3 death entries for players killed by the Choir. Tone: 17th-century frontier horror, religious dread."
- **Output:** 11 text strings.
- **Integration:** Main agent adds to message database and Chronicle templates.

**Token budget:** Main agent ~20K, Subagent ~4K. Total: ~24K.

---

### Phase 8: The Full Bestiary (Week 10)

**Main Agent:**
- Implement all enemy types and AI.
- Implement status effects.
- Implement combat system (turn-based, 2 AP).
- Implement weapon degradation.
- Implement death types.

**Subagent (1 session, ~6K tokens):**
- **Task:** Generate complete bestiary entries for all 7 enemy types.
- **Input:** "From the Combat doc, write a complete `bestiary.json` with entries for: Corrupted Wolf, Bear, Corrupted Deer, Wendigo, Shadow, Drowned, Revenant. Each needs: name, description (2-3 sentences), behavior summary, weakness, resistance, audio cues, and 3 variant names (e.g., 'Rabid Wolf', 'Pack Leader')."
- **Output:** JSON file with 7 detailed entries.
- **Integration:** Main agent loads into bestiary database, uses descriptions for examine tooltips.

**Token budget:** Main agent ~20K, Subagent ~6K. Total: ~26K.

---

### Phase 9: Pilgrims & Mood (Week 11)

**Main Agent:**
- Implement all pilgrim roles and AI.
- Implement Mood system.
- Implement pilgrim events.
- Implement cemetery and grave mechanics.
- Implement Confessional structure.

**Subagent (1 session, ~5K tokens):**
- **Task:** Generate pilgrim names, backstories, and event texts.
- **Input:** "Generate: (1) 20 pilgrim names (10 male, 10 female, 17th-century Puritan style), (2) 10 rescue scenarios (how they are found in the wild), (3) 10 death Chronicle entries (different causes, different Vocations writing them), (4) 5 'miracle' entries (unlikely survival stories)."
- **Output:** ~45 text strings in JSON.
- **Integration:** Main agent loads into pilgrim database and Chronicle template system.

**Token budget:** Main agent ~18K, Subagent ~5K. Total: ~23K.

---

### Phase 10: Polish & The Endgame (Week 12)

**Main Agent:**
- Implement all 5 regions.
- Implement at least 1 ending fully.
- Implement title screen, character creation, death screen.
- Implement audio engine (Web Audio API).
- Bug fixes, balance passes, performance optimization.
- Playtest with external players.

**Subagent (1 session, ~5K tokens):**
- **Task:** Generate the complete audio asset list and implementation notes.
- **Input:** "From the Audio Design doc, generate a complete `audio_manifest.json` with every sound needed for the prototype. Each entry needs: id, filename, type (ambient/sfx/music), duration, loop (true/false), priority (1-5), and a 1-sentence description of when it plays."
- **Output:** JSON file with ~60 audio entries.
- **Integration:** Main agent uses manifest to implement audio loading and playback. Can generate placeholder sounds if real audio is not ready.

**Subagent (optional, 1 session, ~3K tokens):**
- **Task:** Write the tutorial script (first 10 minutes of gameplay).
- **Input:** "Write a step-by-step tutorial script for the first 10 minutes of Canaan. The player is a Priest who just washed ashore. Include: what they see, what hints appear, what they learn, and where they are likely to die first. Format: timestamp + message + context hint."
- **Output:** Tutorial script document.
- **Integration:** Main agent implements hint triggers based on script.

**Token budget:** Main agent ~25K, Subagent ~8K. Total: ~33K.

---

## 5. Weekly Token Budget Summary

| Week | Main Agent | Subagent | Total | Subagent Task |
|------|-----------|----------|-------|---------------|
| 1-2 | 15K | 4K | 19K | Web Worker research |
| 3-4 | 20K | 5K | 25K | Glyph mapping JSON |
| 5 | 12K | 4K | 16K | Items database |
| 6 | 15K | 3K | 18K | Wolf AI pseudocode |
| 7 | 18K | 5K | 23K | Blueprints JSON |
| 8 | 18K | 4K | 22K | Seasonal messages |
| 9 | 20K | 4K | 24K | Choir dialogue |
| 10 | 20K | 6K | 26K | Bestiary entries |
| 11 | 18K | 5K | 23K | Pilgrim content |
| 12 | 25K | 8K | 33K | Audio manifest + tutorial |
| **Total** | **181K** | **48K** | **229K** | — |

**Subagent share: 21% of total tokens.** Efficient. The main agent does the hard integration work; subagents handle content and research.

---

## 6. Subagent Prompt Templates

### Template 1: Content Generation

```
You are a content generator for The Wilds of Canaan, a 17th-century frontier survival horror ASCII game.

CONTEXT:
[Paste relevant section from design doc]

TASK:
[Specific request: generate X items of type Y, following format Z]

CONSTRAINTS:
- Tone: [grim, religious, sparse, 17th-century diction]
- Length: [max 15 words per entry / 2-3 sentences / etc.]
- Format: [JSON / Markdown list / plain text]
- Tags: [include metadata for Vocation, season, mood]

OUTPUT:
[Expected format example]
```

### Template 2: Code Generation

```
You are a TypeScript developer for The Wilds of Canaan.

CONTEXT:
[Paste relevant architecture section]

EXISTING CODE:
[Paste the interface/class the code must integrate with]

TASK:
Implement [function name] that [does X].

CONSTRAINTS:
- Must match the existing interface.
- Must handle edge cases: [list edge cases].
- Must be typed (no `any`).
- Include comments explaining logic.

OUTPUT:
TypeScript code only. No explanation outside code comments.
```

### Template 3: Research

```
You are researching [technology/pattern] for a browser-based ASCII game.

CONTEXT:
[2-sentence project description]

QUESTION:
[Specific technical question]

CONSTRAINTS:
- Focus on practical implementation, not theory.
- Include code examples where possible.
- Note browser compatibility issues.

OUTPUT:
3-paragraph summary + code snippet.
```

### Template 4: Review

```
You are reviewing [system] for The Wilds of Canaan.

CONTEXT:
[Design doc section]

CODE TO REVIEW:
[Paste code]

TASK:
Identify: (1) bugs, (2) edge cases not handled, (3) performance issues, (4) deviations from design doc.

OUTPUT:
Bullet list. Each item: [Severity: High/Med/Low] [Issue] [Suggested fix].
```

---

## 7. When NOT to Use a Subagent

| Situation | Why | What To Do |
|-----------|-----|------------|
| **Architecture change** | Needs full context of all 17 documents | Main agent decides. |
| **Bug in cross-system interaction** | Subagent sees one file, not the ripple | Main agent traces. Subagent tests fix. |
| **Playtest feedback interpretation** | Requires holistic design sense | Main agent analyzes. Subagent generates survey questions. |
| **Asset creation** | Subagents cannot generate actual images/audio | Main agent directs. Human artists/tools create assets. |
| **Real-time debugging** | Context window too small for full debug state | Main agent debugs. Subagent researches error patterns. |

---

## 8. The Handoff Protocol

When a subagent finishes, its output must be validated before integration:

```
SUBAGENT OUTPUT RECEIVED
  Task: [what was asked]
  Format: [JSON / code / text]

VALIDATION CHECKLIST:
  [ ] Output matches requested format
  [ ] No hallucinated fields or entries
  [ ] Tone matches Canaan's voice
  [ ] No contradictions with existing design docs
  [ ] Numbers are reasonable (not 999 damage, not 0.001% chance)

INTEGRATION:
  [ ] Loaded into correct file/location
  [ ] Referenced by main code
  [ ] Tested in browser
  [ ] No console errors

COMMIT:
  [ ] Commit message: "Add [feature] from subagent session"
  [ ] Tag: subagent-generated
```

---

## 9. Summary

| Principle | Application |
|-----------|-------------|
| **Subagents do content, main agent does architecture** | Subagents write JSON, text, pseudocode. Main agent writes engine, renderer, integration. |
| **Context is bounded** | Subagents get 1-2 document sections, not all 17. |
| **Batch for efficiency** | One 5K subagent session > five 1K sessions. |
| **Validate everything** | Subagent output is draft, not final. |
| **21% token share** | Subagents handle ~48K of 229K total tokens. The rest is integration, debugging, and design. |

The workflow is not about replacing the main agent. It is about **amplifying** the main agent — letting them focus on the hard problems (architecture, balance, integration) while subagents handle the volume work (content, lists, research, templates).

---

Document Version 1.0
The Wilds of Canaan - Development Workflow & Subagent Strategy
