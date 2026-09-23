# The Wilds of Canaan
## Input & Control Design Document

---

## 1. Philosophy

The Wilds of Canaan is a **keyboard-primary** game with **full mouse support.** This is not a compromise. It is a deliberate design choice based on the DCSS lesson: accessibility does not mean dumbing down. A game that can be played with a keyboard in 30 seconds and with a mouse in 2 minutes serves both audiences without sacrificing depth.

**Core principles:**
- **Keyboard is fast.** Experienced players should never need to touch the mouse.
- **Mouse is discoverable.** New players should never need to memorize keybinds.
- **Both are complete.** No action is keyboard-only or mouse-only. Every system works with both.
- **Gamepad is future.** Not supported in the 12-week prototype, but the architecture allows it.

---

## 2. Keyboard: The Primary Language

### 2.1 Why Keyboard-Primary?

Roguelike players expect keyboard control. It is faster, more precise, and does not require moving a cursor across the screen. In a game where a single turn can mean life or death, speed matters.

**The Numpad vs. Vi-keys Debate:**
Canaan supports both, plus arrow keys with modifiers.

| Direction | Numpad | Vi-keys | Arrow Keys |
|-----------|--------|---------|------------|
| North | 8 | k | Up |
| South | 2 | j | Down |
| West | 4 | h | Left |
| East | 6 | l | Right |
| Northwest | 7 | y | Shift+Up+Left |
| Northeast | 9 | u | Shift+Up+Right |
| Southwest | 1 | b | Shift+Down+Left |
| Southeast | 3 | n | Shift+Down+Right |
| Wait/Rest | 5 | . | Space |

**Default:** Vi-keys are the default (hjklyubn). Numpad is auto-detected if a numpad key is pressed. Arrow keys work but are slower (no diagonal without shift).

### 2.2 The Core Keymap

**Movement & Basic Actions:**
| Key | Action | Context |
|-----|--------|---------|
| `h/j/k/l/y/u/b/n` | Move 1 tile | Always |
| `Shift + direction` | Sprint (2 tiles, costs Stamina) | Always |
| `.` or `5` | Wait 1 turn | Always |
| `>` or `<` | Enter/Exit structure | Adjacent to door |
| `g` | Gather/Butcher/Interact | Adjacent to resource/corpse |
| `f` | Fire/Throw | With ranged weapon equipped |
| `a` | Attack (melee) | Adjacent to hostile |
| `r` | Channel Rite (Priest) | On Holy Ground |

**Inventory & Equipment:**
| Key | Action |
|-----|--------|
| `i` | Inventory |
| `e` | Equip/Unequip |
| `d` | Drop |
| `u` | Use (consumable) |
| `q` | Quaff (drink) |
| `w` | Wield (weapon) |
| `W` | Wear (armor) |
| `t` | Throw |

**Building & Crafting:**
| Key | Action | Vocation |
|-----|--------|----------|
| `B` | Build (blueprint menu) | Craftsman |
| `b` | Build freeform (wall/floor) | Craftsman |
| `R` | Perform Rite | Priest |
| `c` | Camp (temporary structure) | Woodsman |
| `C` | Craft (open crafting menu) | All |
| `T` | Place Trap | Craftsman/Woodsman |

**Information:**
| Key | Action |
|-----|--------|
| `x` | Look/Examine (cursor mode) |
| `X` | Read the Woods (Woodsman) |
| `m` | Map screen (full zoom-out) |
| `M` | Mood/Settlement status |
| `l` | Lost Scriptures (known) |
| `L` | The Chronicle (current run) |
| `?` | Help screen (contextual) |

**System:**
| Key | Action |
|-----|--------|
| `Esc` | Cancel/Back/Close menu |
| `Enter` | Confirm/Select |
| `Tab` | Cycle targets (combat) |
| `Space` | Advance text/Continue |
| `S` | Save and quit |
| `Ctrl+S` | Quick save (Ironman: just records state) |
| `V` | Toggle View (world / zoomed base) |
| `Z` | Toggle Zoom (far / normal / close) |

### 2.3 Contextual Key Hints

The bottom bar always shows context-sensitive hints:

```
> build wall                    [TAB:Map]  [Z]oom  [V]iew  [?]Help
```

When hovering over a tile with the mouse, the hints update:
```
Pine tree (clean)               [G]ather  [X]Examine  [C]hop
```

When in combat:
```
Corrupted Wolf (wounded)        [A]ttack  [F]ire  [T]rap  [R]etreat
```

### 2.4 Modifier Keys

| Modifier | Effect |
|----------|--------|
| `Shift + move` | Sprint (2 tiles, costs 20 Stamina) |
| `Ctrl + move` | Move until hostile spotted or destination reached (auto-explore) |
| `Shift + click` | Queue action (perform after current action completes) |
| `Alt + number` | Quick-use item slot |

---

## 3. Mouse: The Discoverable Path

### 3.1 Why Full Mouse Support?

The web prototype is played in a browser. Browser users expect mouse control. A player who discovers the game from a link should be able to play without reading a manual.

**DCSS Lesson:** Mouse support does not hurt the game. It brings in players who would otherwise bounce. Those players may later learn keyboard shortcuts. But they can play the entire game with a mouse if they choose.

### 3.2 Mouse Actions

**Left Click:**
| Target | Action |
|--------|--------|
| Empty ground (adjacent) | Move to tile |
| Empty ground (distant) | Pathfind to tile (avoiding blight/hostiles if possible) |
| Resource (tree, rock, etc.) | Gather/Interact |
| Hostile (adjacent) | Attack |
| Hostile (distant, with ranged weapon) | Fire at target |
| Structure (door) | Open/Close |
| Structure (forge, altar, etc.) | Use/Interact |
| Item on ground | Pick up |
| Player (self) | Open character/status panel |

**Right Click:**
| Target | Action |
|--------|--------|
| Any tile | Context menu: Examine, Move Here, Gather, Attack, Place Trap, etc. |
| Ground (Craftsman) | Build menu: Wall, Floor, Door, Blueprint... |
| Ground (Priest) | Rite menu: Consecrate, Bless Flame, Circle of Salt... |
| Ground (Woodsman) | Camp menu: Lean-To, Firepit, Salt Ring... |
| Hostile | Examine (shows stats, weaknesses, last known behavior) |
| Pilgrim | Examine (shows name, role, mood, recent events) |

**Scroll Wheel:**
| Direction | Action |
|-----------|--------|
| Up | Zoom in (close -> normal -> far) |
| Down | Zoom out (far -> normal -> close) |

**Click and Drag:**
- **Map screen:** Pan the map (when zoomed in).
- **Inventory:** Drag items to equip, drop, or give to pilgrim.

### 3.3 Hover Tooltips

Hovering over any tile or entity shows a tooltip:

```
+------------------+
| Pine Tree        |
| State: Clean     |
| Yield: 3 wood    |
| Tool: Axe        |
| [G]ather  [C]hop |
+------------------+
```

```
+------------------+
| Corrupted Wolf   |
| Health: 60%      |
| Weak: Silver     |
| Resist: Physical |
| Pack: 3 nearby   |
| [A]ttack [F]ire  |
+------------------+
```

```
+------------------+
| Thomas           |
| Role: Laborer    |
| Mood: Desperate  |
| Faith: 15%       |
| "He stares at    |
|  the blight."    |
+------------------+
```

### 3.4 Click-to-Build (Craftsman)

The Craftsman's blueprint system is designed for mouse:

1. **Click** "Build" button (or press `B`).
2. **Click** blueprint from list (Longhouse, Forge, etc.).
3. **Ghost outline** appears under cursor. Drag to position. Click to place.
4. **Material checklist** appears next to ghost. Green = have, Red = need.
5. **Click** "Confirm" or press `Enter`.
6. Construction begins. Pilgrims auto-assist.

### 3.5 Click-to-Rite (Priest)

The Priest's rites are designed for mouse:

1. **Right-click** ground.
2. Select "Perform Rite" from context menu.
3. **Radial menu** appears: Consecrate, Bless Flame, Circle of Salt...
4. **Click** rite.
5. **Radius selector** appears (1/3/5/7 tiles). Click size.
6. **Cost display** appears. Click "Begin."
7. Channeling begins. Progress bar fills. Vulnerable to interruption.

### 3.6 The Mini-Map as Navigation

The sidebar mini-map is clickable:
- **Click** a point on the mini-map: Player paths toward that world coordinate.
- **Right-click** a point: Set waypoint (`!` appears on main map).
- **Hover** over mini-map: Shows coordinate and terrain type.

---

## 4. Gamepad: Future Architecture

Gamepad is **not supported in the 12-week prototype.** But the architecture allows it later.

**Why not now:**
- Web gamepad API is inconsistent across browsers.
- ASCII grid navigation with an analog stick feels imprecise.
- The target audience (roguelike players, web browsers) primarily uses keyboard/mouse.

**Future implementation:**
- Left stick: Movement (8-directional).
- Right stick: Cursor mode (for examining, targeting).
- A button: Confirm/Interact/Attack.
- B button: Cancel/Back.
- X button: Gather/Use.
- Y button: Inventory.
- LB/RB: Tab through menus/targets.
- LT: Sprint.
- RT: Channel/Perform Rite.
- D-pad: Quick item slots.
- Start: Menu/Save.
- Select: Map.

**The protocol does not change.** Gamepad input is translated to the same `INPUT` messages as keyboard and mouse.

---

## 5. Input Translation Layer

All input methods converge to the same protocol commands:

```
Client Input -> Translation Layer -> Protocol -> Engine
```

**Keyboard:**
```
Key 'h' pressed -> INPUT move_west
Key 'g' pressed -> INPUT gather
Key 'B' pressed -> INPUT build_menu
```

**Mouse:**
```
Left-click tile (14, 22) -> INPUT move 14 22
Right-click tile (14, 22) -> INPUT context_menu 14 22
Left-click hostile (14, 22) -> INPUT attack 14 22
Scroll up -> INPUT zoom_in
```

**Gamepad (future):**
```
Left stick west -> INPUT move_west
A button -> INPUT confirm
```

**The engine never knows what input device was used.** It only receives `INPUT` commands. This means:
- Adding new input methods requires only client-side changes.
- The engine logic is device-agnostic.
- Replay/spectator mode works regardless of original input method.

---

## 6. Accessibility Considerations

### 6.1 Rebindable Keys

All keys are rebindable via a settings menu. The configuration is stored in `localStorage`:

```json
{
  "move_north": "k",
  "move_south": "j",
  "move_west": "h",
  "move_east": "l",
  "gather": "g",
  "build": "B",
  "inventory": "i",
  "confirm": "Enter",
  "cancel": "Escape"
}
```

### 6.2 One-Handed Mode

A preset keymap for players who can only use one hand:
- Movement: Arrow keys (with Shift for diagonal)
- Actions: Number row (`1` = gather, `2` = attack, `3` = build, etc.)
- Menus: Function keys (`F1` = inventory, `F2` = map, etc.)

### 6.3 Screen Reader Support

The web client uses semantic HTML and ARIA labels for screen readers:
- The canvas has `aria-live="polite"` regions for messages.
- The message log is a real `<div>` with text content, not just canvas rendering.
- Status bars are real `<progress>` elements.
- The sidebar is real HTML, not canvas.

This means screen readers can announce:
```
"You are hungry. The blight creeps. A wolf howls nearby."
"Faith: 80 percent. Warmth: 60 percent."
"Corrupted Wolf, 3 tiles west."
```

### 6.4 Colorblind Mode

A toggle that changes the color palette:
- Blight: Purple -> Striped pattern (horizontal lines)
- Holy Ground: Gold -> Striped pattern (vertical lines)
- Hostiles: Red -> Bold + underline
- Water: Cyan -> Wavy underline

The client renders these patterns using CSS/Canvas patterns, not just color.

---

## 7. UI Implications

### 7.1 The Bottom Bar

The bottom bar is the primary input feedback area:

```
+--------------------------------------------------------------------------------------+
| > build wall                    [TAB:Map]  [Z]oom  [V]iew  [?]Help  [Mouse: ON]    |
+--------------------------------------------------------------------------------------+
```

When mouse hovers over a tile:
```
+--------------------------------------------------------------------------------------+
| Pine tree (clean)  [G]ather  [X]Examine  [C]hop  [Click]Select  [R-Click]Menu      |
+--------------------------------------------------------------------------------------+
```

### 7.2 The Radial Menu (Right-Click)

Right-clicking opens a radial menu for quick actions:

```
        [Examine]
            |
    [Gather]---[Move Here]
            |
        [Attack]
            |
        [Build]
```

This appears at the cursor location and disappears after selection or clicking elsewhere.

### 7.3 The Action Bar

A persistent action bar at the bottom (optional, toggleable):

```
+--------------------------------------------------------------------------------------+
| [Move] [Gather] [Attack] [Build] [Rite] [Craft] [Inventory] [Map] [Help]            |
+--------------------------------------------------------------------------------------+
```

Each button shows its keyboard shortcut on hover. Clicking performs the action. This is for pure mouse players who want toolbar convenience.

---

## 8. Summary

| Input | Priority | Completeness | Target Audience |
|-------|----------|--------------|-----------------|
| **Keyboard** | Primary | 100% | Roguelike veterans, speedrunners, accessibility (one-handed mode) |
| **Mouse** | Secondary | 100% | Casual players, web browsers, new players, discovery |
| **Gamepad** | Future | 0% (prototype) | Console ports, couch play, future expansion |

| Feature | Keyboard | Mouse | Notes |
|---------|----------|-------|-------|
| Movement | hjklyubn + numpad + arrows | Click to pathfind | Both support 8-directional |
| Combat | `a` attack, `f` fire, `Tab` target | Click hostile, right-click for examine | Mouse shows weakness tooltip |
| Building | `B` blueprint, `b` freeform | Click build button, drag ghost, click confirm | Mouse is superior for placement |
| Rites | `R` then select | Right-click ground, radial menu | Mouse is superior for radius selection |
| Inventory | `i` then navigate | Click inventory button, drag items | Mouse supports drag-and-drop |
| Gathering | `g` | Click resource | Both single-action |
| Examine | `x` then move cursor | Hover | Mouse is superior for quick examination |
| Map | `m` | Click mini-map | Mouse supports click-to-navigate |

**The golden rule:** No player should ever think "I need a keyboard for this" or "I need a mouse for this." Both are complete. Both are valid. The game adapts to the player, not the other way around.

---

Document Version 1.0
The Wilds of Canaan - Input & Control Design Document
