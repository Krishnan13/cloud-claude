# Templates: story sheet, decision card, animatic, episode notebook

## 1. Story sheet (Module 0)

Read Shashi's story in whatever form it comes. Fill this in, then show it.

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

Rules:
- Quote Shashi's lines exactly. Never reword them in the sheet.
- Suggested new lines are shown separately, marked "SUGGESTED", each with a one-line reason, in that character's voice.
- Prefer trimming or reordering over adding.
- Every suggestion can be refused; "leave as is" is always listed.

After approval, write the **locked script**: Shashi's lines plus only the accepted suggestions, with speaker, place and any stage note per line.

## 2. Decision card (end of every ★ module)

```
CARD <n>: <module>

Here it is: <image / contact sheet / audio / video attached>

Options:
  A ★ <option> (why, in one line)
  B   <option> (why)
  C   <option> (why)          cost if it differs: credits / time

Small calls I made myself (overrule any): 
  - ...
  - ...

Your call: A / B / C / other
```

Keep it to one screen. Show, don't describe. One question per card when possible.

## 3. Animatic spec (Module 6)

- Real voice takes placed at their real times; rough mix (voices + one ambience bed, no effects yet).
- Real backdrops and the planned camera framing and cuts.
- Characters placed in neutral poses, facing the right way; mouths move from `envelope.py`; no other acting.
- Burned-in text, top left: shot number and the line being spoken.
- `-ql --frame_rate 6`; about a minute to render.
- Ask on the card: pacing, pauses (especially before the twist), shot order, anything that drags or rushes.

## 4. Episode notebook (one per story, in the episode folder)

```
# <series> ep <n>: <title>

## Story sheet (approved <date>)
...
## Locked script
...
## Decisions
| module | decision | why | date |
|--------|----------|-----|------|
## Lessons for the craft book / series bible (proposed in Module 9)
...
```

Decisions here belong to this story. Only lessons about how things look or move go on to the craft book.
