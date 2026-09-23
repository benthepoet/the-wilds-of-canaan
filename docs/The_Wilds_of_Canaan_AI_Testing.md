# The Wilds of Canaan
## AI & Automated Testing Document

---

## 1. Philosophy

The text protocol is not merely a rendering layer. It is a **complete, stateless interface** between the game engine and any consumer — human, machine, or agent. Because the engine accepts text commands and emits text descriptions, an AI can play The Wilds of Canaan without a browser, without a screen, and without human-like perception. It parses. It decides. It acts.

This is not an afterthought. It is a **first-class feature** of the architecture.

---

## 2. The Protocol as an AI Interface

### 2.1 The Observation Space

Every frame, the engine emits a complete description of the visible world:

```
DRAW 14 22 forest clean dark_green black 0
DRAW 15 22 forest blight_3 dark_purple black 1
DRAW 16 22 holy_ground bright gold black 2
DRAW 10 5 player none white black 0
DRAW 11 5 wolf wounded dark_red black 0
STATUS Faith:80 Warmth:60 Hunger:40 Corrupt:15 Blight:20
MSG A wolf howls nearby.
MSG The blight creeps.
FLUSH
```

An AI agent parses these lines into a structured world model:

```typescript
interface WorldState {
    tiles: Map<string, Tile>;        // key: "x,y", value: terrain + state
    entities: Map<string, Entity>;   // creatures, items, structures
    player: PlayerStats;             // Faith, Warmth, Hunger, etc.
    messages: string[];              // Recent events
    tick: number;                    // Current game tick
}
```

This is **superior to pixel-based AI** (computer vision, OCR) because:
- **No ambiguity.** A tile is `forest:clean` or `forest:blighted`. There is no guessing.
- **No hidden state.** The protocol reveals exactly what the player would see. No fog-of-war cheating, but also no missed details.
- **No rendering cost.** The AI does not need a GPU, a browser, or a Canvas. It parses strings.
- **Deterministic.** Given the same seed and the same inputs, the output is identical. Reproducible tests.

### 2.2 The Action Space

The AI sends the same commands a human player sends:

```
INPUT move_east
INPUT move_northeast
INPUT attack
INPUT gather
INPUT build wall 14 8 stone
INPUT rite consecrate 16 10 3
INPUT craft silver_mace
INPUT eat venison
INPUT equip wool_cloak
INPUT wait
```

Every action is a single text line. There are no mouse coordinates, no click timings, no gesture recognition. The action space is discrete, finite, and unambiguous.

### 2.3 The Decision Loop

```
+-------------+     protocol lines      +-------------+
|   ENGINE    | ----------------------> |  AI AGENT   |
|  (headless) |                         |  (parser +  |
+-------------+                         |   decider)  |
      ^                                 +-------------+
      |                                       |
      | INPUT command                         | decide()
      |                                       v
+-------------+                         +-------------+
|   WORLD     | <---------------------- |   ACTION    |
|   STATE     |    apply action         |   OUTPUT    |
+-------------+                         +-------------+
```

The loop is:
1. **Observe:** Parse the latest protocol frame into a world model.
2. **Decide:** Run a policy (heuristic, search tree, neural network) to select an action.
3. **Act:** Send the action as an `INPUT` line.
4. **Repeat.**

---

## 3. Headless Mode

### 3.1 What Is Headless Mode?

Headless mode runs the engine without any rendering, without any Web Worker, and without any browser. It reads commands from stdin and writes protocol lines to stdout.

**Use cases:**
- Automated testing (CI/CD pipelines)
- Balance tuning (run thousands of games)
- RL training (agents play millions of episodes)
- Bug finding (fuzzing, property-based testing)
- Bot play (AI opponents, tutorial guides)

### 3.2 Headless in the Prototype (TypeScript)

Since the prototype engine is TypeScript, headless mode runs under Node.js:

```typescript
// test/headless.ts
import { Engine } from '../src/engine';

const engine = new Engine({
    seed: '7f3a9c',
    headless: true,
    vocation: 'priest'
});

// Run a simulation
for (let tick = 0; tick < 1000; tick++) {
    const action = decideAction(engine.getState());
    engine.input(action);
    const lines = engine.flush();

    // Assert invariants
    if (engine.player.health < 0) {
        console.log(`Died at tick ${tick}: ${engine.chronicle.lastEntry}`);
        break;
    }

    if (engine.day > 30 && engine.season !== 'winter') {
        throw new Error('Season transition bug: Day 30 should be winter');
    }
}
```

Run it:
```bash
npx ts-node test/headless.ts --seed 7f3a9c --vocation priest --ticks 1000
```

### 3.3 Headless in Production (Go)

The Go engine binary supports headless mode natively:

```bash
# Build the headless binary
go build -o canaan-headless cmd/headless/main.go

# Run a single simulation
./canaan-headless --seed 7f3a9c --vocation woodsman --ticks 5000 --output json

# Run a batch of 1000 games
./canaan-headless --batch 1000 --vocations priest,woodsman,craftsman --output csv
```

**Output formats:**
- `json`: Full protocol log (for replay, debugging)
- `csv`: Summary statistics (seed, vocation, days survived, cause of death, Manifestations defeated)
- `null`: No output, just exit code (for CI speed)

### 3.4 The Test Harness

A Python test harness for the Go binary:

```python
import subprocess
import json

class CanaanHarness:
    def __init__(self, seed, vocation):
        self.proc = subprocess.Popen(
            ['./canaan-headless', '--seed', seed, '--vocation', vocation],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.state = {}

    def act(self, command):
        self.proc.stdin.write(f"INPUT {command}\n")
        self.proc.stdin.flush()

        lines = []
        while True:
            line = self.proc.stdout.readline().strip()
            if line == 'FLUSH':
                break
            lines.append(line)

        return self._parse(lines)

    def _parse(self, lines):
        for line in lines:
            if line.startswith('DRAW'):
                _, x, y, tile, state, fg, bg, variant = line.split()
                self.state[f"{x},{y}"] = {
                    'tile': tile, 'state': state, 'variant': variant
                }
            elif line.startswith('STATUS'):
                # Parse stats
                pass
            elif line.startswith('MSG'):
                # Parse message
                pass
        return self.state

    def close(self):
        self.proc.stdin.write("QUIT\n")
        self.proc.wait()
```

---

## 4. Automated Testing Strategies

### 4.1 Unit Tests (Engine Components)

Test individual systems in isolation:

```typescript
// test/blight.test.ts
import { BlightSystem } from '../src/systems/blight';

describe('Blight spread', () => {
    test('clean tile becomes tainted when adjacent to blight', () => {
        const world = createTestWorld();
        world.setBlight(10, 10, 50);  // blighted center

        const blight = new BlightSystem(world);
        blight.tick();

        expect(world.getBlight(11, 10)).toBeGreaterThan(0);
        expect(world.getBlight(11, 10)).toBeLessThan(50);
    });

    test('holy ground blocks spread', () => {
        const world = createTestWorld();
        world.setBlight(10, 10, 80);
        world.setHoly(11, 10, true);

        const blight = new BlightSystem(world);
        blight.tick();

        expect(world.getBlight(11, 10)).toBe(0);
    });
});
```

### 4.2 Integration Tests (Full Game Loops)

Test complete scenarios:

```typescript
// test/survival.test.ts
describe('Winter survival', () => {
    test('player without food dies by Day 35', () => {
        const engine = new Engine({
            seed: 'winter_test',
            vocation: 'priest',
            headless: true
        });

        // Do nothing. Starve.
        for (let i = 0; i < 500; i++) {
            engine.input('wait');
            engine.tick();
        }

        expect(engine.player.health).toBe(0);
        expect(engine.chronicle.causeOfDeath).toContain('starvation');
    });

    test('player with 30 days of food survives winter', () => {
        const engine = new Engine({
            seed: 'winter_test',
            vocation: 'priest',
            headless: true,
            startingInventory: { jerky: 30 }
        });

        for (let i = 0; i < 500; i++) {
            engine.input('eat jerky');
            engine.input('wait');
            engine.tick();
        }

        expect(engine.player.health).toBeGreaterThan(0);
        expect(engine.day).toBeGreaterThan(40);
    });
});
```

### 4.3 Property-Based Tests (Fuzzing)

Generate random valid inputs and assert invariants:

```typescript
// test/invariants.test.ts
import fc from 'fast-check';

describe('Game invariants', () => {
    test('blight never exceeds 100', () => {
        fc.assert(fc.property(
            fc.string(),  // random seed
            fc.integer({min: 1, max: 100}),  // random ticks
            (seed, ticks) => {
                const engine = new Engine({ seed, headless: true });
                for (let i = 0; i < ticks; i++) {
                    engine.input(randomValidAction());
                    engine.tick();
                }

                for (const tile of engine.world.tiles) {
                    expect(tile.blight).toBeLessThanOrEqual(100);
                    expect(tile.blight).toBeGreaterThanOrEqual(0);
                }
            }
        ));
    });

    test('health never exceeds 100', () => {
        // ...
    });

    test('corruption 100 = death', () => {
        // ...
    });
});
```

### 4.4 Regression Tests (Seed-Locked)

Lock specific seeds to catch regressions:

```typescript
// test/regression.test.ts
describe('Seed 7f3a9c regression suite', () => {
    test('Day 14: blight should be at tile (20, 15)', () => {
        const engine = new Engine({ seed: '7f3a9c', headless: true });

        for (let i = 0; i < 14 * 100; i++) {  // 14 days * 100 ticks/day
            engine.input('wait');
            engine.tick();
        }

        expect(engine.world.getBlight(20, 15)).toBeGreaterThan(0);
    });

    test('Priest can consecrate starting area by Day 3', () => {
        const engine = new Engine({ seed: '7f3a9c', vocation: 'priest', headless: true });

        // Gather salt, gather water, perform rite
        engine.input('gather');
        engine.tick();
        // ... more actions

        expect(engine.world.isHoly(16, 10)).toBe(true);
    });
});
```

### 4.5 Performance Tests

```typescript
// test/performance.test.ts
describe('Performance benchmarks', () => {
    test('1000 ticks completes in < 1 second', () => {
        const engine = new Engine({ seed: 'perf_test', headless: true });

        const start = performance.now();
        for (let i = 0; i < 1000; i++) {
            engine.input('wait');
            engine.tick();
        }
        const elapsed = performance.now() - start;

        expect(elapsed).toBeLessThan(1000);
    });

    test('World gen (seed 7f3a9c) completes in < 500ms', () => {
        const start = performance.now();
        new Engine({ seed: '7f3a9c' });
        const elapsed = performance.now() - start;

        expect(elapsed).toBeLessThan(500);
    });
});
```

---

## 5. Reinforcement Learning

### 5.1 Why Canaan Is Good for RL

| Feature | Why It Helps RL |
|---------|----------------|
| **Discrete action space** | ~30 valid commands. No continuous control needed. |
| **Structured observations** | Protocol lines parse into a grid + stats. No CNN required. |
| **Clear reward signal** | +1 per day survived, -100 for death, +50 per Manifestation. |
| **Episodic** | Each run is an episode. Natural termination (death or victory). |
| **Deterministic** | Same seed + same actions = same outcome. Reproducible training. |
| **Fast** | Headless mode runs 1000+ ticks per second. Millions of episodes possible. |

### 5.2 Reward Function

```typescript
function calculateReward(state: WorldState, action: string, nextState: WorldState): number {
    let reward = 0;

    // Survival
    reward += 1;  // +1 per tick survived

    // Health
    const healthDelta = nextState.player.health - state.player.health;
    reward += healthDelta * 10;  // +10 per health gained, -10 per lost

    // Progress
    if (nextState.manifestationsDefeated > state.manifestationsDefeated) {
        reward += 50;
    }

    // Resources
    const foodDelta = nextState.player.food - state.player.food;
    reward += foodDelta * 5;

    // Penalties
    if (nextState.player.corruption > 50) {
        reward -= 5;  // Danger zone
    }

    // Death
    if (nextState.player.health <= 0) {
        reward -= 100;
    }

    return reward;
}
```

### 5.3 Observation Encoding

For a neural network, encode the world as tensors:

```typescript
function encodeObservation(state: WorldState): Float32Array {
    const width = 21;   // 10-tile radius around player
    const height = 21;
    const channels = 5; // terrain, blight, holy, entity, visibility

    const tensor = new Float32Array(width * height * channels);

    for (let dy = -10; dy <= 10; dy++) {
        for (let dx = -10; dx <= 10; dx++) {
            const x = state.player.x + dx;
            const y = state.player.y + dy;
            const tile = state.tiles.get(`${x},${y}`);

            const idx = ((dy + 10) * width + (dx + 10)) * channels;

            // Channel 0: terrain type (one-hot or enum)
            tensor[idx + 0] = tile ? terrainToNumber(tile.terrain) : 0;

            // Channel 1: blight level (0-1 normalized)
            tensor[idx + 1] = tile ? tile.blight / 100 : 0;

            // Channel 2: holy ground (0 or 1)
            tensor[idx + 2] = tile && tile.holy ? 1 : 0;

            // Channel 3: entity present (0 or 1)
            tensor[idx + 3] = state.entities.has(`${x},${y}`) ? 1 : 0;

            // Channel 4: visible (0 or 1)
            tensor[idx + 4] = tile && tile.visible ? 1 : 0;
        }
    }

    return tensor;
}
```

### 5.4 Training Pipeline

```python
# train.py
import gym
from stable_baselines3 import PPO

class CanaanEnv(gym.Env):
    def __init__(self, seed=None):
        self.engine = CanaanHeadless(seed=seed or random_seed())
        self.action_space = gym.spaces.Discrete(30)  # 30 valid commands
        self.observation_space = gym.spaces.Box(
            low=0, high=1,
            shape=(21, 21, 5),
            dtype=np.float32
        )

    def reset(self):
        self.engine = CanaanHeadless(seed=random_seed())
        return self._get_obs()

    def step(self, action):
        cmd = action_to_command(action)
        self.engine.input(cmd)
        self.engine.tick()

        obs = self._get_obs()
        reward = calculate_reward(self.engine.state)
        done = self.engine.player.health <= 0 or self.engine.victory
        info = {'days': self.engine.day, 'seed': self.engine.seed}

        return obs, reward, done, info

# Train
env = CanaanEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000_000)

# Evaluate
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=1000)
print(f"Mean reward: {mean_reward:.2f} +/- {std_reward:.2f}")
```

---

## 6. Balance Tuning with Data

### 6.1 The Balance Loop

```
1. Define hypothesis: "Winter is too easy."
2. Run 1000 simulations (all Vocations, random seeds).
3. Analyze: 80% of players survive winter. Target: 40%.
4. Adjust: Reduce Clean Spring frequency by 30%.
5. Re-run 1000 simulations.
6. Compare: Now 42% survive. Close enough.
```

### 6.2 Metrics to Track

| Metric | Collection Method | Target |
|--------|------------------|--------|
| **Mean survival days** | Batch headless runs | 20-30 days (first-time players) |
| **Win rate by Vocation** | Batch runs, grouped by Vocation | 30-40% Priest, 25-35% Woodsman, 35-45% Craftsman |
| **Most common death cause** | Chronicle analysis | Should vary by Vocation |
| **Mean time to first Chapel** | Event tracking | Day 5-8 |
| **Mean time to first Manifestation** | Event tracking | Day 15-25 |
| **Pilgrim survival rate** | Track rescued vs. died | 40-60% |
| **Resource scarcity index** | Count available vs. consumed | Should trend toward scarcity by Day 25 |

### 6.3 The Dashboard

A simple HTML dashboard generated from batch runs:

```
+----------------------------------------------------------+
| Canaan Balance Dashboard (10,000 runs)                   |
+----------------------------------------------------------+
|                                                          |
|  Survival Rate by Vocation                               |
|  Priest:    38%  [##############----]                    |
|  Woodsman:  31%  [###########-------]                    |
|  Craftsman: 42%  [################--]                    |
|                                                          |
|  Death Causes (all Vocations)                            |
|  Starvation:  35%                                        |
|  Wolves:      22%                                        |
|  Blight:      18%                                        |
|  Manifestation: 15%                                      |
|  Frozen:       7%                                        |
|  Other:        3%                                        |
|                                                          |
|  Mean Days Survived: 24.3 (+/- 8.1)                      |
|  Mean Food Stockpiled by Day 30: 12.4 days               |
|  Mean Blight Distance at Day 30: 8.2 tiles               |
|                                                          |
+----------------------------------------------------------+
```

---

## 7. Bot Play & Tutorial AI

### 7.1 The Tutorial Bot

A scripted AI that demonstrates optimal play for new players:

```typescript
// bot/tutorial.ts
class TutorialBot {
    async play(engine: Engine) {
        // Day 1-3: Gather basics
        await this.gatherWood(10);
        await this.gatherStone(5);
        await this.buildFirepit();

        // Day 4-7: Establish base
        await this.consecrateGround(3);
        await this.buildChapel();

        // Day 8-14: Prepare for winter
        await this.gatherFood(20);
        await this.buildSmokehouse();
        await this.craftWarmArmor();

        // Day 15+: Defeat Manifestation
        await this.prepareForDrownedChoir();
        await this.defeatManifestation();
    }
}
```

The bot runs in real-time in the browser, with the player watching. It explains each action via the message log: "The bot is gathering wood. You should too before winter."

### 7.2 The Ghost

A "ghost" of a previous player\'s run, replayed via their Chronicle:

```typescript
// Load Chronicle from seed
const chronicle = loadChronicle(seed);

// Replay actions
for (const entry of chronicle.actions) {
    await delay(entry.timestamp - prevTimestamp);
    engine.input(entry.command);

    // Render ghost player as translucent `@`
    renderGhost(entry.position);
}
```

Players can watch how others survived (or died) on the same seed. The ghost is not interactive — it is a teaching tool.

---

## 8. CI/CD Integration

### 8.1 GitHub Actions Workflow

```yaml
# .github/workflows/test.yml
name: Canaan Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Unit tests
        run: npm test

      - name: Integration tests
        run: npm run test:integration

      - name: Property-based tests
        run: npm run test:fuzz -- --runs 10000

      - name: Performance benchmarks
        run: npm run test:perf

      - name: Balance check
        run: npm run test:balance -- --runs 1000 --output dashboard.html

      - name: Upload dashboard
        uses: actions/upload-artifact@v3
        with:
          name: balance-dashboard
          path: dashboard.html
```

### 8.2 Pre-Commit Hooks

```bash
# .husky/pre-commit
npm run test:unit
npm run test:regression -- --seeds 7f3a9c,abc123,def456
```

Every commit runs the regression suite on locked seeds. If Day 14 of seed `7f3a9c` changes, the commit is blocked until manually reviewed.

---

## 9. Summary

| Capability | Method | Use Case |
|-----------|--------|----------|
| **Unit tests** | Jest/Vitest on engine components | Catch regressions in blight, combat, crafting |
| **Integration tests** | Full game loops in headless mode | Verify winter survival, Manifestation defeat |
| **Property tests** | fast-check fuzzing | Assert invariants (blight <= 100, health >= 0) |
| **Regression tests** | Seed-locked scenarios | Ensure specific seeds produce expected outcomes |
| **Performance tests** | Benchmark ticks/second | Catch slowdowns before they affect players |
| **RL training** | PPO on encoded observations | Discover optimal strategies, find exploits |
| **Balance tuning** | Batch simulations + metrics | Adjust scarcity, difficulty, Vocation parity |
| **Tutorial bot** | Scripted AI with explanations | Teach new players optimal early game |
| **Ghost replay** | Chronicle action replay | Show how others survived the same seed |

The text protocol makes all of this possible. The engine does not know if it is talking to a human, a test harness, or a neural network. It speaks the same language to all of them.

---

Document Version 1.0
The Wilds of Canaan - AI & Automated Testing Document
