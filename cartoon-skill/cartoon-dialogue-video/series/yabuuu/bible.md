# Yabuuu series bible

Kannada comedy skits. Two friends get excited about something, it builds up, and the twist deflates it. Then Suresh says "ಯಬೂಊಊ".
General look and movement rules are in `references/craft_book.md`. This file holds only what is special to this series.

## Episodes

| # | title | length | notes |
|---|---|---|---|
| 1 | Madam Magu | 83.5 s | the reference episode; code in `assets/template/`, backdrops in Shashi's project zip |

## Cast and voices (ElevenLabs, `eleven_v4`)

| character | voice | id | look (`ink.py` spec) |
|---|---|---|---|
| Ramesh | Bharadwaj – Expressive, Real & Chill Guy | 75K9CAd9ZbhCXsP4nMDk | `RAMESH`; tilak on the forehead |
| Suresh | Srivatsa – Casual & Natural Conversation | jtyEMdWULw6XHzgQFVCt | `SURESH` |
| older neighbour | Rajaratna P | Z1sgBQe4e9WquuP9yR3D | `NEIGHBOUR` |
| Madam (ep 1) | — | — | `MADAM` |

## Look: "living ink"

- Big heads (about 1:3), bold dark outlines (#20140E), flat fills, simple bodies with four-finger hands.
- Boiling lines and characters on twos (see craft book §1).

## Places: Mangaluru

- Colourful private bus: deity photo + red bulb, tinsel, stickers, conductor's bag. Shashi rejected a clean modern bus as "San Francisco metro".
- Mangalore-tile roofs, laterite walls, coconut palms.
- Props: "S.K. TEXTILES" shopping bag.

## The sting: "ಯಬೂಊಊ" (every episode)

- At the twist the two friends slowly turn to each other.
- **Suresh** says the catchphrase from `series/yabuuu/sting_yabuu.mp3` (light, puzzled-amused, quick start, long dragged "ಊ"; 2.3 s), mouth moving, one brow up, small head tilt.
- **Then** the picture freezes, a slow push-in, colour drains (`hue=s=0.45`), whoosh, and `series_sfx.music_hit()` (plucked D-A-D + tabla "dhin").
- Reuse this exact recording and hit every episode.
- Rejected before: Ramesh's voice, slow or sober delivery, intense or pained delivery.

## Story shape (typical, not a rule)

Build-up (anticipation, greed, excitement) → held silence → reveal → deadpan beat → sting. Each story decides its own details in its notebook.
