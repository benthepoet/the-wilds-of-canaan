# The Wilds of Canaan
## Git Workflow & PR Strategy

---

## 1. Philosophy

Even as a solo developer (or small team), a PR-based workflow enforces discipline. It creates a review checkpoint between "code written" and "code merged." For a project with subagent-generated content, PRs are the gate where human judgment validates machine output.

**Rules:**
- **Nothing merges to `master` without a PR.** Not even hotfixes. Not even "just a small change."
- **Every PR has a checklist.** Even if you are the only reviewer, the checklist forces you to look.
- **Subagent output goes through PRs.** Never commit subagent-generated code directly. Always review it first.
- **`master` is always deployable.** If it is on `master`, it could go live.

---

## 2. Branch Strategy

### 2.1 The Branches

| Branch | Purpose | Protection | Deploys To |
|--------|---------|-----------|------------|
| `master` | Production-ready code | PR required, 1 review, CI must pass | GitHub Pages (auto) |
| `develop` | Integration branch for active work | PR required, CI must pass | Staging (optional) |
| `feature/*` | Individual features | None (merged via PR) | — |
| `fix/*` | Bug fixes | None (merged via PR) | — |
| `content/*` | Subagent-generated content | None (merged via PR) | — |
| `release/*` | Release preparation | PR required, 1 review, CI must pass | — |

### 2.2 Branch Naming

```
feature/blight-spread-algorithm
feature/canvas-renderer
feature/pilgrim-ai

fix/wolf-pack-coordination
fix/inventory-weight-calculation
fix/chronicle-save-corruption

content/glyph-mapping-json
content/bestiary-entries
content/seasonal-messages

release/v0.1.0-prototype
release/v0.2.0-beta
```

### 2.3 The Flow

```
master (deployable)
  |
  +-- develop (integration)
        |
        +-- feature/blight-spread
        |     |
        |     +-- PR -> develop
        |
        +-- content/bestiary-entries
        |     |
        |     +-- PR -> develop
        |
        +-- PR -> master (release)
```

**Weekly rhythm:**
- Monday: Branch `feature/*` or `content/*` from `develop`.
- Wednesday: Open PR to `develop`.
- Thursday: Review and merge to `develop`.
- Friday: If `develop` is stable, open PR to `master`.

**Milestone rhythm (supersedes weekly for milestone work):**
- Every playable milestone (see `The_Wilds_of_Canaan_Playable_Milestones.md`) lands via its own PR to `develop`: branch `feature/mN-<name>` from `develop`, open the PR when the milestone's checks pass, review against the milestone doc, squash-merge.
- Small fixes between milestones (UI tweaks, bug fixes) may still commit directly to `develop`.
- PRs to `master` remain release-only (`release/*` branches).

---

## 3. The PR Process

### 3.1 Opening a PR

Every PR has a template:

```markdown
## What
[Brief description of what changed]

## Why
[Why this change was needed — link to design doc section if applicable]

## How to Test
[Steps to verify the change works]

## Checklist
- [ ] Code follows project style (ESLint passes)
- [ ] No `console.log` left in production code
- [ ] Subagent output validated (if applicable)
- [ ] Design doc updated (if behavior changed)
- [ ] Tests added or updated
- [ ] Manual testing performed (browser, 5+ minutes)
- [ ] No regressions in existing features

## Subagent Generated?
- [ ] Yes — source session: [link or description]
- [ ] No
```

### 3.2 PR Size Limits

| Type | Max Lines Changed | Why |
|------|------------------|-----|
| **Feature PR** | 500 lines | Larger = harder to review, more bugs slip through |
| **Fix PR** | 100 lines | Fixes should be surgical |
| **Content PR** | 1000 lines | JSON/text is easier to review, but still cap it |
| **Release PR** | No limit | This is the accumulated `develop` branch |

**If a PR exceeds the limit:** Split it. A 1200-line feature PR becomes two 600-line PRs.

### 3.3 Review Checklist (Self-Review for Solo Dev)

Even without a team, go through this checklist before merging:

```markdown
## Review Checklist

### Code Quality
- [ ] No magic numbers (use constants from config)
- [ ] No `any` types in TypeScript
- [ ] Functions are < 50 lines (preferably < 30)
- [ ] No nested callbacks > 3 deep
- [ ] Error handling for all async operations

### Game Logic
- [ ] No contradictions with design docs (GDD, Combat, Building, etc.)
- [ ] Numbers are within expected ranges (no 999 damage, no 0.001% chance)
- [ ] Edge cases handled (empty inventory, zero health, full blight)
- [ ] No infinite loops in AI or pathfinding

### Performance
- [ ] No memory leaks (event listeners cleaned up)
- [ ] No O(n^2) loops in hot paths (rendering, blight spread)
- [ ] Web Worker messages are batched, not per-tile

### Content (if subagent-generated)
- [ ] No hallucinated items/entities not in design docs
- [ ] Tone matches 17th-century frontier horror
- [ ] No anachronisms (no "gun," no "electricity," no "camera")
- [ ] JSON is valid and schema-compliant
- [ ] No duplicate IDs or names
```

### 3.4 Merging

**Merge method:** Squash and merge.

```bash
# Feature branch -> develop
git checkout develop
git merge --squash feature/blight-spread
git commit -m "feat: implement blight spread algorithm

- Blight spreads 1 tile/day, escalating after Day 20
- Holy ground blocks spread completely
- Visual: 5-stage progression (clean -> hell)
- Audio: hiss sound on spread, surge sound on escalation

Closes #42"
```

**Why squash:** Keeps `develop` and `master` clean. One PR = one commit. Feature branch history is disposable.

---

## 4. Commit Message Convention

### 4.1 Format

```
<type>: <short summary>

<body: what changed and why>

<footer: references, breaking changes>
```

### 4.2 Types

| Type | Use | Example |
|------|-----|---------|
| `feat` | New feature | `feat: add blight spread algorithm` |
| `fix` | Bug fix | `fix: wolf pack stops chasing at water edge` |
| `content` | Subagent-generated content | `content: add bestiary entries for all hostiles` |
| `docs` | Documentation | `docs: update combat system with status effects` |
| `refactor` | Code restructuring | `refactor: split World class into Region chunks` |
| `perf` | Performance improvement | `perf: batch DRAW protocol lines, reduce renders 40%` |
| `test` | Test addition/fix | `test: add property-based tests for blight invariants` |
| `chore` | Build/tooling | `chore: update TypeScript to 5.2` |
| `audio` | Sound/music | `audio: add winter ambient loop and ice crack SFX` |
| `ui` | Interface changes | `ui: add dynamic viewport resizing` |

### 4.3 Examples

```
feat: implement consecration rite for Priest

- Rite channels for 3 seconds, vulnerable to interruption
- Creates holy ground in radius 1/3/5/7 tiles
- Costs: Holy Water + Salt + Faith
- Visual: gold pulse expansion, blight recoil
- Audio: chanting + bell toll on completion

Closes #15
```

```
content: generate seasonal ambient messages

- 60 messages total: 15 per season
- Tagged by Vocation (Priest/Woodsman/Craftsman specific variants)
- Integrated into Mood system
- Subagent session: seasonal-messages-v1

Refs #23
```

```
fix: prevent infinite loop in wolf AI when player is unreachable

- Wolf now times out after 50 pathfinding steps
- Falls back to "patrol" behavior instead of stuck "chase"
- Added test: wolf_unreachable_patrol_fallback

Fixes #56
```

---

## 5. Subagent Workflow

### 5.1 The Subagent Branch

Subagent output never touches `develop` directly.

```
1. Main agent creates branch: content/bestiary-entries
2. Main agent runs subagent session, generates output
3. Main agent pastes output into files on content/bestiary-entries
4. Main agent reviews, edits, fixes
5. Main agent opens PR: content/bestiary-entries -> develop
6. Main agent runs review checklist
7. Main agent merges (squash)
```

### 5.2 Subagent Commit Messages

```
content: add [description] from subagent

- Source: [subagent session name or timestamp]
- Reviewed by: [main agent name]
- Changes made: [list of edits, corrections, rejections]
- Validation: [checklist results]
```

Example:
```
content: add bestiary entries for 7 hostile types

- Source: subagent session 2024-09-10-bestiary
- Reviewed by: dev
- Changes made:
  - Fixed Wendigo description (was too sci-fi, reworded to religious horror)
  - Removed "Pack Leader" variant for Shadow (Shadows are solitary)
  - Added audio cues for all entries
  - Validated JSON schema
- Validation: All 7 entries match Combat doc. No duplicates. Tone correct.
```

### 5.3 Rejecting Subagent Output

Sometimes subagent output is bad. That is fine. The branch is abandoned.

```bash
# Bad subagent output — do not merge
git branch -D content/bad-generation
# No PR opened. No history preserved. Clean failure.
```

**Document the rejection:**
- Open an issue: `subagent-rejection: [task] — [reason]`
- Example: `subagent-rejection: wolf AI — proposed behavior tree contradicts pack coordination design`
- This prevents repeating the same failed prompt.

---

## 6. CI/CD Integration

### 6.1 GitHub Actions Workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [develop, master]
  push:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run test:unit
      - run: npm run test:integration

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  deploy:
    needs: [lint, test, build]
    if: github.ref == 'refs/heads/master'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: dist
          path: dist/
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

### 6.2 PR Gates

A PR cannot merge unless:
- [ ] CI passes (lint, typecheck, unit tests, integration tests)
- [ ] Build succeeds (no TypeScript errors, no bundler errors)
- [ ] Review checklist completed (self-review for solo dev)
- [ ] No merge conflicts

### 6.3 Deploy Pipeline

| Branch | Action | URL |
|--------|--------|-----|
| `master` | Auto-deploy to GitHub Pages | `https://canaan.game` |
| `develop` | Auto-deploy to GitHub Pages (subdomain) | `https://dev.canaan.game` (optional) |
| `feature/*` | No auto-deploy. Manual `npm run preview` | `localhost:5173` |

---

## 7. Versioning & Releases

### 7.1 Semantic Versioning

```
MAJOR.MINOR.PATCH

MAJOR: Incompatible save format change, new region, new ending
MINOR: New Manifestation, new Vocation, new feature
PATCH: Bug fix, balance tweak, content addition
```

### 7.2 Version Tags

```bash
# Prototype release
git tag -a v0.1.0 -m "Prototype: Shallows + Priest + Drowned Choir"
git push origin v0.1.0

# Beta release
git tag -a v0.5.0 -m "Beta: All 5 regions, all 5 Manifestations, 3 endings"
git push origin v0.5.0

# Full release
git tag -a v1.0.0 -m "Release: The Wilds of Canaan"
git push origin v1.0.0
```

### 7.3 Release Branch

```bash
# Create release branch
git checkout -b release/v0.2.0 develop

# Final testing, bug fixes only
# ...

# Merge to master
git checkout main
git merge --no-ff release/v0.2.0
git tag -a v0.2.0

# Merge back to develop
git checkout develop
git merge --no-ff release/v0.2.0
```

---

## 8. Issue Tracking

### 8.1 Issue Labels

| Label | Color | Use |
|-------|-------|-----|
| `bug` | Red | Something is broken |
| `feature` | Green | New capability |
| `content` | Purple | Subagent-generated text/JSON |
| `balance` | Orange | Numbers feel wrong |
| `audio` | Blue | Sound or music |
| `ui` | Yellow | Interface or rendering |
| `docs` | Grey | Documentation update |
| `subagent-rejection` | Black | Subagent output was rejected |
| `prototype` | Light green | Must fix before prototype launch |
| `post-launch` | Light grey | Can wait until after release |

### 8.2 Issue Templates

**Bug Report:**
```markdown
## Bug Description
[What happened]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should have happened]

## Actual Behavior
[What actually happened]

## Environment
- Seed: [if applicable]
- Day: [if applicable]
- Browser: [Chrome/Firefox/etc.]
- Version: [game version]

## Save File
[Attach .canaan file or paste export string]
```

**Content Request:**
```markdown
## What Content Is Needed
[e.g., 10 more pilgrim death entries]

## Design Doc Reference
[Link to relevant section]

## Tone/Style Notes
[Specific guidance]

## Subagent Session
[If already generated, link or describe]
```

---

## 9. The Weekly Ritual

### Monday
- [ ] Review open PRs from last week. Merge or close.
- [ ] Create new feature/content branches for this week.
- [ ] Update project board (GitHub Projects or Trello).

### Wednesday
- [ ] Mid-week PR review. Merge completed features to `develop`.
- [ ] Run balance check (if enough changes accumulated).

### Friday
- [ ] End-of-week PR review. Merge stable `develop` to `master` if ready.
- [ ] Deploy to GitHub Pages.
- [ ] Playtest the live build for 15 minutes.
- [ ] Update CHANGELOG.md.

### As Needed
- [ ] Subagent session: generate content, review output, branch, PR, merge.
- [ ] Bug fix: branch from `develop`, fix, PR, merge.
- [ ] Hotfix: branch from `master`, fix, PR to `master` AND `develop`.

---

## 10. Summary

| Rule | Enforcement |
|------|-------------|
| **Nothing merges without PR** | Branch protection on `master` and `develop` |
| **Every PR has a checklist** | PR template |
| **Subagent output goes through PR** | Content branches, review, squash merge |
| **`master` is always deployable** | CI gates: lint, test, build |
| **Squash and merge** | Clean history, one PR = one commit |
| **Semantic versioning** | Tags for every release |
| **Self-review checklist** | Even solo devs must look before they leap |

The workflow is not bureaucracy. It is **a safety net.** The PR is the moment you stop writing and start thinking. For a project with 18 design documents and subagent-generated content, that moment is essential.

---

Document Version 1.0
The Wilds of Canaan - Git Workflow & PR Strategy
