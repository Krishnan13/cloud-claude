---
name: "cartoon-dialogue-video"
description: "Co-direct a short 2D cartoon with Shashi, built in code: any story series (the 'Yabuuu' series is one; new series welcome). Shashi's story arrives in any form (dialogue, plot notes, backdrop hints, characters implied); Claude turns it into a story sheet, then works in small modules (script, storyboard, voices, backdrops, characters, animatic, render, sound), each ending in a short decision card for Shashi. ElevenLabs voices and painted backdrops, characters drawn in code, film-style shots and acting, procedural sound. Use whenever Shashi shares a dialogue, skit, story or idea and wants a video, an animated scene, a cartoon, an episode, a new series, voices added to a scene, or a remake of an AI-generated (Gemini/Veo) video, even if they don't say 'animation' or 'Manim'. Works in cloud sessions and in Claude Code on Shashi's Windows laptop."
---

# Cartoon studio: Shashi and Claude co-direct

Shashi and Claude are **co-directors**. Work in small modules. Each module ends with a **decision card**: Claude brings 2-3 options, marks the recommended one, says why, and Shashi decides in a word. Never run from script to finished video in one go. Catch problems while they are cheap: on paper, on stills, in the animatic. Not after the full render.

Follow `working-with-shashi` and `shashi-global-rules` throughout (plain words, plan first, cheap helpers, honest checks, show before saving).

**This one file holds everything** (Shashi can update it with one tap). Parts:
- **A. Workflow:** modules and decision cards
- **B. Craft book:** how things look and move, for **every** story; read it before designing any shot
- **C. Series bibles:** one section per series
- **D. Templates:** story sheet, card, animatic, episode notebook
- **E. Code and setup**

Story and directing choices for one story live in that episode's `notebook.md` in the project. **They never become general rules here.**
Older copies of `references/*.md` or `series/*/bible.md` may sit in the skill folder: ignore them; this file wins.
Master copy of this skill: `cartoon-skill/cartoon-dialogue-video/` in Shashi's GitHub project.

---

# A. Workflow

## Who does what

- **Shashi:** the story, its human touch, and every ★ decision.
- **Opus (me): the director's legwork and opinion.** Story sheet, story beats, shot list, camera, acting, character design, backdrop prompts, checking every render. Coming up with engaging staging and animation is my main contribution, not just assembling parts. Bring a clear recommendation every time.
- **Command Code helper (DeepSeek 4.1 Flash; Shashi prefers fast mode for animation: `-m deepseek/deepseek-v4.1-flash-fast`):** drudgery with a precise spec, such as sound-effect scripts, mux/encode scripts and bulk edits. It is weak at drawing and acting: don't hand it characters or staging. Post the model plan and wait for OK before using it.
- **ElevenLabs connector:** voices (`eleven_v4`) and backdrops (`recraft-v4.1-flash`, ~48 credits each). Shashi is on the paid Starter plan.

## The modules (★ = decision card, wait for Shashi)

**0. Story sheet ★** Shashi's story can come in any form: dialogue, a paragraph, notes, a transcript. Sort it into four boxes (plot, characters, places, dialogue) and mark each item ✅ given / ❓ unclear / ➕ missing (template D1).
- ❓ → a one-word question with my best guess marked.
- ➕ → a labelled suggestion with a one-line reason.
- Plot sharpening → name the weak spot, offer 1-2 small fixes, plus **"leave as is"**.
- **Protect the writer's touch.** Shashi's words stay word for word. Suggestions stay visibly separate, never mixed into the text. Trim or reorder before adding. Any new line is written in that character's own voice. "Leave as is" is always an option.
- Find the twist: build-up (anticipation, greed, excitement), a held silence, the reveal, a deadpan beat, then the sting or ending.
- Output: the **locked script**. Every later module builds from it.

**1. Brief ★** Which series (or a new one)? Format (16:9 / 9:16)? Setting: make it specifically local (Mangaluru: loud colourful private buses, Mangalore-tile roofs, laterite walls, coconut palms…). Mood. For a new series, also draft its bible (template in C).

**2. Storyboard ★** A shot table (time, place, what moves, line or sound), **plus rough sketch frames**: one small image per shot, drawn in code (grey boxes for the set, simple figures, an arrow for camera movement), shown as one contact sheet. Pick each place *for the motion the shot needs* (B4).

**3. Voices ★** `creative_list_voices(languages=[...])`. Cast from the series bible; new characters get 2-3 candidate voices to choose from. Keep Shashi's words; fix pronunciation by respelling (ask how it should sound). No "…" inside a word (it makes a pause); drawn-out sounds = repeated vowels. Light emotion tags only. 2 takes when delivery matters; Shashi picks. Download promptly (links expire ~2 h).

**4. Backdrops ★** Prefix: "Flat 2D storybook vector illustration with clean bold dark outlines, background plate for an animated short, wide 16:9, no people, no readable text." (or the series' own prefix). State the viewpoint explicitly ("seen from the seat in front, looking straight at…", "flat SIDE VIEW elevation, no perspective"). 2 variations when the look matters. Measure where characters stand or sit on a grid before using a plate.

**5. Characters and style stills ★** A still frame for every new character, angle or set; Shashi reviews faces closely (eyes!). Iterate on stills: they are cheap. A few-second motion test for any new kind of movement.

**6. Animatic ★** The rough draft of the film (spec D3): real voices at real timing, real backdrops and camera framing, characters placed but without acting, low resolution, shot number and line burned in. Renders in about a minute. Question it answers: *does the story play well in time?* Fix pacing, pauses and shot order here.

**7. Acting pass ★** Acting as keyframes over the master clock (see E). Show a 6 fps preview plus stills of the key beats (the twist, reactions). Short card: "these beats, these expressions: OK?"

**8. Final render and sound (automatic, then checked)** Full render, procedural ambience and effects, mix, mux. Check honestly: 1 fps contact sheet (+ 2-4 fps around key beats) and look at it; measure `volumedetect` in voice vs ambience windows (voices ~15-20 dB above). Report what was checked and fixed.

**9. Review and lessons ★** Deliver with `SendUserFile` (display `attach`; previews can be muted). Join scenes with ffmpeg's concat *filter* (re-encode). In the cloud, remind Shashi the machine is wiped when idle and offer a zip. Then sort every correction Shashi made:
- how things **look or move** → Part B (all stories);
- cast, voice, style or gag of the **series** → that series' section in Part C;
- a **story or directing choice** → the episode notebook only.

Show the proposed additions. After OK: edit the master copy in the GitHub project, commit, and send Shashi the new SKILL.md with `SendUserFile` so they can tap "Update skill". Code changes cannot go through that button: tell Shashi when a zip upload is needed. Warn Shashi if this file passes about 500 lines.

## Decision cards: how to run them

- One card per module, fitting on one screen (template D2).
- Show, don't describe: images, contact sheets, audio takes, the animatic.
- Options with a ★ recommendation and a one-line reason each; say the cost (credits, time) when it differs.
- List "small calls I made myself" in a few lines, so Shashi can overrule any of them.
- Record each decision and its reason in the episode notebook as it is made.
- Going back is fine; say which later modules it affects.

## Project layout (per episode)

```
<series>/<epNN-short-name>/
  notebook.md      story sheet, locked script, every decision + reason
  voices/  backdrops/  stills/  animatic/  render/
  scene1.py ...    copied from assets/template/
```

---

# B. Craft book: how things look and move (all stories, all series)

General lessons on drawing, movement, camera and sound; most came from Shashi's feedback on Yabuuu episode 1. Add new lessons in the right section with the date and episode in brackets, e.g. "(Oct 2026, Yabuuu ep 2)".

## B1. Drawing in code

- **Boiling lines:** the drawing wobbles slightly 8 times a second (`ink.boil`). Use a smooth offset *field* (neighbouring points move together). Jittering points one by one tears shapes open and kills fills.
- **On twos:** characters change pose 12 times a second (`tc = floor(t*12)/12`); world motion (window lights, light sweeps, camera) runs every frame at 24 fps.
- **Outlines match the backdrops:** if the painted plates have dark outlines, the characters need the same outline colour and weight, or they look pasted on.
- Keep characters at a readable size; tiny distant figures merge into a blob.

## B2. Faces and eyes

- Big dark pupils with a highlight.
- The upper-eyelid line curves *up* like a real eye. A downward-dipping lid line reads as angry.
- Friendly arched brows, set well above the eyes.
- Default lid 0.1. Heavier lids only for acting: droop = disappointed or deadpan, lift = surprise.

## B3. Head turns (three-quarter view)

- Features slide toward the turn, the chin shifts, the nose pokes out on the turn side, only the back ear shows, more hair on the back of the head.
- The eye on the *turning side is the far eye*: slightly narrower and tucked behind the nose. (Getting this backwards made a character's eyes look wrong.)

## B4. Motion must fit the backdrop (flat paintings)

| backdrop viewpoint | believable motion |
|---|---|
| front-facing interior (e.g. bus seat from the front) | characters sit, turn, gesture; 2D push-ins and cuts; whole-frame shake for bumps; light bands sweeping; moving things only inside cut-out layers (lights behind redrawn window bars) |
| flat side elevation (wall or street seen side-on) | walking across the frame in profile; stops, looks, points |
| perspective lane toward camera | only walking *toward* camera with growing scale; avoid unless the shot needs it |
| facade / gate | crowds from behind, people entering from the side |
| interior seen through bars | push-in on the subject; bars drawn in front by code |

- Never walk characters "into" a perspective picture or swing the camera around a room.
- Anything that must move inside a painting is made as its own layer.
- Direction matters: when characters face the front of a vehicle, the street outside slides from the near end of the window to the far end.

## B5. Staging and camera (films, not stage plays)

- Characters who talk to each other **turn toward each other**. While one speaks, the listener looks at the speaker, not at the camera.
- Default conversation angle: from the front, waist-up two-shot; cut to single medium shots of the speaker and close-ups for reactions.
- Snap zoom (0.15 s) for a shock line.
- Show actions so they read instantly:
  - peeping into a window → **from inside the room**: faces rising slowly above the sill, fingers curled over it, eyes searching (backs of heads from outside were unreadable);
  - searching while walking → **side view**: looking over walls, peering into bushes, a hand shading the eyes.
- Comedy tools: a gag the other character doesn't notice, a daydream bubble, silence before a reveal, a slow deadpan turn.

## B6. Sound

- Voices on top, about 15-20 dB above the ambience.
- Ambience per place (vehicle hum + vibration, crickets, birds, crowd murmur).
- One effect per meaning (horn, brake hiss, bell, pothole thud, whoosh on a snap zoom, ka-ching for money).
- Silence for suspense. Footsteps only while walking.
- Two-pass loudnorm to −14 LUFS.

## B7. Working rhythm that saves rounds

Story sheet → storyboard sketches → stills → short motion test → animatic → acting preview at 6 fps → full render. Iterate on paper, stills and previews, never on full renders.

---

# C. Series bibles

Only what is special to each series. General look and movement rules are in Part B.

## C1. Yabuuu

Kannada comedy skits. Two friends get excited about something, it builds up, and the twist deflates it. Then Suresh says "ಯಬೂಊಊ".

**Episodes**

| # | title | length | notes |
|---|---|---|---|
| 1 | Madam Magu | 83.5 s | the reference episode; code in `assets/template/`, backdrops in Shashi's project zip |

**Cast and voices** (ElevenLabs, `eleven_v4`)

| character | voice | id | look (`ink.py` spec) |
|---|---|---|---|
| Ramesh | Bharadwaj – Expressive, Real & Chill Guy | 75K9CAd9ZbhCXsP4nMDk | `RAMESH`; tilak on the forehead |
| Suresh | Srivatsa – Casual & Natural Conversation | jtyEMdWULw6XHzgQFVCt | `SURESH` |
| older neighbour | Rajaratna P | Z1sgBQe4e9WquuP9yR3D | `NEIGHBOUR` |
| Madam (ep 1) | — | — | `MADAM` |

**Look: "living ink".** Big heads (about 1:3), bold dark outlines (#20140E), flat fills, simple bodies with four-finger hands. Boiling lines and characters on twos (B1).

**Places: Mangaluru.** Colourful private bus: deity photo + red bulb, tinsel, stickers, conductor's bag (Shashi rejected a clean modern bus as "San Francisco metro"). Mangalore-tile roofs, laterite walls, coconut palms. Props: "S.K. TEXTILES" shopping bag.

**The sting: "ಯಬೂಊಊ" (every episode)**
- At the twist the two friends slowly turn to each other.
- **Suresh** says the catchphrase from `sting_yabuu.mp3` (in this skill folder: `series/yabuuu/` or, in older installs, `assets/series/`; find it with `find <skill folder> -name sting_yabuu.mp3`). Light, puzzled-amused, quick start, long dragged "ಊ"; 2.3 s. Mouth moving, one brow up, small head tilt.
- **Then** the picture freezes, a slow push-in, colour drains (`hue=s=0.45`), whoosh, and `series_sfx.music_hit()` (plucked D-A-D + tabla "dhin").
- Reuse this exact recording and hit every episode.
- Rejected before: Ramesh's voice, slow or sober delivery, intense or pained delivery.

**Story shape (typical, not a rule):** build-up (anticipation, greed, excitement) → held silence → reveal → deadpan beat → sting. Each story decides its own details in its notebook.

## C2. New series template

Copy this as a new C-section and fill it in during Module 1 (Brief) with Shashi.

```
## C<n>. <Series name>
Idea: what kind of stories, language, audience, tone (1-2 lines).
Episodes: | # | title | length | notes |
Cast and voices: | character | voice | id | look (spec in code) |
Look: drawing style (reuse "living ink" from ink.py, or new: decide with style stills),
      outline colour, proportions, palette.
Places: usual settings and the local details that make them feel real.
Recurring elements: catchphrase, sting, opening/ending, running gags, music hit (or none).
```

---

# D. Templates

## D1. Story sheet (Module 0)

```
STORY SHEET: <working title>

What I understood (2-3 lines): ...

| box        | ✅ given by you          | ❓ unclear (my guess ★)          | ➕ missing (suggestion + why) |
|------------|--------------------------|----------------------------------|-------------------------------|
| Plot       | build-up, twist, ending  |                                  |                               |
| Characters | who, how they talk/look  |                                  |                               |
| Places     | backdrops                |                                  |                               |
| Dialogue   | lines as written         |                                  |                               |

Sharpening (optional):
  Weak spot: ...
  A) small fix ...   B) another fix ...   C) leave as is
```

- Quote Shashi's lines exactly. Never reword them in the sheet.
- Suggested new lines are shown separately, marked "SUGGESTED", each with a one-line reason, in that character's voice.
- Prefer trimming or reordering over adding. Every suggestion can be refused.

After approval, write the **locked script**: Shashi's lines plus only the accepted suggestions, with speaker, place and any stage note per line.

## D2. Decision card (end of every ★ module)

```
CARD <n>: <module>

Here it is: <image / contact sheet / audio / video attached>

Options:
  A ★ <option> (why, in one line)
  B   <option> (why)
  C   <option> (why)          cost if it differs: credits / time

Small calls I made myself (overrule any):
  - ...

Your call: A / B / C / other
```

Keep it to one screen. Show, don't describe. One question per card when possible.

## D3. Animatic spec (Module 6)

- Real voice takes placed at their real times; rough mix (voices + one ambience bed, no effects yet).
- Real backdrops and the planned camera framing and cuts.
- Characters placed in neutral poses, facing the right way; mouths move from `envelope.py`; no other acting.
- Burned-in text, top left: shot number and the line being spoken.
- `-ql --frame_rate 6`; about a minute to render.
- Ask on the card: pacing, pauses (especially before the twist), shot order, anything that drags or rushes.

## D4. Episode notebook (one per story, in the episode folder)

```
# <series> ep <n>: <title>

## Story sheet (approved <date>)
## Locked script
## Decisions
| module | decision | why | date |
|--------|----------|-----|------|
## Lessons proposed for Part B / Part C (Module 9)
```

Decisions here belong to this story. Only lessons about how things look or move go on to Part B.

---

# E. Code and setup

## Code (assets/template/)

Built for Yabuuu episode 1 ("Madam Magu", 83.5 s); the engine is reusable for any series. New series add their own character specs to `ink.py` (or a series file next to it).

| file | what it is |
|---|---|
| `ink.py` | the "living ink" drawing engine: `person(spec, pose, t, x, y, s)` front/seated/standing/back views, `person_side` profile walk, `puppy()`, `hand()`, boiling lines; Yabuuu specs RAMESH, SURESH, NEIGHBOUR, MADAM, `crowd_spec(i)` |
| `style_test.py` | backdrop mapping helpers + `window_layer()` (lights sliding behind bus window bars) and `light_sweep()` |
| `chars_test.py` | character sheet still (use when adding a character) |
| `scene1.py`, `scene2.py` | scene structure to copy: `LINES` voice timings, `key()`/`blink()` acting helpers, `SHOTS` list, `world(t)` rebuilt each frame, characters on twos (`tc = floor(t*12)/12`), the `get_moving_and_static_mobjects` override (keep it, or old frames ghost) |
| `sound_scene1.py`, `sound_scene2.py`, `series_sfx.py`, `sfx.py` | procedural ambience/effects, voice placement, two-pass loudnorm (LRA=25, linear) |
| `envelope.py` | mouth opening from each voice mp3 (RMS per frame) |
| `mux_scene*.sh` | soundtrack + picture (+ end-of-scene desaturation) |

Render: `manim -qm --frame_rate 24 --disable_caching scene2.py Scene2`. Preview: `-ql --frame_rate 6` (~1 min). Animatic: same scene file with acting switched off (`ACTING = False`: neutral poses, mouths from `envelope.py` only) at `-ql --frame_rate 6`. Backdrops live in the episode's `backdrops/` folder (not in this skill); episode 1's are in Shashi's project zip.

## Setup

**Cloud (Linux):** `python3 -m venv .venv && .venv/bin/pip install manim numpy pillow` (system pip fails on manim's `srt`; may need `apt-get install -y libpango1.0-dev pkg-config`). Helper: `bash /usr/local/bin/delegate.sh -m deepseek/deepseek-v4.1-flash-fast -d <project> "<task>"`. Run your own scripts without `python -I` (it hides the project folder from imports).

**Laptop (Windows, Claude Code):** work in `E:\aashu channel\<episode>` (a git folder). Install once: `winget install Gyan.FFmpeg`, Python 3.12+, then in the project `python -m venv .venv` and `.venv\Scripts\pip install manim numpy pillow`. Run `.sh` scripts from Git Bash (`bash mux_scene1.sh`). Helper: `bash /c/Users/Krishnanvp/bin/delegate.sh -m deepseek/deepseek-v4.1-flash-fast -d . "<task>"`. If the DejaVu Sans font is missing, Manim falls back to a default font for the bag text and ₹: fine, or set `font="Arial"` in `ink.py`. The ElevenLabs connector works the same; on the laptop there is no proxy, so no "unusual activity" blocks.

## Known limits (iterate with Shashi; don't fix unasked)

- Heads in profile are a strong three-quarter view on a side body (accepted).
- Crowds are back views only; no faces in crowds yet.
- Character art is simple flat cut-out; acting and staging carry the comedy.
- `ACTING = False` switch for the animatic is new: add it to the scene file when first used.
