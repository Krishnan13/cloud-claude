# Craft book: how things look and move (all stories, all series)

These are general lessons on drawing, movement, camera and sound. They apply to every story. Most came from Shashi's feedback on Yabuuu episode 1.
Story and directing choices (where the twist goes, pacing of one episode) do **not** belong here: they go in that episode's notebook.
A series' own cast, colours and gags go in its `bible.md`.

## 1. Drawing in code

- **Boiling lines:** the drawing wobbles slightly 8 times a second (`ink.boil`). Use a smooth offset *field* (neighbouring points move together). Jittering points one by one tears shapes open and kills fills.
- **On twos:** characters change pose 12 times a second (`tc = floor(t*12)/12`); world motion (window lights, light sweeps, camera) runs every frame at 24 fps.
- **Outlines match the backdrops:** if the painted plates have dark outlines, the characters need the same outline colour and weight, or they look pasted on.
- Keep characters at a readable size; tiny distant figures merge into a blob.

## 2. Faces and eyes

- Big dark pupils with a highlight.
- The upper-eyelid line curves *up* like a real eye. A downward-dipping lid line reads as angry.
- Friendly arched brows, set well above the eyes.
- Default lid 0.1. Heavier lids only for acting: droop = disappointed or deadpan, lift = surprise.

## 3. Head turns (three-quarter view)

- Features slide toward the turn, the chin shifts, the nose pokes out on the turn side, only the back ear shows, more hair on the back of the head.
- The eye on the *turning side is the far eye*: slightly narrower and tucked behind the nose. (Getting this backwards made a character's eyes look wrong.)

## 4. Motion must fit the backdrop (flat paintings)

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

## 5. Staging and camera (films, not stage plays)

- Characters who talk to each other **turn toward each other**. While one speaks, the listener looks at the speaker, not at the camera.
- Default conversation angle: from the front, waist-up two-shot; cut to single medium shots of the speaker and close-ups for reactions.
- Snap zoom (0.15 s) for a shock line.
- Show actions so they read instantly:
  - peeping into a window → **from inside the room**: faces rising slowly above the sill, fingers curled over it, eyes searching (backs of heads from outside were unreadable);
  - searching while walking → **side view**: looking over walls, peering into bushes, a hand shading the eyes.
- Comedy tools: a gag the other character doesn't notice, a daydream bubble, silence before a reveal, a slow deadpan turn.

## 6. Sound

- Voices on top, about 15-20 dB above the ambience.
- Ambience per place (vehicle hum + vibration, crickets, birds, crowd murmur).
- One effect per meaning (horn, brake hiss, bell, pothole thud, whoosh on a snap zoom, ka-ching for money).
- Silence for suspense. Footsteps only while walking.
- Two-pass loudnorm to −14 LUFS.

## 7. Working rhythm that saves rounds

Story sheet → storyboard sketches → stills → short motion test → animatic → acting preview at 6 fps → full render. Iterate on paper, stills and previews, never on full renders.

## Lesson log

Add new lessons above, in the right section, with the date and episode in brackets, e.g. "(Oct 2026, Yabuuu ep 2)".
