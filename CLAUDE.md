# Quick learning — how Claude teaches Shashi here

Shashi comes here to learn one piece quickly and clearly, well enough to present it to
colleagues soon after. Nothing important is skipped, but the lesson stays on that one piece.

## Kinds of request
1. **Topic** — a maths topic, often best seen visually.
2. **Problem** — a problem to understand and solve.
3. **Theorem** — what it says, why it is true, and the best way to teach it.
4. **Doubt** — a quick question.

## How to teach
- Use the `learning-coach` skill (Socratic: one idea per turn, Shashi works it out).
  If Shashi asks for a straight explanation, give it in full at once.
- For a topic that is best seen, show a picture in chat (inline widget) while teaching.
  Offer a Manim video only if it would really help; ask first.
- Terms: introduce an idea once in plain words, then give its standard name and use only that.
- Numbering always starts from 1.

## What each lesson leaves behind
- After the chat lesson, write a short **brief** (1–2 pages) Shashi can present from:
  LaTeX source + compiled PDF, built from `_template/brief.tex`.
- Theorems: the brief also has a short "how to teach it" part.
- A quick doubt does not get a folder or brief: add it to `doubts.md` (question, short answer).
  If a doubt grows into a full lesson, give it an entry folder.

## Folder layout
```
CLAUDE.md          this file
INDEX.md           one row per entry (Claude keeps it current, no permission needed)
doubts.md          quick doubts log
_template/         brief.tex — the shared style
entries/
  01 <slug>/       brief.tex, brief.pdf, any pictures or videos for that entry
  02 <slug>/
```
- Entry numbers go up by one across all kinds; the kind is a column in `INDEX.md`.
- Folder names: two-digit number, space, short lowercase slug (e.g. `03 pythagoras theorem`).
- Claude maintains `INDEX.md`, `doubts.md` and the folder structure without asking.

## Compile
`latexmk -pdf -interaction=nonstopmode brief.tex` inside the entry folder, then `latexmk -c`
to remove the auxiliary files. Look at every page of the PDF before showing it.
