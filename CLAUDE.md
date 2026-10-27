# Teaching notes: working rules (cloud)

Shashi (Krishnan) is a mathematics teacher: Grade 9 and 10 CBSE tuition, BIO LEARNING CENTER (BLC) MCQ sets, and Prayoga's Prerana activities.
This file holds the key rules. The full reference is `handbook.md` (section numbers below point into it). Open a handbook section only when the task needs it, to save usage.

If this file, the handbook and Shashi disagree: what Shashi says now wins, then this file, then the handbook. If unclear, ask. Do not guess.

## 1. Where the work runs (changed 27 Oct 2026)

- **This cloud workspace is the main place for the work.** The handbook's rule "laptop first, cloud only as fallback" is replaced.
- The workspace is temporary. Keep all work files in this GitHub project, in one folder per chapter (for example `g9-ch6-perimeter-area/`), and commit and push when a piece of work is approved, so nothing is lost.
- The repo must stay **private**. It holds class details and Drive ids.
- Not available here: `/mnt/project-files/`, Remote Control, device folder tools, Codex. Ignore handbook steps that need them.

## 2. Talking with Shashi (handbook 8.4)

- Plain words, treat Shashi as a capable non-expert. Lead with the answer. Short replies.
- Anything bigger than a quick answer: show a short plan and wait for OK. Ask one-word questions, mark the recommended option.
- For lesson material: consult first, get the lesson brief approved, then build (handbook 3.3, math-lesson-builder skill).
- Say what was checked and how. Never just "done". Answer "done?" in one or two honest lines.
- Do not add content Shashi did not ask for; suggest it in chat first.
- When Shashi corrects something or states a new preference, add it to this file (or the handbook log, 8.5) in the same turn, and tell Shashi.

## 3. Saving usage: helper models (handbook 6)

- Main model: planning, question design, judgement, teaching and language review, final look at every page.
- Helpers do drudgery (LaTeX, TikZ, re-solving, formatting) through Command Code, already installed here:

      bash /usr/local/bin/delegate.sh -m <model> -d <folder> -t <turns> "task"

  - `deepseek/deepseek-v4.1-flash` (or fast: `deepseek/deepseek-v4.1-flash-fast`): routine work.
  - `meta/muse-spark-1.3-contributor`: independent re-solve of every answer (never show it the answers).
  - Snippet jobs: `-t 3`, a scratch `-d`, and say "output only ..., do not create files". Strip DeepSeek's ```latex fence.
  - It runs with full tools: point `-d` only at a scratch or target folder.
  - Big papers: 2-3 DeepSeek jobs in parallel, one section each, then assemble.
  - Haiku subagents (effort xhigh) only if Command Code fails.
- **Before using any helper, post a one-line-per-job model plan and wait for OK.**
- **Every time DeepSeek is used, ask Shashi: fast mode or normal?**

## 4. Quality bar (lean, handbook 2.1 and 3.3)

1. Write with the checklist rules from the start (Appendix D of the handbook).
2. One cheap independent checker re-solves every answer and compares every diagram label with the text.
3. One round only. A second round only if a maths error is found.
4. Compile, render every page, and look at every page of both copies.
5. Final look by the main model at every diagram, question and question sentence before Shashi sees it.
6. Never use find-and-replace on numbers or words across a file. Edit each place by hand.

## 5. Question and sheet rules (handbook 8.1-8.3)

- CBSE competency-based, easy to hard, only a few easy ones. Test the objective from every angle (work backwards, explain, find the mistake, draw, compare/what-if, real life). At most one plain-substitution question per set.
- Every question and example says exactly what to find.
- Worked examples show: rough diagram with measurements, **Given:**, **To find:**, steps with reasons, **Answer:** with units.
- Indian and South Indian settings in plain English. No regional words (visiri, pookalam). No pizza.
- Whole-number answers (including steps) unless decimals are the point. Data must be possible.
- Some questions: tell students to draw a rough diagram; sometimes make drawing a marked part.
- Stay within what has been taught. Do not repeat earlier questions.
- Student sheet: no difficulty labels, no question titles. Assignment heading: "Assignment" left, date right, one thin rule.
- fc copy: for other teachers. Formal academic register ("Concepts assessed"), short sentences, active voice, no tool talk (TikZ, trap). A rough answer diagram for every question. "Common mistake" notes only when truly needed. Answers in smaller grey text.

## 6. House design and LaTeX (handbook 5, preambles in Appendix E)

- A4, 11 pt, plain exam-paper look, black and white (figures must read in greyscale).
- Century Schoolbook: `tgschola` + `fouriernc`. Fractions with `\dfrac`. Rupees with `tfrupee` (`\rupee`).
- One source, two copies: first line `\newif\ifteacher\teacherfalse` (student) or `\teachertrue` (fc).
- Compile with `pdflatex` twice. Render pages with `pdftoppm` and look at each one.
- LaTeX needs the setup script in this environment (texlive packages + `tex-gyre` + `texlive-fonts-extra`).

## 7. Files, names and delivery (handbook 4)

- Names: `<name> N` (student) and `<name> N fc` (teacher), as .tex and .pdf. Example: `homework 3`, `homework 3 fc`. Do not change a name Shashi gives.
- BLC MCQ series keeps its own names: `set N perimeter area`, `set N solution perimeter area`.
- Google Drive: top folder "Tuition_grade9,10" (id `1qszlXOHCttHHiYTIHfJHLLzFXqzCBZwP`); Chapter 6 folder "Perimeter and area (g9, ch6)" (id `1GyNyZlcFLsVkoSPMUvU42g-hiF9uWJ48`).
- Share PDFs in the chat first. Save to Drive only after Shashi says OK. Keep the old version when replacing.
- The Drive connector can save .tex files; it could not upload PDFs in the old project. Check before promising.

## 8. Where the classes are (handbook 7; check with Shashi before planning)

- Grade 9, Chapter 6 (Ganita Manjari): whole chapter taught, including area of circle, sector and segment (Shashi, 27 Oct 2026). Tests on Drive: test 1, test 2 (50 marks), test 3 (30 marks, made 27 Oct 2026, in `g9-ch6-perimeter-area/test3/`).
- Grade 10: nothing recorded yet.
- Prerana (30 Oct 2026): waiting for Shashi to pick one of four activities (handbook 3.9).
