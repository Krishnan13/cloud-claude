---
name: "cartoon-dialogue-video"
description: "Co-direct a short 2D cartoon with Shashi, built in code: any story series (the 'Yabuuu' series is one; new series welcome). Shashi's story arrives in any form (dialogue, plot notes, backdrop hints, characters implied); Claude turns it into a story sheet, then works in small modules (script, storyboard, voices, backdrops, characters, animatic, render, sound), each ending in a short decision card for Shashi. ElevenLabs voices and painted backdrops, characters drawn in code, film-style shots and acting, procedural sound. Use whenever Shashi shares a dialogue, skit, story or idea and wants a video, an animated scene, a cartoon, an episode, a new series, voices added to a scene, or a remake of an AI-generated (Gemini/Veo) video, even if they don't say 'animation' or 'Manim'. Works in cloud sessions and in Claude Code on Shashi's Windows laptop."
---

# Cartoon studio: Shashi and Claude co-direct

Shashi and Claude are **co-directors**. Work in small modules. Each module ends with a **decision card**: Claude brings 2-3 options, marks the recommended one, says why, and Shashi decides in a word. Never run from script to finished video in one go. Catch problems while they are cheap: on paper, on stills, in the animatic. Not after the full render.

Follow `working-with-shashi` and `shashi-global-rules` throughout (plain words, plan first, cheap helpers, honest checks, show before saving).

## What to read

| file | what it holds | applies to |
|---|---|---|
| `references/craft_book.md` | how things look and move: faces, head turns, physics, camera, staging, motion vs backdrop, sound | **every story**. Read before designing any shot. |
| `series/<name>/bible.md` | cast, voices, drawing style, places, recurring gags of one series | that series only |
| `references/cards.md` | templates: story sheet, decision card, episode notebook, animatic spec | every module |
| episode `notebook.md` (in the project, not here) | story and directing choices for one story, with reasons | **that story only. Never turned into a general rule.** |

Series now: `series/yabuuu/` (Kannada comedy, Ramesh and Suresh, the ಯಬೂಊಊ sting). A new series starts from `series/_new_series/bible.md`.

## Who does what

- **Shashi:** the story, its human touch, and every ★ decision.
- **Opus (me): the director's legwork and opinion.** Story sheet, story beats, shot list, camera, acting, character design, backdrop prompts, checking every render. Coming up with engaging staging and animation is my main contribution, not just assembling parts. Bring a clear recommendation every time.
- **Command Code helper (DeepSeek 4.1 Flash; Shashi prefers fast mode for animation: `-m deepseek/deepseek-v4.1-flash-fast`):** drudgery with a precise spec, such as sound-effect scripts, mux/encode scripts and bulk edits. It is weak at drawing and acting: don't hand it characters or staging. Post the model plan and wait for OK before using it.
- **ElevenLabs connector:** voices (`eleven_v4`) and backdrops (`recraft-v4.1-flash`, ~48 credits each). Shashi is on the paid Starter plan.

## The modules (★ = decision card, wait for Shashi)

**0. Story sheet ★** Shashi's story can come in any form: dialogue, a paragraph, notes, a transcript. Sort it into four boxes (plot, characters, places, dialogue) and mark each item ✅ given / ❓ unclear / ➕ missing (template in `cards.md`).
- ❓ → a one-word question with my best guess marked.
- ➕ → a labelled suggestion with a one-line reason.
- Plot sharpening → name the weak spot, offer 1-2 small fixes, plus **"leave as is"**.
- **Protect the writer's touch.** Shashi's words stay word for word. Suggestions stay visibly separate, never mixed into the text. Trim or reorder before adding. Any new line is written in that character's own voice. "Leave as is" is always an option.
- Find the twist: build-up (anticipation, greed, excitement), a held silence, the reveal, a deadpan beat, then the sting or ending.
- Output: the **locked script**. Every later module builds from it.

**1. Brief ★** Which series (or a new one)? Format (16:9 / 9:16)? Setting: make it specifically local (Mangaluru: loud colourful private buses, Mangalore-tile roofs, laterite walls, coconut palms…). Mood. For a new series, also fill a first draft of its bible.

**2. Storyboard ★** A shot table (time, place, what moves, line or sound), **plus rough sketch frames**: one small image per shot, drawn in code (grey boxes for the set, simple figures, an arrow for camera movement), shown as one contact sheet. Pick each place *for the motion the shot needs* (craft book §4).

**3. Voices ★** `creative_list_voices(languages=[...])`. Cast from the series bible; new characters get 2-3 candidate voices to choose from. Keep Shashi's words; fix pronunciation by respelling (ask how it should sound). No "…" inside a word (it makes a pause); drawn-out sounds = repeated vowels. Light emotion tags only. 2 takes when delivery matters; Shashi picks. Download promptly (links expire ~2 h).

**4. Backdrops ★** Prefix: "Flat 2D storybook vector illustration with clean bold dark outlines, background plate for an animated short, wide 16:9, no people, no readable text." (or the series' own prefix). State the viewpoint explicitly ("seen from the seat in front, looking straight at…", "flat SIDE VIEW elevation, no perspective"). 2 variations when the look matters. Measure where characters stand or sit on a grid before using a plate.

**5. Characters and style stills ★** A still frame for every new character, angle or set; Shashi reviews faces closely (eyes!). Iterate on stills: they are cheap. A few-second motion test for any new kind of movement.

**6. Animatic ★** The rough draft of the film (spec in `cards.md`): real voices at real timing, real backdrops and camera framing, characters placed but without acting, low resolution, shot number and line burned in. Renders in about a minute. Question it answers: *does the story play well in time?* Fix pacing, pauses and shot order here.

**7. Acting pass ★** Acting as keyframes over the master clock (see "Code"). Show a 6 fps preview plus stills of the key beats (the twist, reactions). Short card: "these beats, these expressions: OK?"

**8. Final render and sound (automatic, then checked)** Full render, procedural ambience and effects, mix, mux. Check honestly: 1 fps contact sheet (+ 2-4 fps around key beats) and look at it; measure `volumedetect` in voice vs ambience windows (voices ~15-20 dB above). Report what was checked and fixed.

**9. Review and lessons ★** Deliver with `SendUserFile` (display `attach`; previews can be muted). Join scenes with ffmpeg's concat *filter* (re-encode). In the cloud, remind Shashi the machine is wiped when idle and offer a zip. Then sort every correction Shashi made:
- how things **look or move** → `references/craft_book.md` (all stories);
- cast, voice, style or gag of the **series** → that series' `bible.md`;
- a **story or directing choice** → the episode notebook only.
Show the proposed additions; save after OK. The skill files live in Shashi's claude.ai skills, so a changed skill is delivered as a zip for Shashi to upload.

## Decision cards: how to run them

- One card per module, fitting on one screen. Format in `cards.md`.
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
