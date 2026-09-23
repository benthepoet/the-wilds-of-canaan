# The Wilds of Canaan
## Audio & Sound Design Document

---

## 1. Philosophy

Sound in The Wilds of Canaan is not decoration. It is **information.** The player should be able to close their eyes and still know: where they are, what season it is, what dangers approach, and whether their settlement is thriving or dying.

The audio design follows three principles:
- **Diegetic first.** Every sound originates from something in the world. Wind, fire, footsteps, chanting. No abstract "game sounds."
- **Silence is a sound.** The absence of ambient noise is as meaningful as its presence. A silent forest is wrong. A silent settlement is doomed.
- **The player is not the center.** Sounds happen whether the player is there or not. Wolves howl in the distance. Pilgrims pray at night. The blight does not announce itself.

---

## 2. The Audio Engine

### 2.1 Web Audio API

The browser client uses the **Web Audio API** (not `<audio>` tags) for:
- Low-latency playback
- Dynamic mixing (ambient + SFX + music layers)
- Spatial audio (3D positioning for off-screen events)
- Procedural generation (wind, fire, water)

```javascript
const audioCtx = new AudioContext();

// Master gain -> three sub-mixers
const masterGain = audioCtx.createGain();
const ambientGain = audioCtx.createGain();   // Wind, water, forest
const sfxGain = audioCtx.createGain();       // Footsteps, combat, building
const musicGain = audioCtx.createGain();     // Chanting, seasonal themes

masterGain.connect(audioCtx.destination);
ambientGain.connect(masterGain);
sfxGain.connect(masterGain);
musicGain.connect(masterGain);

// Volume sliders (0.0 - 1.0)
ambientGain.gain.value = 0.6;
sfxGain.gain.value = 0.8;
musicGain.gain.value = 0.4;
```

### 2.2 Audio File Strategy

| Category | Format | Size Budget | Notes |
|----------|--------|-------------|-------|
| **Ambient loops** | Ogg Vorbis | 2-5MB total | Long loops (30-60s), cross-faded |
| **SFX one-shots** | Ogg Vorbis | 1-2MB total | Short (0.5-3s), multiple variants |
| **Procedural audio** | Synthesized | 0 bytes | Wind, fire, water generated in real-time |
| **Music stings** | Ogg Vorbis | 500KB total | Short thematic phrases, not full songs |

**Total audio budget: ~5MB.** Small enough for fast web loading, large enough for variety.

---

## 3. Ambient Soundscapes

### 3.1 Seasonal Ambients

Each season has a base ambient layer that plays continuously:

| Season | Base Sound | Variations |
|--------|-----------|------------|
| **Spring** | Light wind, distant bird calls, thawing ice (crackling) | Rain showers, morning fog (dampened everything) |
| **Summer** | Strong wind, dense insect drone, leaf rustle | Thunderstorms (distant rumble), hot midday (cicadas) |
| **Autumn** | Dry wind, leaf crunch, crow caws | Cold snap (sharp wind), harvest (distant chopping) |
| **Winter** | Howling wind, creaking trees, snow crunch | Blizzard (overwhelming wind), ice crack (sharp, sudden) |

**Implementation:**
- Base ambient: 60-second loop, cross-faded with seasonal transition (2-second fade).
- Variations: Triggered by weather state. Fade in over 5 seconds, fade out when weather changes.
- Volume: 0.3-0.6 (always present but not overwhelming).

### 3.2 Regional Ambients

Layered on top of seasonal ambient based on player location:

| Region | Layer | Notes |
|--------|-------|-------|
| **The Shallows** | Waves, seagulls, ship creaking (distant) | Louder near water. Muted by forest. |
| **The Black Pines** | Dense wind (muffled by trees), twig snap, owl hoot | Oppressive. Limits visibility of distant sounds. |
| **The Frozen Straits** | Ice groaning, wind across flat ice, silence (no wildlife) | The silence is the sound. Wrong. |
| **The Mire** | Bubbling mud, insect swarm, distant splash | Unhealthy. Raises anxiety without the player knowing why. |
| **The Bluffs** | Screaming wind, rockfall (distant), nothing else | Highest altitude = loudest wind, no shelter. |

**Implementation:**
- Regional layer: 30-second loop, volume 0.2-0.4.
- Cross-fade between regions over 3 seconds as player moves.
- The Frozen Straits silence: not "no sound," but "no animal sound." Only wind and ice. This is detectable.

### 3.3 Time-of-Day Ambients

| Time | Modifier |
|------|----------|
| **Dawn** | Birds begin. Wind picks up. Settlement sounds start (pilgrims waking). |
| **Day** | Full ambient. Wildlife active. Construction sounds (if pilgrims working). |
| **Dusk** | Birds stop. Wind drops. Insects start. Pilgrims return to shelter. |
| **Night** | Owls, wolves (distant), wind only. Settlement: chanting or silence. |
| **Blood Moon** | All ambient drops to 20% volume. Replaced by low drone (see below). |

---

## 4. Sound Effects (SFX)

### 4.1 Movement

| Action | Sound | Notes |
|--------|-------|-------|
| **Footstep (grass)** | Soft crunch | 3 variants, random selection |
| **Footstep (snow)** | Sharp crunch | 3 variants. Louder. Alerts nearby hostiles. |
| **Footstep (ice)** | Hollow thud | 2 variants. Each step has 10% chance of "crack" sub-sound. |
| **Footstep (holy ground)** | Muted, almost silent | Consecrated earth absorbs sound. |
| **Sprint** | Heavy breath + louder footsteps | Stamina-dependent. Breathing intensifies as Stamina drops. |
| **Swim** | Splash, gasp | Only in water tiles. Drowning: choking sounds. |

### 4.2 Gathering & Crafting

| Action | Sound | Notes |
|--------|-------|-------|
| **Chop wood** | Axe impact + wood crack | 3 variants. Rhythm: chop-chop-crack (tree falls). |
| **Mine stone** | Pick impact + stone chip | 2 variants. Dull, heavy. |
| **Gather herbs** | Leaf rustle, snap | Soft. 2 variants. |
| **Butcher** | Wet slice, bone crack | Unpleasant. Pilgrims nearby lose Mood. |
| **Build (framed)** | Hammer nail, wood creak | Rhythmic. Pilgrims assist = overlapping hammers. |
| **Build (complete)** | Final nail, structure settle | Satisfying thud. |
| **Craft (forge)** | Hammer on metal, hiss of steam | Only at forge. Distinctive. |
| **Drop item** | Thud (wood/stone), clink (metal), splash (water) | Material-dependent. |

### 4.3 Combat

| Action | Sound | Notes |
|--------|-------|-------|
| **Melee hit (flesh)** | Wet thud, grunt | 3 variants. |
| **Melee hit (armor)** | Dull clang | 2 variants. |
| **Melee miss** | Whoosh, stumble | 2 variants. |
| **Bow fire** | String twang, arrow whistle | Arrow whistle continues until impact. |
| **Arrow impact** | Thud (flesh), clink (armor), thunk (wood) | Material-dependent. |
| **Trap trigger** | Snap, crash, scream | Wolf trap: snap + yelp. Pit trap: crash + silence. |
| **Death (player)** | Final breath, body fall | No music sting. Just silence. Then: wind returns. |
| **Death (hostile)** | Yelp, gurgle, collapse | Beast: yelp. Demon: dissolving hiss. Undead: bone clatter. |

### 4.4 Priest Rites

| Rite | Sound | Notes |
|------|-------|-------|
| **Consecrate (start)** | Low hum, wind drops | All ambient fades to 30%. |
| **Consecrate (channeling)** | Chanting (Latin-like gibbering), bell toll (distant) | 3 voice variants. Overlaps if multiple acolytes assist. |
| **Consecrate (complete)** | Bell toll (close), wind returns, gold "shimmer" sound | Satisfying. Ambient returns to 100%. |
| **Banishment** | Shout, thunderclap, demon scream | Loud. Stuns ambient for 2 seconds. |
| **Bless weapon** | Metal ring, whisper | Short. 2 seconds. |
| **Circle of Salt** | Salt pour, whisper | Soft. The circle "hums" while active. |
| **Last Rites** | Whispered prayer, body settle, silence | Solemn. No other sounds for 3 seconds. |

### 4.5 Blight & Corruption

| Event | Sound | Notes |
|-------|-------|-------|
| **Blight spread (normal)** | Faint hiss, like steam | Barely audible. You notice it when it stops. |
| **Blight surge** | Loud hiss, ground crack, distant scream | Alert sound. All ambient drops. |
| **Blight tile (stepping on)** | Squelch, faint whisper | Corruption gain. |
| **Corruption (player, low)** | Faint whisper, like wind through trees | Barely audible. |
| **Corruption (player, high)** | Clear whispering, your name | Distinct voices. "Thomas... Thomas..." |
| **Corruption (100)** | Scream, silence, then ambient returns | You become a Revenant. The scream is yours. |

### 4.6 Settlement & Pilgrims

| Event | Sound | Notes |
|-------|-------|-------|
| **Pilgrim rescued** | Weak cough, sob, "Thank you" | 3 voice variants (male, female, child). |
| **Pilgrim working** | Hammer, chop, hum | Ambient. Not foreground. |
| **Pilgrim praying** | Whispered prayer, chant | 2-3 pilgrims = overlapping whispers (comforting). 5+ = choir-like. |
| **Pilgrim despair** | Sobbing, silence, then: "I cannot" | One voice. Stops all other pilgrim sounds for 5 seconds. |
| **Pilgrim suicide** | Rope creak, snap, silence | No scream. Just the structure settling. Then: wind. |
| **Mood shift (Hopeful)** | Chanting intensifies, fire crackle louder | Subtle. You feel it before you notice it. |
| **Mood shift (Doomed)** | Chanting stops. Wind only. Then: a single sob. | The silence is the message. |

---

## 5. Music

### 5.1 Philosophy: No Traditional Music

There is no soundtrack in the traditional sense. No orchestral score, no combat music, no victory fanfare. The "music" of Canaan is:
- **Chanting** (pilgrims, the Priest)
- **Wind** (seasonal, regional)
- **Silence** (the most important)

This preserves the ASCII aesthetic: the game is sparse, and your imagination fills the gaps.

### 5.2 Musical Elements

| Element | Trigger | Description |
|---------|---------|-------------|
| **Chapel chant** | 2+ pilgrims praying at altar | Gregorian-like drone. 30-second loop. Fades in/out based on player proximity. |
| **Acolyte solo** | Single pilgrim praying | Single voice. Melancholy. Unsettling in isolation. |
| **The Drowned Choir** | Manifestation 1 active | Dissonant choral drone. Underwater-muffled. Not musical — it is the enemy singing. |
| **The Hollow Stag** | Manifestation 2 active | Horn-like drone, like a broken hunting horn. Distant, then closer. |
| **The Burning Eye** | Manifestation 5 active | Single sustained organ note. Low. It does not stop. It does not change. It is always there. |
| **Victory (Sanctuary)** | Cathedral consecrated | Full choir. 10 seconds. Then: silence, then wind returns. |
| **Defeat** | Death | No music. Wind only. Then: menu appears. |

### 5.3 The Blood Moon

During a Blood Moon, all ambient drops to 20% and a **low drone** (40Hz sine wave, barely audible) plays continuously. This is not music. It is physical discomfort. Players should feel it in their chest before they hear it.

---

## 6. Spatial Audio

### 6.1 Off-Screen Events

Events outside the viewport use spatial audio to convey direction and distance:

```javascript
// Wolf howl from northeast, 30 tiles away
const panner = audioCtx.createPanner();
panner.positionX.value = 20;   // northeast
panner.positionY.value = 0;
panner.positionZ.value = -30;  // distance (negative = behind listener)
panner.connect(masterGain);

// Volume attenuated by distance
const distance = Math.sqrt(20*20 + 30*30);
const volume = Math.max(0, 1 - distance / 50);  // audible up to 50 tiles
howlSource.gain.value = volume;
```

| Event | Audible Range | Directional? |
|-------|--------------|--------------|
| **Wolf howl** | 40 tiles | Yes (pan left/right) |
| **Blight surge** | 60 tiles | No (omnidirectional) |
| **Pilgrim scream** | 20 tiles | Yes |
| **Manifestation spawn** | 80 tiles | No (omnidirectional, all ambient drops) |
| **Fire/brazier** | 15 tiles | Yes |
| **Running water** | 25 tiles | Yes |

### 6.2 The Stereo Field

- **Left-heavy:** Wind from the west. Wolves to the west. Blight approaching from the west.
- **Right-heavy:** Same, but east.
- **Center, close:** Player actions, immediate threats.
- **Center, distant:** Manifestations, blight surges, settlement events.

Headphones are recommended but not required. The stereo field works on speakers but is less precise.

---

## 7. Audio States

The audio engine maintains a state machine that blends layers dynamically:

```
[Seasonal Ambient] + [Regional Ambient] + [Time Ambient]
        +
[Settlement Sounds] (if near base)
        +
[SFX] (one-shots, spatial)
        +
[Music] (chanting, Manifestation drones)
        =
[Master Mix]
```

**State transitions:**
- Entering blight: Ambient fades to 50%, hiss layer fades in.
- Entering holy ground: Ambient fades to 30%, hum layer fades in.
- Night falls: Ambient cross-fades to night variant over 10 seconds.
- Blood Moon: All ambient drops to 20%, drone fades in over 5 seconds.
- Manifestation spawn: All ambient drops to 10%, Manifestation sound fades in.
- Death: All sounds fade to silence over 3 seconds.

---

## 8. Accessibility

### 8.1 Visual Audio Cues

For deaf/hard-of-hearing players:

| Sound | Visual Equivalent |
|-------|-------------------|
| Wolf howl (distant) | `!` icon at screen edge, pulsing |
| Blight surge | Screen border pulses purple |
| Pilgrim scream | `!` icon at pilgrim location |
| Manifestation spawn | Screen shake + red border |
| Fire/brazier | Subtle orange glow at bottom of screen |
| Running water | Cyan ripple effect at screen edge |
| Priest chanting | Gold particles rising from altar |

### 8.2 Subtitles

Full subtitle system:
```
[wolf howls in the distance]
[blight surges — the ground cracks]
[Thomas sobs quietly]
[The brazier crackles]
[wind howls]
```

Subtitles include direction indicators:
```
[wolf howls — northeast]
[water flows — west]
```

### 8.3 Volume Controls

| Slider | Range | Default |
|--------|-------|---------|
| Master | 0-100% | 80% |
| Ambient | 0-100% | 60% |
| SFX | 0-100% | 80% |
| Music/Chanting | 0-100% | 40% |
| UI Sounds | 0-100% | 50% |

---

## 9. Technical Implementation

### 9.1 Audio File Loading

```javascript
// Preload critical sounds
const criticalSounds = [
    'ambient_wind_spring', 'ambient_wind_winter',
    'sfx_footstep_grass_1', 'sfx_footstep_grass_2', 'sfx_footstep_grass_3',
    'sfx_chop_wood', 'sfx_hammer_stone',
    'sfx_consecrate_complete', 'sfx_blight_surge',
    'voice_pilgrim_male_1', 'voice_pilgrim_female_1'
];

// Load on game start
const audioBuffers = {};
for (const name of criticalSounds) {
    const response = await fetch(`audio/${name}.ogg`);
    const arrayBuffer = await response.arrayBuffer();
    audioBuffers[name] = await audioCtx.decodeAudioData(arrayBuffer);
}

// Total: ~3MB of critical audio. Loads in < 2 seconds on 3G.
```

### 9.2 Procedural Audio

Wind, fire, and water are synthesized in real-time (no file loading):

```javascript
// Wind: filtered white noise
function createWindNode(intensity) {
    const bufferSize = audioCtx.sampleRate * 2;
    const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
    }

    const noise = audioCtx.createBufferSource();
    noise.buffer = buffer;
    noise.loop = true;

    const filter = audioCtx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.value = 200 + intensity * 400;

    noise.connect(filter);
    return filter;
}
```

### 9.3 Protocol Integration

The audio engine listens to the same protocol lines as the renderer:

```javascript
function handleProtocolLine(line) {
    if (line.startsWith('DRAW')) {
        const [, x, y, tile, state] = line.split(' ');
        if (tile === 'water' && isAdjacent(player.x, player.y, x, y)) {
            playAmbient('water_nearby', 0.3);
        }
    }

    if (line.startsWith('MSG')) {
        const msg = line.substring(4);
        if (msg.includes('wolf')) playSpatialSfx('wolf_howl', directionOfWolf);
        if (msg.includes('blight surges')) playSfx('blight_surge');
        if (msg.includes('consecrated')) playSfx('consecrate_complete');
    }

    if (line.startsWith('STATUS')) {
        const stats = parseStatus(line);
        if (stats.season !== currentSeason) {
            crossfadeAmbient(`wind_${stats.season}`, 2000);
        }
    }
}
```

---

## 10. Summary

| Category | Count | Size | Priority |
|----------|-------|------|----------|
| **Ambient loops** | 12 (4 seasons x 3 regions) | ~2MB | Critical |
| **SFX one-shots** | ~40 | ~1MB | Critical |
| **Voice lines** | ~20 (pilgrim events) | ~500KB | High |
| **Music stings** | 8 (Manifestations + victories) | ~500KB | High |
| **Procedural audio** | 3 (wind, fire, water) | 0 bytes | Critical |
| **Total** | ~83 sounds | ~4MB | — |

| Feature | Implementation | Notes |
|---------|---------------|-------|
| **Web Audio API** | Native browser | No libraries needed |
| **Spatial audio** | PannerNode | Directional off-screen events |
| **Dynamic mixing** | GainNode graph | Seasonal + regional + SFX + music layers |
| **Procedural audio** | Synthesized buffers | Wind, fire, water = infinite variation, zero file size |
| **Accessibility** | Visual cues + subtitles | Deaf/hard-of-hearing support |
| **Volume controls** | 5 sliders | Master, ambient, SFX, music, UI |

The audio of Canaan is not heard. It is **felt.** The wind is cold. The blight is wrong. The chanting is the only warmth in a dark world.

---

Document Version 1.0
The Wilds of Canaan - Audio & Sound Design Document
