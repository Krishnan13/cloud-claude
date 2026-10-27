# Teaching notes project: complete handbook

Written on 27 October 2026 for Shashi (Krishnan), owner of the "Teaching notes" project.

This handbook lets a new assistant with no memory continue Shashi's work exactly. It collects everything known about how Shashi works in this project. Nothing in the source material is shortened: the project instructions, the project memory, the two personal skills, the lesson-builder skill and the review checklist are copied in full, word for word.

## 0. How to read this handbook

### 0.1 Sources used

| Source | Where it lives | How it appears here |
|---|---|---|
| Project instructions | Project settings (session context) | Section 1, word for word |
| Project memory index (MEMORY.md) | Project memory store (`team/silo/MEMORY.md`) | Section 2.1, word for word |
| Detailed memory files (6 files) | Project memory store | Section 2.2, word for word |
| Skill "working-with-shashi" (version 2, 12 Oct 2026) | Shashi's Claude account | Appendix A, word for word |
| Skill "shashi-global-rules" | Shashi's Claude account | Appendix B, word for word |
| Skill "math-lesson-builder" with its two references and template | Shashi's Claude account | Appendix C, word for word |
| Review checklist | `/mnt/project-files/review-standard/review-checklist.md` | Appendix D, word for word |
| LaTeX source files | `/mnt/project-files/` (Class 2 revised, homework 1, homework 2) | Section 5 and Appendix E |
| All 10 earlier threads and the project chat | Project history | Sections 3, 7 and 8 |
| Laptop rule files (CLAUDE.md, AGENTS.md, command-code-helpers.md, delegate.sh, codex.sh) | `E:\tuition content` and `C:\Users\Krishnanvp\bin` on Shashi's laptop | Section 6, word for word (read on 27 Oct 2026) |
| Laptop Claude Code memory for the tuition folder | `C:\Users\Krishnanvp\.claude\projects\E--tuition-content\memory\` | Section 2.3, word for word |

### 0.2 Order of authority when sources disagree

1. What Shashi says in the current conversation.
2. Project instructions (Section 1).
3. Project memory (Section 2). Newer entries override older ones. Section 2.4 lists entries that later decisions replaced.
4. The skills "working-with-shashi" and "shashi-global-rules" (Appendices A and B).
5. The skill "math-lesson-builder" (Appendix C). Its visual design (Computer Modern font, blue colours, pale-blue boxes) is **replaced** by Shashi's house design (Section 5.2). Its consultation-first workflow still applies.

If two sources disagree and the answer is not clear, ask Shashi. Do not guess. (Rule from working-with-shashi, section 0.)

### 0.3 Who Shashi is (facts gathered from memory and threads)

- Name: Shashi. Also called Krishnan. Email on the account: krishnanvp18@gmail.com. GitHub login: Krishnan13 (no repositories are attached to this project).
- A mathematics teacher. Teaches Grade 9 and 10 tuition (CBSE). Memory calls it "tuition/BLC". BLC is the **BIO LEARNING CENTER** (spelled CENTER), for which Shashi also makes MCQ sets (Section 7.1).
- Grade 9 textbook: the new NCERT book *Ganita Manjari, Grade 9, Part I* (2026). Chapter 6 is "Measuring Space: Perimeter and Area" (sections 6.1–6.10). The chapter PDF is `E:\tuition content\g9 perimeter and area ch6.pdf`.
- Also works at **Prayoga**, which runs the **Prerana** project: one-day experiential, hands-on activities for school students.
- Prefers plain, non-expert explanations. Wants to be treated as a capable amateur, not an expert. Use short sentences and teach briefly when something is technical.
- Very conscious of Claude usage. Claude usage hit 92% on 11 October 2026.
- Devices: a Windows laptop (LAPTOP-IP0993EO) with Claude Code in the desktop app, Google Drive for desktop, Command Code CLI, Codex CLI and MiKTeX. An iPad for teaching with slides (annotates PDFs in GoodNotes, Notability or Files). A phone to follow threads through Remote Control.
- Interested in learning IGCSE and IB mathematics to broaden whom they can teach (13 October 2026).

---

## 1. Project instructions (word for word)

These are the standing instructions saved in the project settings. They are copied exactly.

```
Saving usage: for production or mechanical work (drafting questions, writing LaTeX, drawing TikZ diagrams, re-solving answers, compiling, formatting), hand the work to helper models with precise specs.

Helper models on Shashi's laptop (follow command-code-helpers.md / CLAUDE.md in the tuition folder):
- Default: Command Code CLI. DeepSeek 4.1 Flash for routine work; Muse Spark 1.3 as the second model and for independent re-solving.
- Backup and heavy thinking: Codex CLI. GPT 5.6 Luna for drudgery when Command Code is unavailable; GPT 6.1 Sol or GPT 5.6 Sol for very high intellectual work (hard question design, deep maths or teaching review).
- In the cloud (laptop models not reachable): Haiku subagents (effort xhigh).

Before using helpers on a task, post a short plan saying which models you want for which job and ask Shashi to confirm.

Then review everything helpers produce yourself before it reaches Shashi: compile and check every diagram and answer, and fix small issues directly. Keep planning, judgement calls and the final review with the main model. Keep the review lean: one checker, one round, unless a maths error is found.
```

The project topic (shown in the project header) says:

```
For mathematics lesson planning and teaching-material creation, use $math-lesson-builder. Use this project's sources and previous discussions as context. Complete the consultation and obtain approval of the lesson plan before creating the document.
```

---

## 2. Project memory (everything, word for word)

### 2.1 Memory index: MEMORY.md (word for word)

````markdown
# Teaching notes project
- Owner: Shashi, a mathematics teacher (tuition/BLC, Grade 9 etc.). Prefers plain, non-expert explanations.
- Goal: plan maths lessons and build teaching materials with the math-lesson-builder skill.
- Rule: consult first and get the lesson plan approved before producing the document.
- Outputs typically LaTeX source + compiled PDF.
- No repositories attached.
- Source files live in Shashi's Google Drive: "tuition 9 10" > "Perimeter and area (g9, ch6)" folder: class 1 (PDF only, no .tex, old style), class 2 (.tex + PDF, diagram-fixed and restyled to house design 2026-10-08; student 10 pp, fc 13 pp), test 1, test 2, practice questions, homework 1. Ask before changing Drive files. Restyled working copies of class 2 also in /mnt/project-files/perimeter-area-class2-restyle/.
- File naming (all materials): "<name> N" for the student copy and "<name> N fc" for the facilitator copy, e.g. "class 2" / "class 2 fc", "homework 1" / "homework 1 fc", "test 1" / "test 1 fc", each as .pdf and .tex. Homework 1 (up to Ex 6.2A) done 2026-10-08. Homework 2 (sections 3-4 + median theorem) started 2026-10-11.
- Saving to Drive: the Drive connector can upload .tex but not PDFs (too large). Preferred route: Shashi's laptop has Google Drive for desktop; the synced folder "Tuition_grade9,10" is connected as a device folder (approved 2026-10-08). Save finished PDFs/.tex there and Drive syncs them. Use start_folder_thread with that folder.
- Default device for Remote Control (set by Shashi 2026-10-11): environment_id env_01MvLkQgcViMNAiUEzxQHuip (start_rc_session naming it starts with no card).
- DEFAULT WHERE WORK RUNS (Shashi, 2026-10-11): start every new work thread as a Remote Control session on Shashi's laptop (start_rc_session with the default environment above), not in the cloud. Shashi follows it from their phone via Remote Control. Fall back to a cloud thread only if the laptop is offline, and say so.
- HELPER MODELS (Shashi, 2026-10-11; also in project instructions). On the laptop: (1) default = Command Code CLI: DeepSeek 4.1 Flash for routine work (LaTeX, diagrams, formatting), Muse Spark 1.3 as second model / independent re-solver; tested OK 2026-10-11. (2) Codex CLI = backup for Command Code: GPT 5.6 Luna for drudgery; GPT 6.1 Sol / GPT 5.6 Sol for very high intellectual work. How-to: command-code-helpers.md and CLAUDE.md in the laptop tuition folder. In the cloud: Haiku subagents (xhigh). RULE: before using helpers on a task, post a short plan of which model for which job and ask Shashi to confirm. Claude still reviews all helper output.
- Account skill "working-with-shashi" saved 2026-10-11 (general working rules, evolves via approved update cards). A second "teaching material" skill was offered; Shashi parked it for later.
- USAGE (Shashi, 2026-10-11, firm): keep work lean. Drudgery goes to cheap helpers (above). The main session plans, judges and does the final review. Shashi stopped the homework 2 work because the 6-checker x 3-round review burned far too much usage (~1.6M tokens). Claude usage hit 92% on 2026-10-11 and Shashi is very concerned: keep Claude's own share minimal.
- QUALITY BAR, LEAN VERSION (agreed 2026-10-11, replaces the earlier 6-checker gate): (1) write each sheet with the checklist rules applied from the start; (2) one independent cheap-model checker per sheet that re-solves every answer and compares every diagram label with the text; main session does teaching and language review itself; (3) one round only, fix and recheck changed pages yourself, a second round only if a maths error was found; (4) only real problems (wrong answers, wrong labels, unclear questions) block delivery; style suggestions are listed for Shashi to accept or ignore. Still never blind find-and-replace numbers. Checklist: /mnt/project-files/review-standard/review-checklist.md.
- FINAL CHECK BY THE MAIN MODEL (Shashi, 2026-10-12): before any sheet reaches Shashi, the main Claude model (Opus) itself looks once more at every diagram, every question, and how each question sentence is framed. Helpers' checks do not replace this.
- Pythagoras is fine to use in homework questions (Shashi, 2026-10-11).
- WORKED EXAMPLES MUST MODEL THE SOLUTION FORMAT WE TEACH (Shashi, 2026-10-11, applies to all materials): rough diagram with given measurements marked, "Given:" and "To find:" lines, step-by-step solution with reasons, final answer with units. Done for Class 2 (saved to Drive 2026-10-11).
- Exercises must test the learning objective from every angle (work backwards, explain why / true-false, find the mistake, draw, compare / what-if, real-life), at most one straight-substitution question per set. Shashi found the Class 2 exercises too weak on this (2026-10-11).
- Every question and example must state explicitly what to find. A Class 2 example only showed an area calculation without asking for it, and a student asked "what to find here?" (2026-10-11). Never let this happen.
- Facilitator (fc) copies are for other teachers too: write teacher-facing text (notes, overview, answer explanations) clear, with short sentences, active voice, one point per sentence, consistent terms (ASD-STE100 style). Student questions stay in normal clear English. No tool or internal talk (no "TikZ", "trap", "invariant"). Don't spoon-feed.
- FC REGISTER IS FORMAL / ACADEMIC (Shashi, 2026-10-12): short and clear does not mean casual. Use standard teaching vocabulary other teachers expect, e.g. "concept tested" / "concepts assessed", not "idea tested" / "ideas". Check the whole fc for similar informal words and fix them. Test 2 fc used headings Paper design, Competency focus, Concepts assessed, Common misconceptions, Marking, with answers in full sentences; Shashi approved this.
- "Common mistake" notes in fc: balance. Include one only when that mistake is genuinely likely and worth flagging (e.g. using the sloping side as height helped Shashi in class). Keep each very short and simple. Don't add one to every item or try to read students' minds everywhere; Shashi found overloaded notes confusing (2026-10-11).
- Deliver reviews with pictures as one self-contained PDF; markdown with separate image files doesn't render in the previewer.
- Question style: CBSE competency-based, not direct formula use; easy to hard. Use mostly Indian and South Indian everyday contexts (not pizza etc.) so students connect. But keep the wording in plain English: avoid regional words students may not know (e.g. "visiri"); use an Indian word only if it's very widely known.
- Numbers in questions: choose values so every answer (including intermediate steps) comes out as a whole number unless decimals are the point of the question. Shashi queried an unplanned 337.5 on 2026-10-11.
- Diagrams in question sets: not every question needs a printed diagram, but for those without one, explicitly ask students to draw a rough diagram; for some, make drawing the diagram an actual part of the question.
- Solution/fc copies: include a rough answer diagram for every question (Shashi asked why they were missing, 2026-10-11).
- Assignment/homework sheet format: minimal heading, just "Assignment" with the date at the top right. Nothing on the student sheet that distracts from the question: no difficulty section labels (Warm-up, Challenge, etc.) and no titles or labels in front of questions (e.g. "Vegetable patch", "Clock."). Easy-to-hard grouping and question nicknames are internal only (fine in chat or fc notes).
- House design (default for all new sheets, chosen 2026-10-08): plain, exam-paper look. Font: Century Schoolbook. Black text, no coloured boxes (notes/remember boxes sit between thin grey rules), one thin rule under the heading, diagrams in dark grey / soft grey fills. Fractions full-size (display style, mixed numbers clear), never squeezed small inline. Use the ₹ symbol for rupees. Keep exercise headings with their questions; watch page count (Century Schoolbook is wide, keep line spacing tight). Teacher-copy answers in smaller grey text. Class 1 restyle offered, not yet requested.
- Shashi likes to verify PDFs before they're saved to Drive: share the PDFs in the thread first. (Exception: when on mobile they may ask to push straight to Drive and check there.)
- Class progress (as of 2026-10-12, Shashi): perimeter fully taught, including arc length and perimeter of a sector. Heron's formula taught. Area of a circle, sector and segment NOT yet taught.
- Done 2026-10-12: Test 2 (50 marks, everything except circle/sector/segment area), "test 2" and "test 2 fc" (.pdf + .tex) saved to the Drive ch6 folder; built in the "50-mark perimeter and area test" thread. Shashi approved and asked for old versions to be cleaned; done (working notes kept on the laptop).
- Done 2026-10-11: homework 2 final and Class 2 revised (stronger exercises, find-lines, plain fc; single source body-source.tex with \ifteacher in /mnt/project-files/perimeter-area-class2-revised/). Shashi approved; both saved to Drive (old class 2 kept in perimeter-area-class2-restyle/).
````

### 2.2 Detailed memory files (word for word)

**feedback-assignment-layout-and-design.md**

````markdown
---
name: feedback-assignment-layout-and-design
description: Shashi's layout rules for student sheets: "Assignment" + date header, no difficulty/section labels, minimal elegant design
metadata:
  type: feedback
---

- Homework/assignment header: just "Assignment" (left) and the date (top right). No module title, class name or descriptor block.
- Never print internal labels like "Warm-up", "Think it through", "Challenge" or difficulty grading on student sheets; that is internal discussion only (fine in teacher notes).
- Shashi felt the old blue-box style (colour headings, panel boxes) "does not look elegant" (2026-10-08). Font chosen by Shashi 2026-10-08: Century Schoolbook (\\usepackage{tgschola}\\usepackage{fouriernc}; needs tex-gyre, texlive-fonts-extra). Always use display-size fractions (\\dfrac). Rest of style accepted as simpler:, black text, one thin rule under the header, no boxes, no question titles, muted grey answers in the teacher copy, slate-grey diagrams. Shashi approved this style and had Class 2 restyled with it on 2026-10-08 (class 2 files in Drive replaced); use it for all materials.

**Why:** Shashi's feedback on the Class 2 homework, 2026-10-08.
**How to apply:** apply to every new student-facing sheet. Related: [[feedback-indian-contexts-plain-words]]
````

**feedback-indian-contexts-plain-words.md**

````markdown
---
name: feedback-indian-contexts-plain-words
description: Shashi wants Indian/South Indian contexts in questions but plain English words, not regional terms
metadata:
  type: feedback
---

When writing word problems, use mostly Indian (and South Indian) contexts so students connect (festivals, rupees, local objects), but keep the wording in plain English. Use an Indian word only if it is very widely known (e.g. rangoli, Onam); avoid regional words like "visiri" or "pookalam".

**Why:** Shashi (2026-10-08) rejected a pizza context as foreign, then flagged "visiri" because students may not know it.
**How to apply:** pick Indian settings, describe them in English. Related: [[reference-drive-tuition-folder]]

Also (2026-10-08): not every question needs a printed diagram, but explicitly tell students to draw rough diagrams, and for some questions make "draw the diagram" a marked part of the question so they are forced to do it.
````

**feedback-use-smaller-subagents.md**

````markdown
---
name: feedback-use-smaller-subagents
description: Shashi wants bulk production work done by smaller-model subagents, then reviewed by the main Claude, to save usage
metadata:
  type: feedback
  modified: 2026-10-08T08:46:23.565Z
---

For bulk production work (for example redrawing TikZ diagrams in lesson files), Shashi asked that Claude hand the work to smaller-model subagents (Sonnet) and then review the results itself, instead of doing all of it directly.

**Why:** to save usage. Said on 2026-10-08 while the Chapter 6 Perimeter and Area Class 2 diagrams were being fixed.

**How to apply:** give the subagents precise specs. Render their output and check every diagram visually before delivering, and make small fixes yourself. Lesson materials still need approval before production, as in [[consult-before-producing]].
````

**reference-drive-tuition-folder.md**

````markdown
---
name: reference-drive-tuition-folder
description: Where Shashi's tuition materials live in Google Drive and on their Windows laptop, and how to deliver PDFs there
metadata:
  type: reference
  modified: 2026-10-08T09:00:07.235Z
---

Shashi keeps Grade 9/10 tuition materials in Google Drive under "Tuition_grade9,10" (Drive folder id 1qszlXOHCttHHiYTIHfJHLLzFXqzCBZwP). Each chapter has its own subfolder, for example "Perimeter and area (g9, ch6)" (id 1GyNyZlcFLsVkoSPMUvU42g-hiF9uWJ48).

Their Windows laptop runs Google Drive for desktop, which shows this folder at `G:\My Drive\Tuition_grade9,10`. On 2026-10-08 they granted the device folder tools access to that folder.

**How to apply:** to deliver PDFs, connect the device and write them into the G:\ folder with device_commit_files, and Drive syncs them. The Google Drive connector can't upload PDFs: it only accepts file contents written out inline, and the PDFs are too big for that. Get approval before replacing originals ([[feedback-use-smaller-subagents]]).


File naming (Shashi, 2026-10-08): in the chapter folder, student copies are named simply "class 1", "class 2", "homework 1" (+ .pdf/.tex) and facilitator copies add " fc" (e.g. "class 2 fc.pdf"). Use this scheme for new files. Renaming works via the Google Drive connector's update_file (title); the device folder tools can't rename.
````

**feedback-strict-review-of-materials.md**

````markdown
---
name: feedback-strict-review-of-materials
description: Shashi requires a strict, multi-angle review of every teaching/student sheet before delivery (maths, diagrams, typos, pedagogy)
metadata:
  type: feedback
  modified: 2026-10-11T09:43:13.863Z
---

On 2026-10-11 Shashi found a wrong label ("16" instead of 15 on side AC) in the homework 2 fc diagram. It was caused by a blind find-and-replace when Q6 numbers were changed, plus re-checking only the edited page. Earlier in the same thread they also caught an unintended decimal (337.5) and missing answer diagrams. They asked for a very thorough review of every piece of material: typos, mathematical errors, diagram inaccuracies, and "distorted ideas" that look fine but confuse students or weaken learning. They are happy to use many subagents as independent reviewers.

Proposed (awaiting Shashi's go-ahead): five independent checkers working from the compiled PDFs: maths re-solve, diagram vs text, student simulation (average and weak Grade 9), teaching quality, and proofreading plus student/fc consistency. After any fix, run a full re-check and a text diff of old vs new. Send a short review note with each sheet.

**Why:** errors in student material confuse students and the teacher, and Shashi treats this as serious.
**How to apply:** never use global find-and-replace on numbers in .tex files. After any edit, re-check all pages of both copies. Use the review gate before delivering. Related: [[feedback-use-smaller-subagents]]

Update 2026-10-11: Shashi agreed to the review gate and added three rules.
(1) Exercises must test the learning objective from many angles: working backwards, explaining, finding a mistake, drawing, comparing or "what if", real context. At most one question per set may be plain substitution.
(2) Every example and question must say explicitly what to find. Class 2 Example 3.1 gave a calculation but never asked anything.
(3) Facilitator copies must be plain and usable by other teachers. No internal jargon such as "TikZ", "trap", "invariant" or "structural". Use the core rules of Simplified Technical English (ASD-STE100): short sentences, active voice, one instruction per sentence, consistent terms. A sixth checker (language) is added.
Proposed next steps, awaiting go-ahead: write a review checklist file, trial it on homework 2, then revise class 2.
````

**feedback-haiku-subagents.md**

````markdown
---
name: feedback-haiku-subagents
description: Shashi wants Haiku (xhigh effort) subagents for drudgery work and a lean review process to save usage
metadata:
  type: feedback
---

On 2026-10-11 Shashi said the multi-round review with many agents used too much usage. They want work "lean and robust": use Haiku subagents at xhigh effort for most drudgery work (drawing diagrams, re-solving answers, mechanical checks), and the main session reviews their output.

Lean review (agreed): write sheets with the checklist rules from the start; one independent checker per sheet (cheap model) re-solves every answer and checks diagram labels; main session does teaching/language review and looks at every page; one round only, second round only if a maths error is found.

**Why:** usage cost. **How to apply:** default to Haiku (effort xhigh) for subagents; no multi-agent review rounds. Related: [[feedback-strict-review-of-materials]], [[feedback-use-smaller-subagents]]
````

### 2.3 Laptop Claude Code memory for the tuition folder (word for word)

Claude Code on the laptop keeps its own memory for `E:\tuition content`, separate from the project memory above. It lives in `C:\Users\Krishnanvp\.claude\projects\E--tuition-content\memory\`. It was read on 27 October 2026 and is copied here word for word.

**MEMORY.md**

```
- [G9 Perimeter & Area chapter](g9-perimeter-area-chapter.md) — Ganita Manjari Ch 6 scope, source PDF, MCQ paper conventions
- [Maths sheet house style](maths-sheet-house-style.md) — plain B/W exam look, Schola font, title|label + rule, grey figures, student + fc copies
- [Helper models](command-code-subagents.md) — Command Code default, Codex backup/heavy; ask Shashi to OK the model plan first
- [FC formal language](fc-formal-language.md) — formal academic wording in fc copies; Opus re-checks wording and diagrams before delivery
```

**command-code-subagents.md**

```
---
name: command-code-subagents
description: "In this project, use Command Code models (DeepSeek 4.1 Flash, Muse Spark 1.3) via delegate.sh instead of Claude subagents for drudgery"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ea17ccd5-5736-4bf2-85ab-ee1369252de1
  modified: 2026-10-22T13:24:36.563Z
---

For tuition-content work on this laptop, drudgery (LaTeX, TikZ, re-solving, formatting) goes to
`bash /c/Users/Krishnanvp/bin/delegate.sh`, default `deepseek/deepseek-v4.1-flash`, alternate
`meta/muse-spark-1.3-contributor`. Not Sonnet/Haiku subagents. Main Claude reviews all output.

Backup: `bash /c/Users/Krishnanvp/bin/codex.sh` — `gpt-5.6-luna` drudgery, `gpt-6.1-sol`/`gpt-5.6-sol` very high intellectual work.
Before using any helper, post a short model-per-job plan and wait for Shashi's OK.

Speed (2026-10-12): one DeepSeek job building a whole 21-question test + fc took ~25 min. Shashi
suggested splitting: 2-3 DeepSeek jobs in parallel, each writing one section's LaTeX fragment
(questions, figures, answers), then one job (or me) assembling and compiling. Do this for big papers.

2026-10-22: Shashi wants DeepSeek in fast mode (`deepseek/deepseek-v4.1-flash-fast`) by default. A whole-deck
DeepSeek job hit the 10-min timeout and lost its API connection; when class is minutes away, finish small edits myself.

**Why:** Shashi wants to save Claude usage; set up and tested 2026-10-11 (both models produced compiling TikZ).
**How to apply:** Overrides the project-settings note that says "Sonnet or Haiku subagents". See E:\tuition content\CLAUDE.md and command-code-helpers.md. Related: [[maths-sheet-house-style]].
```

**fc-formal-language.md**

```
---
name: fc-formal-language
description: "Facilitator (fc) copies use formal academic language; main model personally reviews questions, wording and diagrams before sending"
metadata:
  node_type: memory
  type: feedback
  originSessionId: e2ca1f5c-9a37-4ab9-b92d-e69743a90ac0
  modified: 2026-10-12T11:37:55.779Z
---

FC teacher notes and worked answers must use formal academic language ("Concepts assessed", "Common misconceptions", "perpendicular height", "Paper design", "Marking"), not casual words like "ideas tested", "slips", "Equal.". Other teachers read these copies.
Before anything is pushed to Shashi, the main model (Opus) itself re-checks every question's sentence framing, every diagram and every answer, on top of the helper re-solve.

**Why:** Shashi flagged "ideas tested" in the Test 2 fc (2026-10-12) and asked for an Opus check of wording and diagrams before delivery.
**How to apply:** all fc copies and question papers. See [[maths-sheet-house-style]], [[command-code-subagents]].
```

**g9-perimeter-area-chapter.md**

```
---
name: g9-perimeter-area-chapter
description: "Grade 9 tuition — NCERT Ganita Manjari (2026) Ch 6 \"Measuring Space: Perimeter and Area\"; source PDF, scope, and MCQ-paper conventions"
metadata:
  node_type: memory
  type: project
  originSessionId: d6e79114-da03-4932-9536-9da98458b895
  modified: 2026-09-28T01:57:46.348Z
---

The user tutors Grade 9 from the new NCERT book *Ganita Manjari, Grade 9, Part I*. Chapter 6 PDF is `E:\tuition content\g9 perimeter and area ch6.pdf` (sections 6.1–6.10: circumference, π history/irrationality, arc length, 400 m track staggers, parallelogram/triangle area, median theorem, Heron, Brahmagupta cyclic 4-gon, Baudhāyana squaring a rectangle, circle and sector area).

Earlier work (Sept 2026, partly in ChatGPT): Class 1 and Class 2 student/facilitator copies, Test 1, and a 12-question MCQ draft.

MCQ paper conventions the user set: title is just "Perimeter and Area", questions start immediately (no instructions block); answer key/worked solutions is a separate document; competency-based, CBSE item-bank style, Indian context.

**Why:** these conventions came from the user's school brief and their earlier sessions.
**How to apply:** reuse for any further question papers on this chapter; see [[latex-default]] (global CLAUDE.md) for format.
```

**maths-sheet-house-style.md**

```
---
name: maths-sheet-house-style
description: "The user's house style for every maths teaching sheet, worksheet, MCQ set or homework (LaTeX + PDF) — look, headings, figures, copies, file names"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d6e79114-da03-4932-9536-9da98458b895
  modified: 2026-10-10T10:44:21.280Z
---

Every maths sheet follows this house style (user pasted it 2026-10-10; it overrides the math-lesson-builder skill's blue design system, which the user rejected for these sheets):

- **Look:** plain printed-exam-paper look, black on white. No coloured boxes, no coloured headings, no colour words in questions (sheets are printed black-and-white; figures must read in greyscale — use dashes/shading, never colour, to distinguish shapes).
- **Font:** Century Schoolbook — `tgschola` text + `fouriernc` maths, `\linespread{0.97}` (wide font, tight lines).
- **Heading:** short title left, short label (e.g. "Class 2", "Set 2") or date right, one thin rule under it. Nothing else.
- **Notes / Things to Remember:** between two thin grey rules, never shaded boxes.
- **Diagrams:** TikZ, true measurements, dark grey lines, soft grey fills, right-angle marks on heights, dashed lines visibly dashed. Never split a diagram (or an exercise heading) from its question.
- **Maths:** fractions always display size; mixed numbers clearly readable; rupee symbol (₹40).
- **Assignments/homework:** heading "Assignment" left + date right. Never print difficulty labels or topic titles; easy→hard order is internal only. If a question has no diagram, tell students to draw a rough figure and mark all given measurements; sometimes make drawing it part of the question.
- **Questions:** CBSE competency-based, easy→hard, mostly Indian/South Indian everyday settings in plain English, no regional words students may not know.
- **Copies:** student copy (questions only) + facilitator copy (worked answers in smaller grey text, plus teacher notes). Names "<name> N" and "<name> N fc", .tex and .pdf. Check every page visually after compiling.

**Why:** the user's established style across their teaching-notes work (Cowork project).
**How to apply:** default for all new sheets. For the BIO LEARNING CENTER MCQ sets (spelled CENTER; name centred on its own top line, then "Perimeter and Area" left and "Set N" right) the user chose their own names ("set N perimeter area", "set N solution perimeter area") — keep those for that series. The MCQ toolchain in `perimeter-area-mcq/` already implements this style (`preamble.tex`, `\sheethead`, `\drawprompt`, `+draw` flag in selection files). See [[g9-perimeter-area-chapter]].
```

Note on line spacing: the laptop memory says `\linespread{0.97}`, but the Class 2 files use `\linespread{1.04}` and the homework files use `\linespread{1.08}`. Match the file you are working on; for a new sheet of an existing kind, copy that kind's preamble.

### 2.4 Memory entries that later decisions replaced

Some older memory entries are no longer the rule. Follow the newer rule.

| Older entry | Replaced by | Date of change |
|---|---|---|
| feedback-strict-review-of-materials: five, then six, independent checkers per sheet, full re-check after every fix | Lean quality bar: one cheap independent checker, one round, a second round only if a maths error is found; main model does the teaching and language review and a final look at every page | 11 Oct 2026 (Shashi stopped the 6-checker review after about 1.6 million tokens) |
| feedback-use-smaller-subagents: "smaller-model subagents (Sonnet)" | On the laptop: Command Code (DeepSeek 4.1 Flash, Muse Spark 1.3), Codex as backup. In the cloud: Haiku at effort xhigh | 11 Oct 2026 |
| Project instructions, MEMORY.md and feedback-haiku-subagents: "In the cloud: Haiku subagents (effort xhigh)" | Cloud sessions use the Command Code models (DeepSeek 4.1 Flash, Muse Spark 1.3) through `/usr/local/bin/delegate.sh`; Haiku only if Command Code fails | 27 Oct 2026 (tested and working) |
| Laptop memory: DeepSeek fast mode by default | Ask Shashi every time DeepSeek 4.1 Flash is used whether to use fast mode | 27 Oct 2026 |
| feedback-assignment-layout-and-design and the 8 Oct homework 1: font "Palatino" | Century Schoolbook (`tgschola` + `fouriernc`) | 8 Oct 2026 |
| Early Class 2 and homework 1 style: blue headings, pale-blue boxes, "Warm-up / Think it through / Challenge" sections | Plain house design, no difficulty labels, no question titles | 8 Oct 2026 |
| Early file names such as "Chapter-6-Perimeter-Class-2-Student.tex" | "class 2", "class 2 fc", "homework 1", "homework 1 fc", and so on | 8 Oct 2026 |
| MEMORY.md "Default device for Remote Control: environment_id env_01MvLkQgcViMNAiUEzxQHuip" | On 27 Oct 2026 the device list shows the laptop's `E:\tuition content` folder served by environment `env_01W4F84ejdGM7kF5bdZ9R3bj`. Check `list_devices` before using an id from memory. | Observed 27 Oct 2026 |
| MEMORY.md "Homework 2 (sections 3-4 + median theorem) started 2026-10-11" | Homework 2 was finished and saved to Drive on 11 Oct 2026 (also stated later in MEMORY.md) | 11 Oct 2026 |
| MEMORY.md "Class 2 ... student 10 pp, fc 13 pp" | After the 11 Oct revisions Class 2 grew: 12 pp / 19 pp after the exercise rewrite, then 14 pp / 21 pp after the worked-example format change | 11 Oct 2026 |
| feedback-use-smaller-subagents links to `[[consult-before-producing]]` | No memory file of that name exists. The rule itself is in MEMORY.md ("consult first and get the lesson plan approved before producing the document") | n/a |

---

## 3. Workflows, step by step

### 3.1 Where the work runs

1. **Default: Shashi's laptop.** Start every new work thread as a Remote Control session on the laptop folder `E:\tuition content` (Shashi's rule, 11 Oct 2026). Shashi follows it from the phone. The laptop sessions read `CLAUDE.md` and `command-code-helpers.md` in that folder and can call the Command Code and Codex helper models.
2. **Fallback: the cloud.** Use a cloud thread only when the laptop is offline, and say so. In the cloud the helper models are the same Command Code models (DeepSeek 4.1 Flash, Muse Spark 1.3) through `/usr/local/bin/delegate.sh`; Haiku subagents at effort xhigh only if Command Code fails. Codex is laptop-only. A cloud thread cannot move to the laptop once it has started.
3. **Speed exception.** When Shashi is about to teach and time is critical (22 Oct 2026, "class in 4-5 minutes"), a fast cloud thread may be used to deliver a usable PDF at once. Say plainly that it was checked only once.
4. The laptop must be on, with the Claude desktop app open, for laptop work to run. If a laptop session drops, tell Shashi in one line and continue when it is back.

### 3.2 General working protocol for every task

1. Read project memory, the project instructions and the skills working-with-shashi and shashi-global-rules.
2. Read the existing material for the chapter (class notes, earlier homework and tests) so new work stays within what has been taught and does not repeat earlier questions.
3. For anything larger than a quick answer, post a short plan first and wait for Shashi's OK. Ask questions that can be answered in one word, give options on short lines and mark the recommended one. For small undecided details, pick a sensible default, say which, and continue.
4. Before using helper models, post a 2-3 line plan of which model does which job and ask Shashi to confirm. **Every time** DeepSeek 4.1 Flash is used, ask Shashi whether to use fast mode (Shashi's rule, 27 Oct 2026). Do not assume it from an earlier task. (On 22 Oct 2026 Shashi chose fast mode for that task: "things get done faster".) Muse Spark has no fast mode.
5. Do the planning, question design and judgement yourself (main model). Send drudgery (LaTeX, TikZ diagrams, re-solving, compiling, formatting) to helpers with precise specs. For long builds, split the work: 2 or 3 DeepSeek jobs side by side, each writing one section with its figures and answers, then one job (or the main model) assembles and compiles (Shashi's suggestion, 12 Oct 2026).
6. Review everything helpers produce: compile, look at every page and diagram, compare answers with an independent re-solve. Fix small issues yourself.
7. Final check by the main model before anything reaches Shashi: look once more at every diagram, every question and how each question sentence is framed (Shashi, 12 Oct 2026).
8. Share the PDFs in the thread first. Save to Google Drive only after Shashi says OK. Exception: when Shashi is on the phone they may say "push it to Drive" so they can check there.
9. Keep a copy of the old version when replacing a file. When Shashi approves the final version, clean old versions and scratch files on request, and say what was kept.
10. Keep the progress checklist current. When Shashi asks "done?" or "status?", answer honestly in one or two lines: what is finished and what is left.
11. When Shashi corrects something or states a new preference, save it to project memory in that same turn. A general rule about how to work goes into an updated version of the working-with-shashi skill, proposed on a review card at the end of the work.

### 3.3 From a chapter to a class sheet (student copy and fc copy)

This is the math-lesson-builder workflow (Appendix C) with Shashi's rules applied.

1. **Read** the request, the textbook chapter (NCERT Grade 9), the required examples, exercises and theorems, and Shashi's earlier materials for the chapter.
2. **Consult.** Ask grouped questions about every open choice: class number, time, readiness, what was already taught, scope (included and excluded), sequence, examples, diagrams, proofs, practice, facilitator notes, file names and destination. Do not ask again what is already answered.
3. **Agreed brief.** Present a compact brief and lesson route: class destination, included and excluded content, prerequisites and misconceptions, sequence with timing, planned diagrams, examples, proofs and practice, document structure, output files and destination, assumptions.
4. **Wait for approval.** Do not start the document until Shashi approves the brief (project rule).
5. **Helper plan.** Post which model does which job and get Shashi's OK.
6. **Write the content** with the checklist rules applied from the start:
   - Concrete or visual experience first, then observation, precise language, symbols, justification, application.
   - Every example and question states exactly what to find ("Find ...", "Explain ...", "Draw ...").
   - Every worked example models the solution format taught to students: a rough diagram with the given measurements marked (and "?" on the unknown), a **Given:** line, a **To find:** line, a **Solution.** with steps and a short reason for each key step, and an **Answer:** with units.
   - Each exercise set tests the learning objective from several angles: working backwards, explaining why or true/false, finding the mistake, drawing, comparing or "what if", real-life application. At most one plain-substitution question per set, and it comes first.
   - Easy to hard. Indian and South Indian settings in plain English. Whole-number answers unless decimals are the point.
7. **Build one source file.** Write a single LaTeX body with `\ifteacher` switches (Section 5.4). The student copy and the fc copy come from the same source, so the questions match word for word.
8. **fc layer.** Add a short "Teacher's copy: overview" (aims, before the class, if time is short, exercises). Add answers in smaller grey text with step-by-step working and a rough answer diagram for every question. Add a "Note for the teacher" only where it is truly needed. Add a "Common mistake" only when the mistake is genuinely likely and knowing it changes what the teacher does (the sloping side used as the height is the model). Write teacher-facing text in formal, academic, simple English (ASD-STE100 core rules).
9. **Compile** both copies with pdfLaTeX at least twice. Render every page and look at it.
10. **Independent check (lean).** One cheap checker re-solves every answer and compares every diagram label with the text. The main model does the teaching and language review. One round. A second round only if a maths error was found.
11. **Fix** every real problem by hand, in place. Never use global find-and-replace on numbers. Rebuild both PDFs and look at every changed page in both copies.
12. **Final main-model look** at every diagram, question and sentence.
13. **Share** both PDFs in the thread with a short note: what was checked, what was found, what was fixed. List style suggestions separately for Shashi to accept or ignore.
14. **Save** to Drive only after Shashi's OK (Section 4).
15. **Update memory** with the class progress and anything Shashi corrected.

### 3.4 Homework / assignment sheets

1. Confirm the exact point taught up to (for example "up to Exercise 6.2A", or "up to Think and explain after Theorem 1").
2. Read the class notes up to that point, plus Class 1, earlier homework and tests, so nothing beyond the syllabus appears and nothing repeats.
3. Draft the questions with worked answers as a short draft (Markdown in `/mnt/project-files/<folder>/` or in the laptop folder) and list them for Shashi in plain words: number, setting, what it tests. Shashi's usual shape: the first few easy and approachable (only a few), the middle "refreshing" and good, the last one or two challenging.
4. Apply the question rules: CBSE competency-based, not direct formula use; Indian settings in plain English; whole-number answers; explicit "find" line; a mix of angles; some questions require drawing the diagram as a marked part.
5. After approval, build the student and fc copies (Section 5).
6. Student copy layout: "Assignment" on the left and the date on the right, one thin rule, then one italic line telling students to draw a rough diagram for every question and write every step. No section labels, no difficulty labels, no question titles.
7. fc copy: a short teacher overview of the ideas used (in formal language), answers under each question in smaller grey text, and a rough answer diagram for every question.
8. Lean check, final main-model look, share, then save to Drive after OK.

### 3.5 Tests

1. Confirm scope: which topics are included and excluded. Ask about topics that may not have been taught (for Test 2, Heron's formula was taught; Brahmagupta's formula and Baudhāyana's squaring of a rectangle were not).
2. Use the CBSE board-paper layout, scaled to the marks. Test 2 (50 marks) used:
   - A: 8 × 1 = 8 (6 MCQs and 2 assertion–reason, with the standard CBSE assertion–reason instruction)
   - B: 4 × 2 = 8
   - C: 4 × 3 = 12
   - D: 2 × 5 = 10
   - E: 3 case studies × 4 = 12 (parts worth 1 + 1 + 2, with an OR choice in two of them)
3. Questions must genuinely test understanding and application, not plugging in values. Only a few easy, approachable questions at the start (Test 2 had only 3 direct questions out of 21).
4. Look at the earlier test (Test 1) for format and avoid repeating its questions.
5. The main model writes the questions and answers. Muse Spark re-solves them without seeing the answers. DeepSeek builds the LaTeX and diagrams.
6. fc copy headings that Shashi approved: **Paper design**, **Competency focus**, **Concepts assessed**, **Common misconceptions**, **Marking**. Answers in full sentences, formal wording (for example "the perpendicular from A to CB produced" instead of "the height falls outside").
7. Files: "test N" and "test N fc".

### 3.6 Slides for teaching on the iPad

1. Format: a 16:9 slide PDF made with LaTeX Beamer in the house style (Century Schoolbook, plain black and white, grey figures). It opens in GoodNotes, Notability, Apple Books or Files on the iPad, so Shashi can write on it.
2. One question per slide at the top, with the rest of the slide blank for working.
3. Add **teaching slides** that show an idea visually (for example the circle cut into slices and rearranged into a parallelogram or near-rectangle to show πr × r = πr²; a slide with the sector and segment formulas).
4. Add **practice slides** that show a bunch of questions together, numbered, so students can copy them and solve on their own.
5. A separate fc deck ("... slides fc") with a worked-answer slide after each question.
6. When time is short, ship a usable draft first and say what was not yet checked; then add the rest and send the final version.
7. To get a PDF onto the iPad: save it to the Drive folder (laptop `G:` folder); on the iPad open the Google Drive app, tap the file, tap ⋯ → Open in → GoodNotes or Notability.

### 3.7 Revising an existing file

1. Work on copies (in the laptop folder or `/mnt/project-files/`). Do not overwrite Drive files until Shashi has seen the PDFs and said OK.
2. Change only what was asked. Keep approved and already-taught parts as they are unless something there is wrong.
3. Never blind find-and-replace numbers or words. Edit each place by hand.
4. Rebuild both copies and look at every page of both, not only the changed page.
5. Compare old and new text so only the intended changes got through.

### 3.8 Reviews and reports for Shashi

- Deliver reviews with pictures as **one self-contained PDF**. A Markdown file with separate image files does not render in the previewer (8 Oct 2026).
- For each problem: where, what is wrong, why it matters, proposed fix. Group into "Must fix" and "Should improve".

### 3.9 Non-tuition requests in this project

- **Prerana (Prayoga) activity.** Shashi's maths team runs a 90-minute indoor, group-based activity for Grade 9 students on **30 October 2026**. It is a side activity; the main activity that day is biology, but the maths activity has **nothing to do with biology** (Shashi corrected this). Four ideas are on the table: 1 Build shapes and find the hidden rule (Euler's rule, recommended), 2 Win every time (strategy game, multiples of 4), 3 Maths escape room, 4 Catch pi with your own hands. Shashi asked for the core idea and what students do for each; that was given. The thread is waiting for Shashi to pick one, then a full plan follows.
- **IB and IGCSE.** A two-page overview PDF was made (`/mnt/project-files/ib-igcse-overview.pdf`). Shashi wants to learn the maths to broaden their teaching. Advice given: start with Cambridge IGCSE 0580 Extended, then IB DP Mathematics AA SL. An offer to make a topic checklist and a 10-week study plan is open, with no answer yet.
- When explaining activities or unfamiliar ideas, give the core idea, what works and why, and what students are expected to do, in plain words.

---

## 4. File naming, folder layout and Google Drive

### 4.1 File naming (Shashi's rule, 8 Oct 2026)

- Student copy: `<name> N`. Facilitator (teacher) copy: `<name> N fc`. Each as `.tex` and `.pdf`.
- Examples: `class 2.tex`, `class 2.pdf`, `class 2 fc.tex`, `class 2 fc.pdf`; `homework 1` / `homework 1 fc`; `homework 2` / `homework 2 fc`; `test 1` / `test 1 fc`; `test 2` / `test 2 fc`.
- Slides followed the same idea: `6.3A slides.pdf` and `6.3A slides fc.pdf`; the quick cloud deck was `circle area slides.pdf`.
- `practice-questions.pdf` in the chapter folder was not renamed. Shashi said there was no need.
- Exception: the BIO LEARNING CENTER MCQ series uses Shashi's own names: `set N perimeter area` and `set N solution perimeter area` (.tex and .pdf). Keep those for that series. Their heading: "BIO LEARNING CENTER" centred on its own top line, then "Perimeter and Area" on the left and "Set N" on the right.
- MCQ paper conventions: title is just "Perimeter and Area", questions start immediately (no instructions block), the answer key / worked solutions is a separate document, competency-based CBSE item-bank style, Indian context.
- Use lowercase names with spaces exactly as above. Do not change a name Shashi gives.

### 4.2 Google Drive layout

- Top folder: **Tuition_grade9,10** (Drive folder id `1qszlXOHCttHHiYTIHfJHLLzFXqzCBZwP`). Memory also calls it "tuition 9 10".
- One subfolder per chapter. Chapter 6: **Perimeter and area (g9, ch6)** (Drive folder id `1GyNyZlcFLsVkoSPMUvU42g-hiF9uWJ48`).
- Contents of the Chapter 6 folder, as last known:
  - `class 1.pdf`, `class 1 fc.pdf` (PDF only, no .tex, old style; a restyle was offered but not requested)
  - `class 2.tex/.pdf`, `class 2 fc.tex/.pdf` (latest version: 11 Oct 2026, with the worked-example format; student 14 pages, fc 21 pages)
  - `homework 1.tex/.pdf`, `homework 1 fc.tex/.pdf` (up to Ex 6.2A, 8 Oct 2026)
  - `homework 2.tex/.pdf`, `homework 2 fc.tex/.pdf` (sections 3-4 and the median theorem, 11 Oct 2026)
  - `test 1.tex/.pdf`, `test 1 fc.tex/.pdf`
  - `test 2.tex/.pdf`, `test 2 fc.tex/.pdf` (50 marks, 12 Oct 2026; student 5 pages, fc 10 pages)
  - `practice-questions.pdf`
  - `circle area slides.pdf` (quick 18-slide deck, 22 Oct 2026)
  - `6.3A slides.pdf` and `6.3A slides fc.pdf` were finished on 22 Oct 2026, but saving them to Drive was **not confirmed**. Ask Shashi or check the folder.

### 4.3 How to save to Drive

- **Preferred route:** Shashi's laptop runs Google Drive for desktop. The Drive folder appears at `G:\My Drive\Tuition_grade9,10`. Save finished PDFs and .tex files into `G:\My Drive\Tuition_grade9,10\Perimeter and area (g9, ch6)` from a laptop session (or with device folder tools) and Drive syncs them.
- The **Google Drive connector** can upload `.tex` (plain text) but **not PDFs**: it needs the file contents written out inline, and PDFs are far too large. It can rename files (`update_file` with a new title). The device folder tools cannot rename.
- When a file with the same name is still present during sync, Drive for desktop may add " (1)" to the name. Check and fix it.
- Ask before replacing originals. When Shashi chooses "Replace originals", move the old files to the Drive trash (restorable for 30 days) or keep a backup copy.

### 4.4 Laptop folders

| Folder | Use |
|---|---|
| `E:\tuition content` | Default working folder for laptop sessions. See the listing below. |
| `G:\My Drive\Tuition_grade9,10` and `...\Perimeter and area (g9, ch6)` | Google Drive for desktop; the delivery destination. |
| `E:\scratch_pad`, `E:\Learning - Slack-free Exactness` | Other folders on the laptop, not part of this project. |

Listing of `E:\tuition content` (27 Oct 2026, top level and one level down; build files such as .aux and .log omitted here):

- `CLAUDE.md`, `AGENTS.md`, `command-code-helpers.md`: rule files (Section 6).
- `g9 perimeter and area ch6.pdf`: the textbook chapter.
- `Chapter-6-Perimeter-Class-1-Facilitator.tex/.pdf`, `Chapter-6-Perimeter-Class-1-Student.tex/.pdf`: Class 1 sources under the old names. (Drive has Class 1 as PDF only, so the .tex exists only here.)
- `class2-format/`: the 11 Oct worked-example revision of Class 2 (`class 2.tex/.pdf`, `class 2 fc.tex/.pdf`, plus `resolve` and `work` folders).
- `exercise-6.3a-slides/`: the iPad slides (`slides.tex`, `slides fc.tex`, `SPEC.md`, `class2-reference.tex`, `6.3A slides draft.pdf`, `6.3A slides.pdf`, `6.3A slides fc.pdf`, page images).
- `perimeter-area-test2/`: Test 2 (`spec.md`, `questions.md`, `answers.md`, `style-model.tex`, `test 2.tex/.pdf`, `test 2 fc.tex/.pdf`).
- `perimeter-area-mcq/`: the BLC MCQ toolchain and sets (`BRIEF.md`, `REVIEW.md`, `preamble.tex`, `bank`, `selection*.txt`, `tools`, `verify`, `tasks`, `source`, `logs`, five question banks by topic, `perimeter-and-area-mcqs`, `perimeter-and-area-question-bank`, `perimeter-and-area-solutions`, `exemplars`, and `set 1/2/3 perimeter area` with `set 1/2/3 solution perimeter area`, each .tex and .pdf).
- `reference/ib-igcse-overview/`: source of the IB/IGCSE overview.

### 4.5 Project shared folder (`/mnt/project-files/`)

Used by cloud threads. Contents relevant to this project:

- `perimeter-area-class2-review/`: the 8 Oct diagram review (`diagram-review.pdf`, `diagram-review.md`, current-diagram images) and the first fixed Class 2 files (`revised/Chapter-6-Perimeter-Class-2-*.tex/.pdf`).
- `perimeter-area-class2-homework/`: homework 1 draft, final files under old names (`final/Chapter-6-Perimeter-Class-2-Homework-Student/Facilitator.*`), and the two font comparison PDFs.
- `perimeter-area-class2-restyle/`: Class 2 in the house design, before the 11 Oct revision (kept as the old version).
- `perimeter-area-class2-homework2/`: homework 2 (`homework 2.tex/.pdf`, `homework 2 fc.tex/.pdf`), the draft and the three review-round inputs.
- `perimeter-area-class2-revised/`: Class 2 after the 11 Oct exercise revision: `body-source.tex` (single source with `\ifteacher`), `class 2.tex/.pdf`, `class 2 fc.tex/.pdf`. **Note:** the later worked-example format revision (same day) was done on the laptop and is in Drive. The Drive copy is the newest.
- `review-standard/review-checklist.md`: the review checklist (Appendix D).
- Top level: `class 2.pdf`, `class 2 fc.pdf`, `test 2.pdf`, `test 2 fc.pdf` (plus earlier time-stamped test 2 versions), `6.3A slides draft.pdf`, `6.3A slides.pdf`, `6.3A slides fc.pdf`, `circle-area-slides-quick/circle area slides.pdf`, `ib-igcse-overview.pdf`, and this handbook under `handbook/`.

Rules for this folder: put new files in a subfolder, read a shared file again just before changing it (other threads write here too), and attach files in replies so they appear in Shashi's Library.

---

## 5. LaTeX setup

### 5.1 Engines and compiling

- **Laptop:** MiKTeX 24.1: `pdflatex` (MiKTeX-pdfTeX 4.18, pdfTeX 1.40.25 in the PDF metadata), `xelatex` and `lualatex` are also installed. All sheets so far use `pdflatex`.
- **Cloud:** TeX Live, installed when needed. Century Schoolbook needs the `tex-gyre` and `texlive-fonts-extra` packages (for `tgschola`, `fouriernc` and `tfrupee`).
- Compile with `pdflatex` at least twice (more if references are unresolved). For each copy:

```
pdflatex -interaction=nonstopmode "class 2.tex"
pdflatex -interaction=nonstopmode "class 2.tex"
pdflatex -interaction=nonstopmode "class 2 fc.tex"
pdflatex -interaction=nonstopmode "class 2 fc.tex"
```

  (The exact command line used on the laptop is not recorded in the project files. The two-pass pdfLaTeX rule comes from the math-lesson-builder skill.)
- After compiling, render every page to an image (for example `pdftoppm -png -r 80 "class 2 fc.pdf" page`) and look at each page: overfull boxes, clipped text, broken symbols, crowded diagrams, labels on lines, headings stranded at the bottom of a page, a diagram split from its question, unnecessary blank space.
- Check embedded fonts with `pdffonts`: expect CenturySchL (or TeXGyreSchola), Fourier-Math and RupeeTechFat.

### 5.2 House design (default for all sheets since 8 Oct 2026)

- A4 portrait, 11 pt `article`. Plain, elegant, exam-paper look.
- Font: Century Schoolbook: `\usepackage{tgschola}` and `\usepackage{fouriernc}` (maths), with `\usepackage[T1]{fontenc}` and `\usepackage{microtype}`.
- Line spacing tight because the font is wide: `\linespread{1.04}` for class notes, `\linespread{1.08}` for homework. (The laptop memory says `\linespread{0.97}`; match the file you are working on.)
- Sheets are printed in black and white: figures must read in greyscale. Use dashes or shading, never colour, to tell shapes apart, and never use colour words in questions.
- Black text. Accent colour slate `RGB(38,52,70)` for theorem/example labels, exercise headings and main diagram lines. Panel grey `RGB(236,238,241)` (class notes) or `RGB(233,236,240)` (homework) for soft diagram fills. Muted grey `RGB(70,72,76)` for teacher answers.
- No coloured boxes. Notes, "How to use this companion", "Things to Remember" and teacher notes sit between two thin grey rules. In Class 2 this is done by redefining `\colorbox` to draw two `black!35` rules.
- Heading: title on the left, a short label on the right ("Class 2", or the date on an assignment), one thin rule (0.6 pt) underneath. Nothing else: no module title block, no class name, no descriptor.
- Section headings plain black bold (`titlesec`).
- Fractions always full size with `\dfrac`; mixed numbers must read clearly. Never small inline fractions.
- Rupees: `\usepackage{tfrupee}` and `\rupee\,$40$` gives ₹40.
- Diagrams in TikZ, drawn to correct measurements, dark grey/slate lines, soft grey fills, right-angle marks on heights, dashed lines truly dashed (no solid line drawn on top), labels not touching lines, units on every length.
- Keep every exercise heading with its questions (`\Needspace{7\baselineskip}` in the exercise environment) and never split a diagram from its question (`\Needspace` before each question).
- Teacher answers in smaller grey text (`\small`, `\color{muted}`, line spread 1.15).
- Watch the page count: Class 2 student copy was kept at 10 pages after the restyle by tightening line spacing.

### 5.3 Packages used

Class notes (`class 2`): `geometry` (margin 2.3 cm), `amsmath`, `amssymb`, `amsthm`, `fontenc` (T1), `tgschola`, `fouriernc`, `microtype`, `tfrupee`, `xcolor`, `titlesec`, `tikz` (libraries `angles`, `quotes`, `calc`, `arrows.meta`), `enumitem`, `needspace`, `fancyhdr`, `hyperref` (hidelinks), `comment` (student copy only).

Homework (`homework 1`, `homework 2`): `geometry` (margin 2.4 cm, top 2.2 cm), `amsmath`, `amssymb`, `tgschola`, `fouriernc`, `fontenc` (T1), `tfrupee`, `microtype`, `xcolor`, `tikz` (same libraries), `enumitem`, `needspace`, `comment` (student copy only).

Slides (`6.3A slides`): LaTeX Beamer, 16:9 (page size 16 cm × 9 cm), Century Schoolbook with Fourier maths. The source is `E:\tuition content\exercise-6.3a-slides\slides.tex` and `slides fc.tex`.

BLC MCQ sets: a shared `preamble.tex` in `E:\tuition content\perimeter-area-mcq\` with a `\sheethead` macro for the heading, a `\drawprompt` macro for "draw a rough diagram" prompts, and a `+draw` flag in the selection files that adds that prompt to a question. That preamble was not copied into this handbook; read it on the laptop before making a new set.

### 5.4 One source, two copies (`\ifteacher`)

Both copies are built from one body. The only difference is the first line:

```
\newif\ifteacher\teacherfalse   % first line of "class 2.tex"   (student copy)
\newif\ifteacher\teachertrue    % first line of "class 2 fc.tex" (facilitator copy)
```

Everything after that line is identical (`body-source.tex` has no first line; prepend one of the two lines to make each copy). Inside the body:

- `answerblock` environment: in the fc it prints "Answers." / "Answer." in small muted grey; in the student copy it is removed with `\excludecomment{answerblock}` from the `comment` package.
- `\ans{1.}` (class notes) or `\ap{b}` (homework) start each numbered answer or part answer.
- `\facilitatornote{...}`: in the fc prints "Note for the teacher." between grey rules; in the student copy it prints nothing.
- `\ifteacher ... \else ... \fi` blocks for the teacher overview (fc) and "How to use this companion" (student).

This keeps every question word-for-word identical in both copies.

### 5.5 Environments and macros (class notes)

- Theorem styles `brand` (italic body) and `branddef` (upright), headings bold in the accent colour; `theorem`, `corollary`, `definition`, `example` (numbered by section), `illus`, `remark`, `activity`.
- `exercise{6.2A}`: large bold accent heading "Exercise 6.2A", then an enumerate list (`leftmargin=*`, `itemsep=4pt`).
- `\rememberbox{...}`: "Things to Remember".
- `\tr` for the triangle symbol. `\nl` for a line break with 3 pt space inside answers.
- Homework: `hwq` environment (bold numbered questions that continue across environments) and `parts` list ((a), (b), ...).

The full preambles are in Appendix E. The math-lesson-builder template and design reference (Appendix C) are the origin of these environments; the house design changes its font and colours.

---

## 6. Helper models and the exact commands

The text below was read directly from Shashi's laptop on 27 October 2026 (read-only). The two rule files and the two launcher scripts are copied word for word.

### 6.1 Summary: which model does which job

| Where | Job | Model | Model id | How to call |
|---|---|---|---|---|
| Laptop | Routine work: LaTeX, TikZ diagrams, formatting, bulk edits, building slide decks | DeepSeek 4.1 Flash (default helper) | `deepseek/deepseek-v4.1-flash`; fast mode `deepseek/deepseek-v4.1-flash-fast` (Shashi's choice since 22 Oct 2026) | `delegate.sh` |
| Laptop | Second model; independent re-solve of every answer to cross-check | Muse Spark 1.3 contributor (no fast mode) | `meta/muse-spark-1.3-contributor` | `delegate.sh -m ...` |
| Laptop | Free fallbacks (not yet used in this project) | LongCat 2.0, Laguna S 2.1 | `meituan/longcat-2.0:free`, `poolside/laguna-s-2.1-free` | `delegate.sh -m ...` |
| Laptop | Backup for routine work when Command Code is down or struggling | GPT 5.6 Luna | `gpt-5.6-luna` | `codex.sh` |
| Laptop | Very high intellectual work: hard question design, tricky proofs, checking a whole answer key, deep maths or teaching review | GPT 6.1 Sol or GPT 5.6 Sol | `gpt-6.1-sol`, `gpt-5.6-sol` | `codex.sh -m ...` |
| Cloud | Same split as on the laptop: DeepSeek 4.1 Flash for routine work, Muse Spark 1.3 for independent re-solving | Command Code models (tested 27 Oct 2026) | same ids as above | `bash /usr/local/bin/delegate.sh` |
| Cloud, only if Command Code fails | Drudgery and the one checker | Claude Haiku, effort xhigh | (Agent tool, model haiku, effort xhigh) | Agent tool |
| Anywhere | Planning, question design, judgement, teaching and language review, final look at every page | Main model (Opus) | n/a | n/a |

Rules that always apply:
1. Post a short plan (one line per job: which model, which job) and wait for Shashi's OK before running any helper. **Every time** DeepSeek 4.1 Flash is used, ask Shashi whether to use fast mode (rule of 27 Oct 2026; this replaces the laptop memory note that fast mode is the default).
1a. **Cloud sessions use the Command Code models too**, with the same model-for-job split as on the laptop (Shashi, 27 Oct 2026). The cloud machine has the Command Code CLI installed and the commandcode.ai service connected (the proxy adds the credentials). Call it with `bash /usr/local/bin/delegate.sh` (Section 6.2). Tested on 27 Oct 2026: DeepSeek 4.1 Flash fast answered a parallelogram-area question correctly (40 cm²) in about 4 s, and Muse Spark 1.3 answered a semicircle-perimeter question correctly (36 cm) in about 4 s. **Haiku subagents (effort xhigh) are only a fallback** if Command Code fails in the cloud.
2. On the laptop, do **not** spawn Claude subagents (Sonnet, Haiku, Agent tool). Use the CLIs. (Laptop CLAUDE.md.)
3. The main model reviews everything returned: compile every .tex, look at every diagram, check every answer.
4. For a big paper, split the build: 2-3 DeepSeek jobs in parallel, each writing one section's LaTeX fragment (questions, figures, answers), then one job or the main model assembles and compiles. One DeepSeek job building a 21-question test plus fc took about 25 minutes.
5. A whole-deck DeepSeek job hit the 10-minute timeout and lost its API connection on 22 Oct 2026. When class is minutes away, finish small edits yourself.
6. Each Codex call costs about 10k tokens even for a one-line answer, so batch small Codex jobs into one call.
7. DeepSeek wraps output in a ```` ```latex ```` fence; strip it. For snippet jobs say "output only ..., do not create files" and use `-t 3` with a scratch `-d`.
8. Command Code runs with `--yolo` and full tools: scope `-d` to the target or a scratch folder only.

### 6.2 Example commands (laptop, Git Bash)

```bash
# DeepSeek (fast) writes a TikZ snippet only
bash /c/Users/Krishnanvp/bin/delegate.sh -m deepseek/deepseek-v4.1-flash-fast -d "/e/tuition content/scratch" -t 3 \
  "Output only a LaTeX TikZ snippet, do not create files: a parallelogram with base 8 cm and height 5 cm, dashed height, right-angle mark."

# DeepSeek builds a section of a test inside a working folder (file-editing job, more turns)
bash /c/Users/Krishnanvp/bin/delegate.sh -m deepseek/deepseek-v4.1-flash-fast -d "/e/tuition content/perimeter-area-test2" -t 30 \
  "Read spec.md and questions.md. Write section-B.tex ... (precise spec)"

# Muse re-solves every question independently (it must not see the answers)
bash /c/Users/Krishnanvp/bin/delegate.sh -m meta/muse-spark-1.3-contributor -d "/e/tuition content/scratch" -t 3 \
  "Output only your answers, do not create files. Solve each question, showing steps: ..."

# Codex backup for drudgery (read-only by default; -w lets it write inside -d)
bash /c/Users/Krishnanvp/bin/codex.sh -m gpt-5.6-luna -d "/e/tuition content/perimeter-area-test2" -w "task"

# Codex for very hard thinking
bash /c/Users/Krishnanvp/bin/codex.sh -m gpt-6.1-sol -e high "Check this whole answer key: ..."
```

The folder paths in these examples are illustrations. The script paths, flags and model ids are exact.

**Cloud commands (tested 27 Oct 2026).** The cloud machine has its own copy of the launcher at `/usr/local/bin/delegate.sh`. It takes the same flags and finds the npm install of Command Code. Exact working test commands:

```bash
cd <scratch folder>
bash /usr/local/bin/delegate.sh -m deepseek/deepseek-v4.1-flash-fast -t 3 \
  "Output only the answer, do not create files: area of a parallelogram with base 8 cm and height 5 cm."
# -> 40 cm²   (about 4 s)

bash /usr/local/bin/delegate.sh -m meta/muse-spark-1.3-contributor -t 3 \
  "Output only the answer, do not create files: perimeter of a semicircle of radius 7 cm, using pi = 22/7."
# -> 36 cm    (about 4 s)
```

Node prints a harmless "EnvHttpProxyAgent is experimental" warning on stderr; ignore it. Codex is not installed in the cloud, so Codex models are laptop-only.

### 6.3 `E:\tuition content\CLAUDE.md` (word for word)

````markdown
# Tuition content — working rules

## Helpers = Command Code / Codex models, not Claude subagents
Do NOT spawn Claude subagents (Sonnet/Haiku/Agent tool) in this project. Use these CLIs.

**Ask first.** Before using any helper on a task, post a short plan to Shashi: which model
for which job, one line each. Wait for the OK, then run.

### Default: Command Code
    bash /c/Users/Krishnanvp/bin/delegate.sh [-m model] [-d dir] [-t turns] "task"
- `deepseek/deepseek-v4.1-flash` (default): LaTeX, TikZ, formatting, bulk edits.
- `meta/muse-spark-1.3-contributor`: second choice; independent re-solve to cross-check answers.
- Snippet jobs: `-t 3`, a scratch `-d`, and say "output only ..., do not create files".
- It runs with full tools (`--yolo`): scope `-d` to the target folder only.

### Backup / heavy thinking: Codex
    bash /c/Users/Krishnanvp/bin/codex.sh [-m model] [-d dir] [-w] [-e low|medium|high] "task"
- `gpt-5.6-luna` (default): drudgery when Command Code is down or struggling.
- `gpt-6.1-sol`, `gpt-5.6-sol`: very high intellectual work (hard problem design, tricky proofs,
  checking a whole answer key).
- Read-only by default; `-w` lets it write inside `-d`.

### Always
Main Claude keeps planning and judgement, and reviews everything returned: compile every .tex,
look at every diagram, check every answer before it reaches Shashi.

Details and test results: `command-code-helpers.md`.
````

`E:\tuition content\AGENTS.md` is the same file for Codex: identical to CLAUDE.md except that "Claude" is replaced by "Codex" (heading "Helpers = Command Code / Codex models, not Codex subagents", "Do NOT spawn Codex subagents (Sonnet/Haiku/Agent tool)", "Main Codex keeps planning and judgement").

### 6.4 `E:\tuition content\command-code-helpers.md` (word for word)

````markdown
# Command Code helpers (cheap models for drudgery)

Command Code CLI v1.74.1 is installed via npm (`%APPDATA%\npm\command-code`), already logged in.
Wrapper script: `C:\Users\Krishnanvp\bin\delegate.sh` (now falls back to the npm install path).

## Run a one-shot task

```bash
bash /c/Users/Krishnanvp/bin/delegate.sh -m <model> -d <dir> -t <turns> "task"
```

- `-m` model id (default DeepSeek)
- `-d` folder the model works in. It runs with `--yolo` and full tools, so it can write files there.
  Point it at a scratch folder unless you want it editing real files.
- `-t` max turns (3 is plenty for "just print the snippet"; raise for file-editing jobs)
- `-j` NDJSON output instead of plain text

## Model ids

| Model | id |
|---|---|
| DeepSeek 4.1 Flash (default) | `deepseek/deepseek-v4.1-flash` |
| Muse Spark 1.3 contributor | `meta/muse-spark-1.3-contributor` |
| Free fallbacks | `meituan/longcat-2.0:free`, `poolside/laguna-s-2.1-free` |

## Test (2026-10-11): parallelogram TikZ, base 8, height 5, dashed height, right-angle mark

Both models returned correct TikZ that compiled first time with pdflatex.

- DeepSeek: ~12 s, cleaner code (named coordinates). Wraps output in a ```latex fence, so strip it.
- Muse: ~17 s, bare snippet, slightly terser.

## Notes

- Say "output only ... do not create files" in the prompt for snippet jobs, otherwise it may write files into `-d`.
- Neither model is trusted blind: main Claude compiles/renders and checks every diagram and answer.

# Codex (backup, and heavy thinking)

Codex CLI 0.162 from the Codex desktop app, already logged in. Wrapper finds the latest
`%LOCALAPPDATA%\OpenAI\Codex\bin\*\codex.exe` itself, so app updates don't break it.

```bash
bash /c/Users/Krishnanvp/bin/codex.sh [-m model] [-d dir] [-w] [-e low|medium|high] "task"
```

- Default model `gpt-5.6-luna`, effort `medium`, read-only sandbox. `-w` allows writes in `-d`.
- Prints only the final answer (errors go to stderr).

| Model | id | Use |
|---|---|---|
| GPT 5.6 Luna | `gpt-5.6-luna` | drudgery, when Command Code fails |
| GPT 6.1 Sol | `gpt-6.1-sol` | very high intellectual work |
| GPT 5.6 Sol | `gpt-5.6-sol` | very high intellectual work |

Test (2026-10-11): "area of parallelogram, base 8, height 5", effort low. All three answered
`40 cm^2` in about 20 s. Each call uses about 10k tokens even for a one-liner (Codex's own
system prompt), so batch small jobs into one call.

# Rule

Command Code is the default helper; Codex is its backup, and Sol models are for hard thinking.
Before using any helper on a task, Claude posts a one-line-per-job model plan and waits for Shashi's OK.
````

### 6.5 `C:\Users\Krishnanvp\bin\delegate.sh` (word for word)

```bash
#!/usr/bin/env bash
# Delegate a task to Command Code's headless CLI on a cheap open model.
# Claude (Opus) plans/reviews; this runs the drudgery on DeepSeek/Muse/etc.
#
# Usage:
#   tools/delegate.sh [-m model] [-d dir] [-t max_turns] [-j] "task prompt"
#     -m  model id (default: $CC_MODEL or deepseek/deepseek-v4.1-flash)
#     -d  working directory the agent operates in (default: cwd)
#     -t  max conversation turns before it stops (default: 30)
#     -j  emit NDJSON event stream instead of plain text
#
# Cheap picks:  deepseek/deepseek-v4.1-flash   meta/muse-spark-1.3-contributor
# Free picks:   meituan/longcat-2.0:free        poolside/laguna-s-2.1-free
set -euo pipefail

CLI="$LOCALAPPDATA/Programs/Command Code/resources/app/node_modules/command-code/dist/index.mjs"
[ -f "$CLI" ] || CLI="$APPDATA/npm/node_modules/command-code/dist/index.mjs"
model="${CC_MODEL:-deepseek/deepseek-v4.1-flash}"
dir="$PWD"
turns=30
fmt=text

while getopts "m:d:t:j" opt; do
  case $opt in
    m) model="$OPTARG" ;;
    d) dir="$OPTARG" ;;
    t) turns="$OPTARG" ;;
    j) fmt=json ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))
[ $# -ge 1 ] || { sed -n '2,13p' "$0"; exit 2; }

[ -f "$CLI" ] || { echo "Command Code CLI not found at: $CLI" >&2; exit 1; }
cd "$dir"
echo ">> delegate: model=$model dir=$dir max-turns=$turns" >&2

exec node "$CLI" -p "$*" \
  -m "$model" \
  --max-turns "$turns" \
  --output-format "$fmt" \
  --trust \
  --tools-all \
  --yolo \
  --skip-onboarding \
  --no-auto-update
```

### 6.6 `C:\Users\Krishnanvp\bin\codex.sh` (word for word)

```bash
#!/usr/bin/env bash
# Backup helper: one-shot task to Codex CLI (desktop install).
# Usage: codex.sh [-m model] [-d dir] [-w] [-e effort] "task"
#   -m model (default gpt-5.6-luna; heavy thinking: gpt-6.1-sol, gpt-5.6-sol)
#   -d working dir (default cwd)   -w allow writes in dir (default read-only)
#   -e reasoning effort: low|medium|high (default medium)
set -euo pipefail
CLI=$(ls -t "$LOCALAPPDATA"/OpenAI/Codex/bin/*/codex.exe 2>/dev/null | head -1)
[ -n "$CLI" ] || { echo "Codex CLI not found under $LOCALAPPDATA/OpenAI/Codex/bin" >&2; exit 1; }
model=gpt-5.6-luna; dir="$PWD"; sandbox=read-only; effort=medium
while getopts "m:d:we:" o; do case $o in
  m) model="$OPTARG";; d) dir="$OPTARG";; w) sandbox=workspace-write;; e) effort="$OPTARG";; *) exit 2;; esac; done
shift $((OPTIND-1)); [ $# -ge 1 ] || { sed -n '2,7p' "$0"; exit 2; }
out=$(mktemp)
echo ">> codex: model=$model effort=$effort dir=$dir sandbox=$sandbox" >&2
"$CLI" exec -m "$model" -c model_reasoning_effort="$effort" -s "$sandbox" -C "$dir" \
  --skip-git-repo-check --ephemeral --color never -o "$out" "$*" >/dev/null 2>"$out.log" </dev/null || { cat "$out.log" >&2; exit 1; }
cat "$out"; rm -f "$out" "$out.log"
```

### 6.7 Installed tools on the laptop (27 Oct 2026)

- Command Code CLI v1.74.1 (npm), logged in.
- Codex CLI 0.162 (from the Codex desktop app), logged in.
- MiKTeX 24.1: `pdflatex` (MiKTeX-pdfTeX 4.18), `xelatex` (MiKTeX-XeTeX 4.10), `lualatex` (LuaHBTeX 1.17.1).
- Global Claude Code rules file `C:\Users\Krishnanvp\.claude\CLAUDE.md` (not copied here; it matches the shashi-global-rules skill: LaTeX + PDF by default, Office file authorship "Krishnan", DeepSeek fast id, the terms rule, never add unrequested content).

---

## 7. Classes, student groups and where they are up to

### 7.1 Grade 9 tuition (CBSE), Chapter 6 "Perimeter and Area" (as of 27 Oct 2026)

**Taught (confirmed by Shashi):**
- Perimeter fully taught, including arc length and the perimeter of a sector (Class 1 and Class 2 sections 1-2, Ex 6.1C).
- Area of a parallelogram (base × perpendicular height), area of a triangle, obtuse triangle with the height outside, the median theorem (a median divides a triangle into two triangles of equal area), area when the height is not known (Class 2 sections 3-6, Ex 6.2A, 6.2B, 6.2C).
- Heron's formula (confirmed 12 Oct 2026).

**Not taught (as of 12 Oct 2026):** area of a circle, area of a sector, area of a segment. Brahmagupta's formula and Baudhāyana's squaring of a rectangle are not taught and are not planned.

**Latest activity (22 Oct 2026):** Shashi asked for iPad slides of Exercise 6.3A (area of a circle, 6 questions from the Class 2 doc) plus questions on the area of a sector and segment, with teaching slides (circle cut into a parallelogram), for a class that day. Two decks were made:
- `circle area slides.pdf` (quick cloud deck, 18 slides): a teaching slide, a "Remember" slide (circle, sector, arc, segment), Ex 6.3A one per slide plus a copy-all slide, a sector/segment picture slide, 6 new sector/segment questions plus a copy-all slide. Saved to Drive.
- `6.3A slides.pdf` (19 slides) and `6.3A slides fc.pdf` (31 slides) from the laptop, checked, with Muse's re-solve matching every answer. Saving to Drive not confirmed.

So area of a circle (Ex 6.3A) was most likely being taught from 22 Oct. **This is not confirmed.** Ask Shashi where the class is now before planning new work.

**Class 2 structure (single source):** 1 From a circle to an arc · 2 Arc length and sector perimeter (Ex 6.1C) · 3 From a parallelogram to a rectangle (Ex 6.2A) · 4 From a parallelogram to a triangle, an obtuse triangle (Ex 6.2B) · 5 Equal areas without congruence, a property of a median, Theorem 1 · 6 When the height is not known (Ex 6.2C) · 7 Area of a circle (Ex 6.3A) · 8 Area of a sector · 9 Sector and segment · 10 One developing problem sequence · 11 If you are ready for more.

**Materials made so far for Chapter 6:** Class 1 (PDF in Drive; .tex under old names on the laptop), Class 2, homework 1 (10 questions up to Ex 6.2A), homework 2 (sections 3-4 and the median theorem; Pythagoras used), Test 1 (existed before this project), Test 2 (50 marks, everything except circle, sector and segment area), practice questions, the two circle/6.3A slide decks. Earlier work from September 2026 (partly in ChatGPT): Class 1 and Class 2, Test 1 and a 12-question MCQ draft.

### 7.1a BIO LEARNING CENTER (BLC) MCQ sets on Chapter 6

Three MCQ sets exist on the laptop: `set 1/2/3 perimeter area` with separate `set 1/2/3 solution perimeter area`, built with the toolchain in `E:\tuition content\perimeter-area-mcq\` (question banks 1–5 by topic, including Brahmagupta and circle/sector/segment area; selection files `selection-blc-20.txt`, `selection-blc-set2.txt`, `selection-blc-set3.txt`). This work was done outside this project, so it is not in the project threads. Which sets were given to which students is not recorded. Ask Shashi.

**Open items:**
- Class 1 restyle into the house design: offered, not requested.
- "Teaching material" skill: offered, parked by Shashi for later.
- 6.3A slides: Drive save not confirmed.
- Next likely work: homework or test on the area of a circle, sector and segment, once Shashi confirms these are taught.

### 7.2 Grade 10

Memory and the Drive folder name ("Tuition_grade9,10") show Shashi also teaches Grade 10. No Grade 10 material or progress has been recorded in this project. Ask Shashi.

### 7.3 Prerana (Prayoga) Grade 9 group

One-day event on **30 October 2026**, 90 minutes, indoor, group-based, maths team. Waiting for Shashi to choose one of four activities (Section 3.9). Recommended: "Build shapes, find the hidden rule".

### 7.4 Shashi's own learning

IGCSE Extended (Cambridge 0580) first, then IB DP AA SL. Checklist and 10-week plan offered, no answer yet.

---

## 8. Style rules and corrections

### 8.1 Rules for questions and examples

1. CBSE competency-based questions, not direct formula use. Easy to hard; only a few easy, approachable ones at the start.
2. Test the learning objective from every angle: work backwards, explain why or true/false, find the mistake, draw or construct, compare or "what if", real-life application. At most one straight-substitution question per set.
3. Every question and every example states explicitly what to find. (A Class 2 example once showed only an area calculation, and a student asked "what to find here, sir?". Never let this happen.)
4. Worked examples model the solution format taught: rough diagram with given measurements, Given:, To find:, step-by-step solution with reasons, final answer with units.
5. Use mostly Indian and South Indian everyday settings (festivals, rupees, temples, local objects), described in plain English. Use an Indian word only if it is very widely known (rangoli, Onam). Avoid regional words (visiri, pookalam). No foreign settings like pizza.
6. Choose numbers so every answer, including intermediate steps, is a whole number unless decimals are the point. Plan divisibility in advance (the 337.5 mistake came from halving 1350 twice).
7. Data must be possible: the shape can exist, heights are not longer than the sides they meet, the obtuse triangle is really obtuse.
8. Not every question needs a printed diagram. For questions without one, tell students to draw a rough diagram and mark the measurements. For some questions, make drawing the diagram a marked part of the question.
9. Pythagoras may be used in homework questions.
10. "Is he right?" style claims should not always have the answer "No"; make some claims true.
11. Stay within what has been taught; check class notes before writing.
12. Do not repeat questions from earlier homework and tests.

### 8.2 Rules for the student sheet

1. Assignment heading: "Assignment" on the left, the date on the right, one thin rule. Nothing else.
2. No difficulty or section labels (Warm-up, Think it through, Challenge) and no titles or nicknames before questions ("Clock.", "Vegetable patch"). Anything that distracts from the question must not exist. Easy-to-hard grouping and nicknames are internal only (fine in chat or fc notes).
3. House design (Section 5.2).
4. Student and fc copies match word for word in every question.

### 8.3 Rules for the fc (facilitator) copy

1. The fc is for other teachers too. Write it so any teacher can use it without help.
2. Teacher-facing text (overview, notes, answer explanations): short sentences (up to about 20 words), one point per sentence, active voice, common words, the same term for the same thing (ASD-STE100 core rules). Student questions stay in normal clear English.
3. Register is **formal and academic**. Short and clear does not mean casual. Use standard teaching vocabulary: "concepts assessed", "concept tested", "competency focus", not "ideas" (Shashi, 12 Oct 2026). Check the whole fc for similar informal words.
4. No tool or internal talk: no "TikZ", "trap", "invariant", "structural", "scaffold".
5. Do not spoon-feed the teacher, and do not write a script of what to say at every step.
6. "Common mistake" notes: include one only when the mistake is genuinely likely with that exact idea and knowing it in advance changes what the teacher does. At most two short sentences: the mistake, then what to ask or say. Most sections need none. Overloaded notes confused Shashi.
7. A rough answer diagram for every question.
8. Answers show the steps a student should write, in full sentences where explaining.
9. Answers in smaller grey text so they do not fight with the questions.

### 8.4 Rules for working with Shashi

1. Plain language, lead with the answer, short replies, one point per sentence.
2. Plan first for anything big; wait for OK. One-word questions with a recommendation.
3. Keep Claude usage minimal: main model plans, judges and does the final review; helpers do drudgery. Never run many reviewers or repeated rounds.
4. Post the helper-model plan and ask before using helpers; ask fast or normal mode.
5. Say what was checked and how. Never just "done". Report problems plainly.
6. Show files before saving to Drive; keep the old version.
7. Keep the checklist current; answer "done?" honestly.
8. Respond quickly when Shashi is about to teach.
9. React to Shashi's own message, not to your own (a misplaced 👍 on 8 Oct confused Shashi).
10. Do not add content, labels or features Shashi did not ask for; suggest them in chat first.
11. Terms: introduce a new idea once in simple words, then give its standard name and use only that name.
12. Read context carefully: background information is not a requirement (the biology mention for Prerana was only context).

### 8.5 Log of every correction and decision, by date

**8 October 2026**
- Class 2 diagram review: five diagrams did not match the text (missing diagonal in "two triangles make a parallelogram"; obtuse triangle with the height landing inside; circle-to-parallelogram figure wrong and labelling the slanted side as r; "dashed" heights printing solid, no right-angle marks; "sloping side" label on the wrong edge). Shashi approved fixing all. Fixed diagrams labelled the rearranged-circle height as "height ≈ r" outside the shape.
- Shashi could not see images in a Markdown review: deliver reviews as one self-contained PDF.
- Shashi asked to use smaller models as subagents and review their work, to save usage.
- Shashi chose "Replace originals" in Drive for the fixed Class 2 files.
- Drive connector cannot upload PDFs; Shashi has Google Drive for desktop; the laptop folder `G:\My Drive\Tuition_grade9,10` was connected.
- Homework 1: "can you change pizza thing" → use mostly Indian and South Indian contexts.
- "visiri": students may not know regional words; use English words unless the Indian word is very popular.
- Ask students explicitly to draw rough diagrams; make drawing part of some questions.
- Shashi confirmed LaTeX is the tool for PDFs.
- Heading too busy → only "Assignment" and the date at the top right.
- No section labels like Warm-up or Challenge on sheets ("only internal discussion, keep this in mind for future things").
- The blue-box design "does not look elegant" → plain exam-paper style.
- Palatino: fractions and mixed fractions looked bad → full-size fractions; font comparison (Palatino, Century Schoolbook, Charter, Times, Lora, Source Serif, Libertinus, Fira Sans) → **Century Schoolbook** chosen.
- ₹ symbol instead of "Rs.".
- File naming: "class 1", "class 2", "homework 1", "test 1", each with " fc".
- Class 2 restyled into the house design; page count kept at 10 (student) and 13 (fc).

**10 October 2026**
- Shashi asked for a prompt describing the design rules to share with another Claude Code session. One was given (it matches Section 5.2 and 8.2).

**11 October 2026**
- Homework 2: remove labels before questions ("anything that distracts their attention from the question should not exist").
- fc had no rough diagrams → every fc answer needs a rough answer diagram.
- Unplanned decimal 337.5 → choose numbers that divide cleanly.
- Wrong label "16" for side AC (15 cm) caused by blind find-and-replace → never global find-and-replace numbers; re-check all pages.
- Shashi asked for a very strict review; the six-checker review gate was agreed, then stopped because it used far too much usage (about 1.6 million tokens over three rounds) → lean review: one checker, one round.
- Class 2 exercises too weak (plugging values) → test the objective from all angles.
- An example did not say what to find → every question states what to find.
- fc used jargon (TikZ, trap) → plain, simple fc language using ASD-STE100 core rules.
- "Common mistake" notes: balance; only when genuinely needed, concise and simple.
- Pythagoras is fine in homework 2.
- Use Haiku (xhigh) subagents for drudgery in the cloud.
- "You are still in checklist one?" → keep the progress checklist current.
- Examples must model the solution format (rough diagram, Given, To find, steps, answer).
- Usage at 92% → keep Claude's own share minimal; use other models.
- Command Code CLI set up (DeepSeek 4.1 Flash, Muse Spark 1.3); Codex CLI added (GPT 6.1 Sol, GPT 5.6 Sol, GPT 5.6 Luna); always post a model plan and ask first.
- New work threads start on the laptop by default.
- Skill "working-with-shashi" created (a skill evolves only with Shashi's approval through review cards). A second "teaching material" skill was parked.

**12 October 2026**
- Test 2: exclude area of circle, sector and segment; perimeter of a sector stays in; Heron's formula taught; Brahmagupta and Baudhāyana not taught.
- Look at the CBSE style of competency-based and case-study-based assessment → five-section CBSE layout.
- Questions must genuinely test understanding and application; only a few easy ones.
- DeepSeek was slow (25 minutes) → run 2-3 DeepSeek jobs in parallel by section, one to assemble.
- Shashi asked to push to Drive while on mobile.
- fc used "ideas tested" → formal academic language ("concepts"); check for similar words.
- The main model (Opus) must check diagrams, questions and question sentence framing once more before pushing anything to Shashi.
- Clean old versions after approval.
- Skill working-with-shashi updated to version 2.

**13 October 2026**
- IB/IGCSE overview; Shashi wants to learn the maths to broaden teaching scope.

**22 October 2026**
- Prerana: "you got it wrong, our thing is nothing to do with biology session". Explain activities plainly: core idea, what works, what students do.
- Slides: annotatable on the iPad; one question per slide with space; DeepSeek in fast mode; slides with many questions for students to copy; teachable slides like the circle cut into a parallelogram; time matters, deliver fast.
- "This chat is taking lot of time" → a separate quick thread was started to deliver at once.


**27 October 2026**
- Ask Shashi **every time** DeepSeek 4.1 Flash is used whether to use fast mode.
- Cloud sessions use the Command Code models too (same split as the laptop); Haiku only as a fallback. Tested and working on 27 Oct 2026 with `/usr/local/bin/delegate.sh`.
- This handbook was written and saved.

---

## Appendices

### Appendix A. Skill "working-with-shashi" (word for word)

````markdown
---
name: "working-with-shashi"
description: "How to work with Shashi on any task: plain language, plan first, lean usage with cheaper helper models, honest checks, approval before saving. Use in every conversation with Shashi."
---

# Working with Shashi

Version 2 (2026-10-12). Follow these rules on every task, whatever the subject.

## 0. Facts come from memory, not from this skill
- This skill only says HOW to work with Shashi. Facts ABOUT Shashi (role, projects, people, personal preferences) live in Shashi's memory.
- At the start of a task, use the memory (profile, preferences, and any file that fits the task) for facts about Shashi.
- If this skill and memory disagree, do not guess. Tell Shashi what differs and ask which is right.
- If memory is not available (for example in Claude Code on the laptop), use CLAUDE.md in the working folder, and ask Shashi for any missing fact instead of assuming.

## 1. Talk simply
- Treat Shashi as a capable non-expert. Explain in plain words, with no jargon or internal tool talk.
- Lead with the answer or the decision needed. Keep replies short; cut sentences that do not change what Shashi does next.
- One point per sentence. Short sentences, active voice, consistent terms.
- When something is technical, teach it briefly instead of assuming knowledge.

## 2. Plan before big work
- For anything larger than a quick answer, first show a short plan and wait for Shashi's OK.
- Ask questions that can be answered in one word. Give the options on short lines and mark your recommendation.
- For small details Shashi has not decided, pick a sensible default, say which one, and continue.

## 3. Save usage
Shashi's Claude usage is limited and they care about it a lot.
- Do planning, judgement and the final check yourself. Hand routine, mechanical work (formatting, LaTeX, diagrams, re-solving, bulk edits) to cheaper helper models.
- Before using helpers on a task, post a 2-3 line plan of which model does which job and ask Shashi to confirm.
- Helper models on Shashi's laptop: Command Code CLI is the default (DeepSeek 4.1 Flash for routine work, Muse Spark 1.3 as second model / independent checker). Codex CLI is the backup (GPT 5.6 Luna for routine work; GPT 6.1 Sol or GPT 5.6 Sol for very hard thinking). Exact commands are in CLAUDE.md / command-code-helpers.md in the laptop tuition folder. Away from the laptop, use the cheapest capable Claude model (e.g. Haiku).
- Keep checking lean: one careful check, one round. Do a second round only if a real error was found. Never run many reviewers or repeated rounds.
- Batch small helper jobs together instead of many tiny calls.

## 4. Check honestly
- Review everything a helper produces before Shashi sees it.
- Say what was checked and how (re-solved, compared, looked at each page). Never just say "done".
- Report problems plainly. If something was skipped, say so.
- Never change numbers or words across a whole file blindly with find-and-replace. Check each change in its place, and re-check every page after an edit.

## 5. Show before saving
- Share finished files with Shashi first. Save to Google Drive or replace an original only after Shashi says OK.
- Keep a copy of the old version when replacing a file.
- Deliver reviews or reports as one self-contained PDF, not loose files.
- Use Shashi's naming: "<name> N" for the student copy, "<name> N fc" for the teacher (facilitator) copy.

## 6. Status updates
- When Shashi asks "done?", answer honestly with what is finished and what is left, in one or two lines.
- Keep progress notes current so Shashi never has to guess.

## 7. Learn and evolve this skill
This skill grows with Shashi, but only with their approval.
- Whenever Shashi corrects you, shows frustration, or states a new preference about how to work, note the lesson.
- Decide where the lesson belongs:
  - A new fact about Shashi or a personal preference (style, format, tone) goes to memory, not here.
  - A lesson only about one project (class progress, folder paths) goes to that project's memory, not here.
  - A general rule about HOW to work, true for future tasks, goes in this skill.
- For a skill lesson, at the end of that piece of work propose an updated version of this skill: keep every existing rule, add the new one in the right section, raise the version number and date, and show it to Shashi on a review card to save.
- Never put facts about Shashi into this skill; point to memory instead.
- Never change this skill without Shashi's approval.
````

### Appendix B. Skill "shashi-global-rules" (word for word)

Note: its rule "commit and push every finished file to the repo's main branch" applies to Claude Code cloud sessions with a repository. This project has no repository attached; cloud threads here save to `/mnt/project-files/` and share the files in the thread instead.

````markdown
---
name: shashi-global-rules
description: Shashi's standing preferences for documents, usage budget, cheap-model helpers, working protocol, taste and Manim videos. Use on every task with Shashi (Krishnan), alongside working-with-shashi.
---


I am Krishnan, also called Shashi. Follow the `working-with-shashi` skill on every task.

## Documents
- Default format for every document I ask for (worksheets, question papers, answer keys, notes):
  LaTeX source (.tex) plus compiled PDF. Use another format only when I ask for it.
- Every .docx / .pptx / .xlsx you generate: set Author and Last modified by to "Krishnan",
  Title to the document title, and clear Comments. Never leave library defaults like "python-docx".
- In Claude Code cloud sessions (CLAUDE_CODE_REMOTE=true) the machine is wiped when idle: commit and
  push every finished file to the repo's main branch and give me its GitHub link. Save to Google Drive only after I OK it.

## Budget: Claude Pro subscription. Conserve Opus.
- Opus is for planning, design taste, tricky reasoning, and review. Never spend it on drudgery.
- Drudgery = boilerplate, bulk/mechanical edits, scaffolding, test writing, docstrings, format
  conversions, search-and-summarize, first drafts of repetitive code. Delegate it to Command Code's
  headless CLI on a cheap open model:

      bash /c/Users/Krishnanvp/bin/delegate.sh [-m model] [-d dir] [-t turns] "task"   # laptop
      bash /usr/local/bin/delegate.sh [-m model] [-d dir] [-t turns] "task"            # Claude Code cloud

  Default model `deepseek/deepseek-v4.1-flash`. Also `meta/muse-spark-1.3-contributor` (95% off).
  Free: `meituan/longcat-2.0:free`, `poolside/laguna-s-2.1-free`. Use the exact path literal.
- Where neither path exists (Cowork, claude.ai chat or Projects), there is no shell helper: do the
  drudgery with the cheapest capable Claude model (e.g. a Haiku subagent) when the surface allows it.
- Delegate only into git-tracked or scoped directories. Review every delegated result (diff, tests)
  before accepting; fix small issues with Opus, resend big ones to the cheap model with a sharper spec.
- If the CLI isn't reachable, say so in one line and continue with Opus. Don't lecture on limitations.
- Never re-explain this setup. Act on it.

## Working protocol: keep the user informed and deciding
- For any task beyond a few minutes of work, start with a short plan that splits the work into
  **Opus** vs **delegate** parts, one line of reason each, and ask which parts to push to the cheap
  model before running anything. Tiny tasks: just do them.
- When asking which model to delegate to, also ask: fast mode or normal? (Fast is a separate
  model id, e.g. `deepseek/deepseek-v4.1-flash-fast`; if the pick has none, like Muse, say so.)
- After each delegated batch, give a short status: what was sent, what came back, what needs the
  user's review or decision. Terse, no walls of text.
- Surface decisions early with a recommendation, not a menu of options.

## Taste
- Simple, elegant, minimal. Match the surrounding code. No speculative abstractions.
- Never add content, labels or features I didn't ask for (e.g. reading-time lines, extra stats,
  decorations, restructuring). Suggest them in chat and wait for my yes.
- Terms, in every explanation or lesson: introduce a new idea once in simple words, then give its
  standard technical name and use only that name from then on. Never keep a vague everyday stand-in
  (e.g. "mix" for convex combination); vagueness loses me.

## Manim videos (every workspace)
- Pre-production comes first, in chat, before any scene code or render:
  1. Ask format (landscape 16:9 or portrait 9:16 Shorts) and background (colour + treatment).
     Both vary per video -- never assume them from an earlier one.
  2. Show the storyboard, piece by piece (what appears/moves, sound cue, rough seconds), and
     the full narration script. Apply the user's edits; render only after their go.
  Iterate on the script, not on renders.
- Sound effects are on by default for every video, narrated or silent: use the palette in the
  `manim-voiced-video` skill (`assets/sfx.py`, rules in `references/sound-design.md`). One sound
  per meaning; nothing that judges before the evidence. Silent only if the user asks.
- Render every pass with `--disable_caching` so the soundtrack stays frame-exact.
- The user reviews at the video level. Technical calls (caching, levels, cue timing) are mine;
  decide them, don't ask.
````

### Appendix C. Skill "math-lesson-builder" (word for word)

This skill's visual design (Computer Modern, blue accent, pale-blue panels) is replaced by Shashi's house design (Section 5.2). Its consultation, planning and checking workflow still applies.

#### C.1 SKILL.md

````markdown
---
name: math-lesson-builder
description: Create, revise, format, and deliver classroom-ready mathematics facilitator copies as LaTeX source and compiled PDF. Use when the user asks to plan or teach a mathematics chapter, turn a chapter or textbook into facilitator learning material, continue an earlier facilitator-copy workflow, make a lesson more concrete or diagrammatic, add examples or a continuation bank, reproduce the user's established clean teaching-module style, or create an editable .tex source and polished PDF.
---

# Build Mathematics Lessons

Produce a clear mathematics learning resource that a facilitator can learn from and teach with. Keep its main body close to a well-designed student workbook: activities, diagrams, explanations, worked examples, questions, exercises, and formal mathematics should form one continuous learning journey. Add a light facilitator layer only where professional attention or an intervention is genuinely needed.

Read [references/workflow-and-design.md](references/workflow-and-design.md) and [references/latex-design-system.md](references/latex-design-system.md) before drafting or revising a facilitator copy. Start every new document from [assets/math-lesson-template.tex](assets/math-lesson-template.tex).

## Run a thorough consultation before drafting

Do not begin the facilitator-copy document, write polished lesson content, create LaTeX, or format pages immediately. First conduct a deliberate consultation designed to prevent later revisions.

Read the user's message and supplied sources, note what is already known, and then ask comprehensively about every relevant unresolved choice. Prefer asking several clear, grouped questions over making silent assumptions. Continue with follow-up questions when an answer reveals another meaningful choice.

Cover the consultation areas in [references/workflow-and-design.md](references/workflow-and-design.md), including:

- teaching context, student readiness, class duration, and classroom constraints;
- exact content scope and what must or must not be included;
- intended understanding, teaching philosophy, sequence, pacing, and level of formality;
- activities, questions, examples, diagrams, proofs, practice, student recording, and reserve material;
- facilitator-copy wording, density, page design, source template, editable format, filename, and destination.

Do not repeat questions that have already been answered explicitly, but do not avoid a useful question merely because a reasonable default exists. When several decisions are connected, present the likely options and explain the practical difference so the user can choose deliberately.

After the consultation, present a compact **agreed brief and proposed lesson route** containing:

- the class destination;
- included and excluded content;
- prerequisite and misconception plan;
- learning sequence and approximate timing;
- planned diagrams, examples, proof treatment, and practice;
- document structure, design source, output files, filename, and destination;
- any remaining assumptions.

Obtain the user's approval or corrections before starting the actual document. Treat approval of the brief as the drafting gate. If the user explicitly instructs the skill to skip consultation and proceed, follow that instruction.

Treat a supplied PDF or LaTeX file identified as a design template as visual guidance only; do not import its lesson content unless explicitly requested. Do not change a requested filename.

## Plan before formatting

Build the mathematical route before designing pages:

1. Identify the conceptual destination for this class.
2. Diagnose the minimum prerequisites with a short pulse.
3. Find the student need, puzzle, contrast, or visual experience that motivates the idea.
4. Sequence concrete or visual experience → student observation → precise language → symbolic form → proof or justification → application.
5. Separate what must happen today from optional continuation material.
6. Locate predictable misconceptions and create counterexamples or comparison figures for them.

Do not begin with dense vertex notation, definitions, or theorem statements when a concrete diagram or example can create the idea first.

## Write the learning material first

Build the main document as a natural learning sequence, not as an actor-like script for the teacher. Use ordinary section headings based on the mathematics or activity, followed by the material itself:

- a situation, diagram, example, construction, or activity;
- questions that lead the learner to notice the idea;
- space or structure for observations where useful;
- a clear explanation or formalisation;
- worked examples and practice;
- a transition to the next idea.

Let this sequence make the teaching method implicit. A capable teacher should be able to see how to conduct the lesson from the material without being told separately what to prepare, say, draw, ask, observe, board, and record at every stage.

Do not:

- divide ordinary content into repeated facilitator cue boxes;
- prescribe exact teacher dialogue unless wording is unusually delicate or conceptually critical;
- label every small classroom move;
- duplicate the learning material as a separate teaching script;
- add instructions merely because they might be useful.

## Add only a thin facilitator layer

Insert a visually distinct **Note to Facilitator** or brief instruction only when omitting it creates a meaningful risk. Appropriate uses include:

- a crucial misconception or subtle mathematical distinction;
- a safety, material, or setup requirement not evident from the activity;
- the one question or intervention on which discovery depends;
- an expected response that helps diagnose understanding;
- a warning not to reveal a result too early;
- a difficult transition, proof step, or construction;
- a practical time-saving or short-of-time decision;
- an answer, solution cue, or extension intended only for the teacher.

Keep each note short and local to the relevant material. Prefer one precise note over several procedural labels. If the student-facing material already communicates what to do, do not add a facilitator note.

The facilitator copy may include answers, solution guidance, pedagogical intent, misconceptions, and occasional facilitation tips that would be removed from a student version. Its mathematical narrative and activity sequence should otherwise remain substantially the same.

## Use diagrams as mathematical teaching

Add a figure when it reduces abstraction, reveals a relationship, supports discovery, distinguishes examples from non-examples, or anchors a proof. Diagrams must carry an instructional job, not decorate the page.

Prefer:

- before/after or example/non-example pairs;
- colour or line-style correspondence that remains understandable in grayscale;
- labelled constructions built in the order the teacher draws them;
- a discovery diagram followed by a clean proof diagram;
- visual checks before symbolic exercises.

Make the intended interaction with the figure evident through nearby questions or activity directions. Add a facilitator note only if a particular drawing order, emphasis, or intervention is essential. Ensure labels, ratios, orientations, and correspondence are mathematically consistent.

## Provide depth without bloating the main route

For every major idea, include enough graded examples for explanation, guided practice, and independent check. Begin with clean cases, then vary orientation, labels, or representation, and finally include a misconception-revealing case.

Place surplus teaching material in a clearly separated continuation or reserve bank. Include:

- extra examples and problems with answers or solution cues;
- one deeper “what if?” question;
- a recovery explanation for a common sticking point;
- a bridge to the next class.

Never pad the compulsory route merely to make the document longer.

## Handle proofs carefully

Create a need for the result before naming it. Make the diagram and logical dependency visible. Distinguish observation from proof. Present the reasoning as a learnable sequence of questions and explanations, with facilitator notes only at genuinely difficult steps.

If time is short, stop at a mathematically coherent point and resume next class. Do not compress a proof into unexplained algebra.

## Format and produce

Always author the document in LaTeX and compile it to PDF. Deliver both the editable `.tex` source and the compiled `.pdf`. Do not use DOCX, HTML, ReportLab, or another authoring format as the primary source. If the user explicitly requests an additional format, create it only as a secondary export; retain LaTeX as the authoritative source.

Use [assets/math-lesson-template.tex](assets/math-lesson-template.tex) as the base and follow [references/latex-design-system.md](references/latex-design-system.md) exactly. Preserve its A4 geometry, Computer Modern typography, restrained blue palette, theorem styling, page furniture, spacing, exercise treatment, pale panels, and TikZ figure language. Do not redesign it from memory or substitute a generic document template.

Use descriptive mathematical or activity headings, exercise/example/theorem labels instead of fragile page-number references, generous figure size, legible labels, and one restrained style for occasional facilitator-only notes.

Keep wording simple, standard, calm, and professional—not playful, ornamental, or overly verbose. Optimise for quick scanning without removing teaching substance.

Compile with `pdflatex` at least twice, and more times when references require it. Render every PDF page to PNG and inspect visually. Check for compilation warnings that affect output, clipped text, overfull boxes, broken symbols, crowded diagrams, awkward page breaks, orphaned headings, inconsistent spacing, unnecessary blank areas, and deviations from the embedded design system. Revise until the copy is classroom-ready.

## Revise from feedback

Treat feedback as evidence about the reusable method:

- “too abstract” → add concrete cases, comparison figures, and diagram-led questions;
- “too wordy” → shorten prose while retaining the mathematical learning sequence;
- “too many boxes” → restore hierarchy through whitespace and typography;
- “not enough to continue” → expand the reserve bank, not the core route;
- “formatting changed” → return to the supplied visual template and preserve established spacing and symbol treatment.
- “too much hand-holding” → remove repeated teaching cues and let the learning material carry the pedagogy;
- “too different from the student workbook” → retain one shared mathematical narrative and restrict differences to essential facilitator notes, answers, misconceptions, and guidance.

Change only what the user requested. Briefly explain any proposed structural improvement before applying it when it goes beyond the request.

## Final checks

Confirm that:

- the consultation was completed and the approved brief was followed;
- the route reaches the stated class destination;
- every formal statement has an intuitive or visual lead-in;
- examples progress from accessible to transferable;
- diagrams are accurate and integrated naturally with the learning material;
- the facilitator copy reads as coherent mathematics material rather than a performance script;
- facilitator-only notes are sparse, necessary, local, and visually distinct;
- the core learning journey could be reused in a student version without major rewriting;
- timing, reserve material, and the short-of-time route are credible;
- required source content is self-contained, with no instruction to “check the textbook”;
- the authoritative source is LaTeX and compiles without material errors;
- every page of the latest PDF has been visually inspected;
- editable `.tex` source and final `.pdf` use the requested filenames and destination.
````

#### C.2 references/workflow-and-design.md

````markdown
# Workflow and design reference

## Contents

- Established workflow
- Pre-drafting consultation
- Facilitator-copy relationship to student material
- Lesson architecture
- Learning-section test
- Diagram test
- Example progression
- LaTeX production
- Revision rules
- Delivery checklist

## Established workflow

Use this sequence for a new chapter:

1. Read the request, chapter, required examples, exercises, theorems, and supplied teacher/student materials.
2. Conduct a comprehensive consultation covering all unresolved pedagogical, practical, content, and design choices.
3. Summarise the agreed brief and proposed lesson route.
4. Wait for approval or corrections before drafting the document.
5. Determine what can reasonably be learned in one class rather than trying to cover the whole chapter.
6. State the class destination in observable terms.
7. Map prerequisites and likely misconceptions.
8. Design the conceptual route from need and experience to formal mathematics.
9. Allocate realistic time across the learning sequence and identify a coherent stopping point.
10. Draft the complete learning material.
11. Add diagrams where abstraction or correspondence would otherwise dominate.
12. Add graded practice and a separate continuation bank.
13. Format in LaTeX using the bundled teaching-module template and exact design system.
14. Render, inspect, revise, and deliver the editable source plus PDF when requested.

For a revision, preserve parts already approved and target the stated issue. Do not restart the document merely because a different structure is possible.

## Pre-drafting consultation

Ask as many relevant questions as needed to make the first document draft close to final. Organise them into readable groups rather than asking one vague question at a time. Follow up where necessary.

### Teaching situation

- Which grade, board/curriculum, chapter, subtopic, and class number is this?
- How much teaching time is actually available, including any break or setup time?
- How many students are expected, and what is their general readiness?
- What have they already learned, and what difficulties have appeared previously?
- Is the lesson for tuition, school, a camp, teacher training, or another setting?
- What classroom resources are available: board, geometry boxes, printed sheets, projector, manipulatives, or devices?
- Are students expected to work individually, in pairs, or as a whole class?

### Scope and destination

- Which concepts, examples, exercises, constructions, results, and proofs must be covered?
- Which material should be postponed or explicitly excluded?
- Is this the first exposure, consolidation, revision, remedial teaching, or exam preparation?
- What should students understand, say, draw, prove, or solve by the end?
- Should the class prioritise intuition, formal proof, procedural fluency, textbook alignment, or a stated balance?
- Is there a required next-class bridge?

### Teaching route

- Should the lesson begin with a puzzle, real situation, diagram, construction, measurement, numerical example, misconception, or direct question?
- How discovery-based should the lesson be?
- Are there any places where exact facilitator wording is genuinely necessary?
- Which expected student responses or recovery prompts are important enough to appear as facilitator-only notes?
- Which misconceptions or non-examples must be addressed?
- Which stages should involve student activity rather than teacher demonstration?
- What should happen if students finish early or struggle significantly?

### Examples, diagrams, proofs, and practice

- How many teaching examples and practice problems are desired for each major idea?
- Should problems be drawn from the textbook, newly written, or both?
- Are complete solutions required, or only answers and facilitator cues?
- Which ideas require diagrams, comparison figures, constructions, or sequential board drawings?
- Should diagrams be ready-to-print figures, board-drawing guides, or both?
- Are colour and grayscale printing constraints relevant?
- Which proofs must be taught, and should they be discovered, motivated, completed collaboratively, or presented?
- Should the core material function as the student recording/learning sequence, or is separate notebook work needed?
- Is a student guide or worksheet also required, or only the facilitator copy?
- How large should the continuation bank be?

### Document and delivery

- Is there a later approved PDF, LaTeX file, or earlier facilitator copy that should override the bundled visual design?
- Is that source for design only, content only, or both?
- What level of detail and page length is acceptable?
- How should occasional facilitator-only notes be visually distinguished?
- Should the preparation overview occupy one page?
- Are there requested exceptions to the bundled typography, colour, box, spacing, or symbol-formatting rules?
- Is any secondary export required in addition to the standard `.tex` and `.pdf`?
- What filename and destination folder should be used?

Use answers from earlier messages and supplied documents instead of asking the user to repeat them. Nevertheless, surface inferred decisions in the agreed brief so they can be corrected before drafting.

### Drafting gate

Before creating the document, give the user a compact plan showing:

1. class destination and scope;
2. proposed learning sequence with approximate time;
3. main activities and questioning approach;
4. planned examples, diagrams, proofs, practice, notebook work, and reserve bank;
5. intended page structure and design source;
6. output files and delivery location;
7. explicit assumptions.

Do not cross this gate until the user approves the plan or directly instructs the skill to proceed without further consultation.

## Facilitator-copy relationship to student material

Treat the facilitator copy as the fuller version of the same learning resource, not as a separate classroom-performance script.

The shared core should contain:

- context or linking situation;
- activity or exploration;
- diagrams, tables, and observation structures;
- learner-facing questions;
- explanations and formal mathematics;
- examples, exercises, and practice.

Add to the facilitator copy only where useful:

- pedagogical purpose that is not self-evident;
- short setup or timing information;
- important misconception alerts;
- expected observations when diagnostically valuable;
- a key discussion intervention;
- answers, solution cues, or extensions;
- essential practical or proof guidance.

If a student version is later requested, derive it mainly by removing facilitator-only notes and answers—not by rewriting the entire learning sequence.

Use this test: if removing the facilitator callouts leaves a coherent, learnable student resource, the relationship is correct.

## Lesson architecture

A strong underlying route is:

1. **Create the need** — a visual puzzle, contrast, construction, or question.
2. **Recall what is needed** — a short prerequisite connection, not a long review.
3. **Experience or explore** — learners manipulate, measure, compare, draw, or reason.
4. **Notice and name** — collect observations, then introduce precise vocabulary.
5. **Represent** — connect the picture to notation, equations, or conventions.
6. **Discover** — move toward the relationship or theorem through the material.
7. **Formalise or prove** — make the reasoning explicit.
8. **Apply and vary** — clean example, changed orientation/labels, misconception case.
9. **Check understanding** — one small task that exposes whether the destination was reached.
10. **Continue if useful** — extra practice, recovery route, extension, and next-class bridge.

This is an internal design pattern, not a required visible document structure. Express it naturally through the learning material. Do not turn every stage into a labelled teacher instruction. Merge or reorder stages when the mathematics requires it.

## Learning-section test

A section is ready when:

- the mathematical purpose is clear from the activity or content;
- the learner knows what to consider, do, record, or solve;
- questions and examples move naturally toward the intended idea;
- the explanation or formalisation appears at the right moment;
- diagrams and practice are sufficient to make the section learnable;
- a facilitator can conduct it flexibly without a line-by-line script;
- any facilitator-only note is essential and placed exactly where needed.

Avoid both extremes: do not write abstract background commentary that cannot be used for learning, and do not micromanage the facilitator with a separate cue for every classroom action.

## Diagram test

Include a diagram if it does at least one of the following:

- makes a definition visible;
- shows invariant structure across orientation or size;
- clarifies correspondence;
- provides a counterexample;
- supports a construction;
- lets students conjecture;
- exposes the steps of a proof;
- reduces dependence on vertex-heavy prose.

For every diagram verify:

- labels are unambiguous and consistent with the text;
- intended equalities, parallels, or ratios are visually marked;
- the figure remains readable when printed;
- any essential draw order or visual emphasis is evident or stated briefly;
- it does not falsely imply a special case;
- it is large enough to teach from.

## Example progression

For each major idea, use a compact progression:

1. **See it** — obvious visual or numerical case.
2. **Say why** — guided explanation.
3. **Change the surface** — rotate, relabel, resize, or change representation.
4. **Catch the trap** — non-example or common misconception.
5. **Do independently** — short transfer task.

Include solution cues where the facilitator may need quick support. Keep complete worked solutions for non-routine or proof-based questions.

## LaTeX production

Use the bundled `assets/math-lesson-template.tex` as the source skeleton and follow `references/latex-design-system.md` exactly. Keep LaTeX as the authoritative source for every document.

- Preserve the template preamble and semantic environments unless a required mathematical package must be added.
- Draw mathematical figures in TikZ so labels, line weights, colour, and scaling remain consistent.
- Use ordinary prose and theorem environments for most content; reserve pale panels for high-value summaries and rare facilitator notes.
- Keep the pages compact through disciplined writing and spacing, not by reducing the base font or margins.
- Compile with `pdflatex` at least twice.
- Treat material warnings, missing references, overfull boxes, and unavailable glyphs as defects.
- Render every page and inspect the latest PDF at readable size before delivery.

## Revision rules

Apply these interpretations consistently:

| Feedback | Revision |
|---|---|
| Too abstract | Begin with objects, numbers, motion, comparison, or diagrams; delay notation. |
| Too few diagrams | Add teaching figures at correspondence, discovery, counterexample, construction, and proof points. |
| Too verbose | Remove repeated explanation and compress directions while preserving the mathematical transitions. |
| Too many highlights | Reserve panels for decisions or cautions; use headings and whitespace elsewhere. |
| Not enough material | Add examples, recovery explanations, and extension problems to the continuation bank. |
| Too playful | Use conventional academic language and restrained typography. |
| Hard to revise quickly | Improve headings, sequencing, summaries, and local facilitator notes without adding a full script. |
| Symbols formatted poorly | Match the approved source/template and inspect the rendered PDF at normal reading size. |
| Design drift | Return to the bundled LaTeX template and exact values in the design-system reference. |
| Too much hand-holding | Remove repeated Prepare/Say/Ask/Observe/Board/Notebook cues and retain only essential facilitator notes. |
| Too different from student workbook | Rebuild around one shared learning sequence; make the facilitator copy the annotated fuller version. |

## Delivery checklist

Before delivery:

- compile or export successfully;
- compile the LaTeX source with `pdflatex` at least twice;
- inspect every page visually;
- verify mathematical notation and diagram labels;
- verify timing totals;
- confirm self-contained reference material;
- confirm the main body reads as learning material rather than teacher directions;
- confirm facilitator-only notes are sparse and essential;
- confirm a student version could be produced mainly by removing notes and answers;
- confirm the continuation bank is separated from the essential route;
- retain the requested filename;
- always include the editable `.tex` source and compiled `.pdf`;
- save to the requested connected destination only after resolving the exact folder.
````

#### C.3 references/latex-design-system.md

````markdown
# LaTeX design system

Use this specification for every Math Lesson Builder document. It is extracted from the approved `Similar-Triangles-Part-1.tex` source and its compiled 13-page A4 PDF. The source lesson content is not part of this design system.

## Contents

- Authoring and compilation
- Page and typography
- Colour
- Header and footer
- Opening hierarchy
- Section hierarchy
- Theorem-like content
- Exercises and answers
- Panels and facilitator notes
- Mathematics
- Diagrams
- Lists and spacing
- Links
- Prohibited design drift
- Visual QA

## Authoring and compilation

- Author in LaTeX only.
- Use `\documentclass[11pt,a4paper]{article}`.
- Compile with pdfLaTeX. Run `pdflatex` at least twice; run again if references remain unresolved.
- Deliver the `.tex` and compiled `.pdf`.
- Keep the bundled template as the authoritative skeleton.

## Page and typography

- Use A4 portrait.
- Set uniform margins with `\usepackage[margin=2.3cm]{geometry}`.
- Retain LaTeX's Computer Modern family; do not load a substitute body font.
- Use serif roman body text, serif italic emphasis, and serif bold emphasis.
- Set `\parindent` to `0pt`.
- Set `\parskip` to `4pt`.
- Keep body text black.
- Do not reduce the 11-point base size to fit more content. Edit or reflow instead.
- Do not use columns.

## Colour

Use exactly two custom colours:

```tex
\definecolor{accent}{RGB}{0,84,147}
\definecolor{panel}{RGB}{232,242,250}
```

- `accent` is the single deep academic blue, equivalent to `#005493`.
- `panel` is the single pale-blue background, equivalent to `#E8F2FA`.
- Use `accent` for the main title, theorem/example/definition labels, exercise headings, panel labels, and primary TikZ geometry.
- Use `panel` only for full-width, high-value information panels.
- Keep section headings, body text, mathematics, page numbers, and most diagram annotations black.
- Do not introduce additional decorative colours, gradients, shadows, borders, or colour-coded cue systems.

## Header and footer

Use `fancyhdr`:

```tex
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape <module title>}
\fancyhead[R]{\small\itshape <part title>}
\fancyfoot[C]{\thepage}
```

- Retain the default thin header rule.
- Use small italic running heads.
- Put the module/chapter title on the left and part/class title on the right.
- Centre the page number in the footer.
- Do not add logos, footer text, dates, or decorative rules unless explicitly requested.

## Opening hierarchy

Centre the opening block:

```tex
\begin{center}
{\color{accent}\LARGE\bfseries <UPPERCASE MODULE TITLE>}\\[4pt]
{\Large <Part or class subtitle>}\\[6pt]
{\small <brief descriptor>}
\end{center}
\medskip
```

- Main title: uppercase, `\LARGE`, bold, accent blue.
- Subtitle: `\Large`, black, regular weight.
- Descriptor: `\small`, black.
- Use 4 pt between title and subtitle and 6 pt between subtitle and descriptor.
- Follow with `\medskip`, then an optional pale-blue objectives panel.
- Do not make a separate cover page.

## Section hierarchy

- Use ordinary numbered `\section{...}` headings from the `article` class.
- Keep section headings black and bold.
- Use `\subsection*{Worked examples}` or another unnumbered subsection only when a secondary grouping is useful.
- Do not put section headings inside coloured boxes.
- Let whitespace and typography establish hierarchy.
- Avoid orphaned headings and headings stranded at page bottoms.

## Theorem-like content

Load `amsmath`, `amssymb`, and `amsthm`.

Use these exact theorem styles:

```tex
\newtheoremstyle{brand}{9pt}{9pt}{\itshape}{}{\bfseries\color{accent}}{.}{ }{}
\newtheoremstyle{branddef}{9pt}{9pt}{}{}{\bfseries\color{accent}}{.}{ }{}
```

- `brand`: 9 pt space above and below, italic body, bold accent heading, period after heading.
- `branddef`: 9 pt space above and below, upright body, bold accent heading, period after heading.

Use:

```tex
\theoremstyle{brand}
\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\theoremstyle{branddef}
\newtheorem{definition}{Definition}
\newtheorem{example}{Example}[section]
\newtheorem{illus}{Illustration}
\newtheorem{remark}{Remark}
\newtheorem*{activity}{Activity}
```

- Number examples by section.
- Keep theorem and corollary numbering global, as in the approved source.
- Keep definitions, illustrations, and remarks in the upright `branddef` style.
- Keep activities unnumbered unless the lesson requires explicit activity numbering.
- Use the standard `proof` environment. Do not box proofs.
- Preserve conventional bold inline labels such as `Given.`, `To prove.`, and `Construction.` where a formal school proof uses them.

## Exercises and answers

Use this exercise treatment:

```tex
\newenvironment{exercise}[1]
  {\par\medskip\noindent{\large\bfseries\color{accent}Exercise #1}
   \par\smallskip
   \begin{enumerate}[leftmargin=*, itemsep=4pt]}
  {\end{enumerate}}
```

- Exercise heading: large, bold, accent blue.
- No box or horizontal rule around exercises.
- Use full-width numbering with `leftmargin=*`.
- Use 4 pt between top-level exercise items.
- Use compact roman or alphabetic nested lists with `itemsep=1pt`.

Use this compact answer treatment:

```tex
\newenvironment{answerblock}
  {\par\smallskip\noindent\textbf{\color{accent}Answers.}\ }
  {\par\medskip}
```

- Keep the `Answers.` label bold and accent blue.
- Keep routine answers compact and inline when readable.
- Use full worked solutions in the main flow for non-routine examples and proofs.
- Do not place answers in a large decorative box.

## Panels and facilitator notes

Use borderless `\colorbox{panel}` with an inner `\parbox` whose width is:

```tex
\dimexpr\linewidth-2\fboxsep\relax
```

Use the exact summary panel pattern:

```tex
\newcommand{\rememberbox}[1]{%
  \par\medskip\noindent
  \colorbox{panel}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \medskip
      \textbf{\color{accent}\large Things to Remember}
      \par\smallskip #1 \medskip}}
  \par\medskip}
```

- Use pale panels sparingly: opening objectives, a final `Things to Remember` summary, or a rare critical facilitator note.
- Do not give every activity, example, or instruction a panel.
- Do not use outlines, rounded corners, icons, drop shadows, or sidebars.
- Style a necessary facilitator note as a short pale panel with a bold accent label. Keep it local and concise.
- If the note is not essential, omit it.

## Mathematics

- Use `amsmath` display environments and standard Computer Modern mathematics.
- Use `\[` and `\]` for unnumbered displays.
- Use `\tag{...}` only when the teaching sequence refers to named proof steps.
- Prefer proper fractions with `\frac` or `\dfrac`; never simulate fractions with slashes in formal mathematics.
- Use `\operatorname{ar}` or another explicit operator for named quantities.
- Use `\text{...}` for units and prose inside mathematics.
- Define `\newcommand{\tr}{\triangle}` and use it consistently for triangle notation.
- Use `\qedhere` only where necessary to place the proof-ending symbol correctly.
- Keep equations centred and give long chains enough room; split them rather than shrinking them.

## Diagrams

- Create mathematical diagrams in TikZ.
- Centre figures with `center` plus `tikzpicture`; do not use floating figures unless float behaviour is specifically needed.
- Draw the primary mathematical object with `thick,accent`.
- Use black `thick` lines when a neutral reference structure is clearer.
- Use black dashed lines for constructions, auxiliaries, heights, or extensions.
- Place mathematical labels close to their vertices or lines using `above`, `below`, `left`, `right`, and combined positions.
- Use ordinary mathematical italic labels.
- Keep captions short and place them as `\small` TikZ nodes beneath the diagram, for example `Fig.\ 3`.
- Use a moderate scale near `0.9` to `1.05`; size each figure for legibility rather than forcing one scale.
- Keep figures unboxed and surrounded by whitespace.
- Ensure the figure remains intelligible in grayscale through line style and geometry, not colour alone.
- Avoid raster illustrations for mathematical geometry when TikZ can express them precisely.

## Lists and spacing

Load `enumitem`.

- Use `leftmargin=1.6em`, `itemsep=1pt`, and `topsep=2pt` for compact panel lists.
- Use `itemsep=1pt` for compact definition and theorem sublists.
- Use `itemsep=4pt` for top-level exercise questions.
- Use `\medskip` before and after major custom blocks.
- Use `\smallskip` between a custom heading and its contents.
- Do not compress pages with negative vertical space.

## Links

Load:

```tex
\usepackage[
  colorlinks=true,
  linkcolor=blue!55!black,
  urlcolor=blue!55!black
]{hyperref}
```

- Use coloured text links, not boxed links.
- Keep internal and URL links in the restrained dark-blue link colour.

## Prohibited design drift

Do not:

- change the margins, paper size, base font, or font family;
- replace Computer Modern with a modern sans-serif or branded font;
- colour section headings blue;
- turn ordinary content into cards or boxes;
- add decorative icons, banners, cover graphics, gradients, or multiple accent colours;
- introduce repeated `Say`, `Ask`, `Observe`, `Board`, or `Notebook` labels;
- use page-number references when named sections, examples, exercises, or theorems are available;
- shrink diagrams, mathematics, or body text merely to reduce page count;
- copy content from the source Similar Triangles module.

Only depart from this design when the user explicitly requests a change after being told what will change and why.

## Visual QA

After compilation:

1. Check the PDF is A4 portrait with the intended page count.
2. Confirm Computer Modern fonts are embedded.
3. Render every page to PNG.
4. Inspect title balance, headers, thin header rule, centred page numbers, margins, paragraph density, panel widths, theorem spacing, exercises, answers, figures, and final summary.
5. Check that pale panels are full-width, borderless, and rare.
6. Check TikZ labels and lines at readable size.
7. Check for overfull boxes, clipped equations, broken glyphs, unresolved references, awkward page breaks, and excess blank space.
8. Recompile and re-render after every material correction.
````

#### C.4 assets/math-lesson-template.tex

````latex
\documentclass[11pt,a4paper]{article}

\usepackage[margin=2.3cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage[colorlinks=true,linkcolor=blue!55!black,urlcolor=blue!55!black]{hyperref}

\definecolor{accent}{RGB}{0,84,147}
\definecolor{panel}{RGB}{232,242,250}

\newtheoremstyle{brand}{9pt}{9pt}{\itshape}{}{\bfseries\color{accent}}{.}{ }{}
\newtheoremstyle{branddef}{9pt}{9pt}{}{}{\bfseries\color{accent}}{.}{ }{}

\theoremstyle{brand}
\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}

\theoremstyle{branddef}
\newtheorem{definition}{Definition}
\newtheorem{example}{Example}[section]
\newtheorem{illus}{Illustration}
\newtheorem{remark}{Remark}
\newtheorem*{activity}{Activity}

\newcommand{\tr}{\triangle}

\newenvironment{exercise}[1]
  {\par\medskip\noindent{\large\bfseries\color{accent}Exercise #1}
   \par\smallskip
   \begin{enumerate}[leftmargin=*,itemsep=4pt]}
  {\end{enumerate}}

\newenvironment{answerblock}
  {\par\smallskip\noindent\textbf{\color{accent}Answers.}\ }
  {\par\medskip}

\newcommand{\rememberbox}[1]{%
  \par\medskip\noindent
  \colorbox{panel}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \medskip
      \textbf{\color{accent}\large Things to Remember}
      \par\smallskip #1 \medskip}}
  \par\medskip}

\newcommand{\facilitatornote}[1]{%
  \par\medskip\noindent
  \colorbox{panel}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \smallskip
      \textbf{\color{accent}Note to Facilitator.}\ #1
      \smallskip}}
  \par\medskip}

% Replace these values for each lesson.
\newcommand{\ModuleTitle}{MODULE TITLE}
\newcommand{\PartTitle}{Part or Class Title}
\newcommand{\ModuleDescriptor}{A teaching module for school mathematics}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\itshape \ModuleTitle}
\fancyhead[R]{\small\itshape \PartTitle}
\fancyfoot[C]{\thepage}

\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}

\begin{document}

\begin{center}
{\color{accent}\LARGE\bfseries \MakeUppercase{\ModuleTitle}}\\[4pt]
{\Large \PartTitle}\\[6pt]
{\small \ModuleDescriptor}
\end{center}

\medskip
\colorbox{panel}{%
  \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \textbf{\color{accent}Learning objectives.}
    By the end of this lesson, students should be able to:
    \begin{itemize}[leftmargin=1.6em,itemsep=1pt,topsep=2pt]
      \item replace this line with a precise learning objective;
      \item replace this line with another precise learning objective.
    \end{itemize}}}

% Build the lesson as continuous learning material.
% Use ordinary sections, prose, activities, diagrams, examples, and exercises.
% Insert \facilitatornote{...} only when the note is essential.

\section{First mathematical idea}

Replace this placeholder with the lesson material.

\begin{example}
Replace this placeholder with a worked example.
\end{example}

\begin{exercise}{1.1}
  \item Replace this placeholder with a practice question.
\end{exercise}

\begin{answerblock}
1.\ Replace this placeholder with the answer.
\end{answerblock}

\rememberbox{%
  \begin{enumerate}[leftmargin=1.6em,itemsep=2pt,topsep=2pt]
    \item Replace this placeholder with a concise mathematical summary.
  \end{enumerate}}

\end{document}
````

#### C.5 agents/openai.yaml

````yaml
interface:
  display_name: "Math Lesson Builder"
  short_description: "Build clean LaTeX mathematics teaching material"
  default_prompt: "Use $math-lesson-builder to create LaTeX teaching material for my next mathematics chapter."
policy:
  products:
  - chatgpt
  - codex
  - api
  - atlas
  allow_implicit_invocation: true
````

### Appendix D. Review checklist (word for word)

File: `/mnt/project-files/review-standard/review-checklist.md`. Under the lean quality bar (11 Oct 2026), one cheap checker covers sections 1 and 2 (maths and diagrams); the main model covers sections 3 to 6 itself while writing and in the final look. The six separate checkers are no longer run.

````markdown
# Review checklist for teaching materials

Every class sheet, homework, test and facilitator copy (fc) must pass this review before it goes to Shashi. Checkers work from the **compiled PDFs**, which are exactly what students and teachers see.

## General rules for every checker
- Report problems only. For each one, give the page, the question or section, what is wrong, why it matters for learning, and a suggested fix.
- Mark each problem **Must fix** (wrong, misleading or confusing) or **Should fix** (weak or unclear).
- Use only the syllabus taught up to this point (see the scope notes in the brief). Anything beyond it is a problem.
- Do not praise. If a section has no problems, say "no issues".

## 1. Maths checker
- Solve every question and example from scratch **before** you read the given answer. Then compare.
- Check that every answer in the fc is correct, complete and shows the method a student should write.
- Check that the data is possible: the figure can exist, lengths fit together, heights are not longer than the sides they meet, angles are possible.
- Check that the numbers stay clean: no unplanned decimals or ugly fractions unless the question needs them.
- Check units in the question, the working and the answer.

## 2. Diagram checker
- Compare every diagram with its text: each label, length, letter, right-angle mark and shaded region.
- Check rough proportions. A length marked 15 must not look shorter than one marked 12 without a reason.
- Check that perpendicular lines look perpendicular, midpoints look like midpoints, and parallel lines look parallel.
- Check readability: no labels overlapping lines or other labels, and no label that could belong to two objects.
- Flag any diagram that could mislead, for example one where a sloping side looks like the height.

## 3. Student checker
Attempt the sheet twice, first as an average Grade 9 student and then as a weak Grade 9 student. Use only what has been taught.
- Can you tell **exactly what to find** from the text alone? Every example and question must state it ("Find ...", "Explain ...", "Draw ...").
- Is any word, name or setting unfamiliar? Is any sentence unclear, or could it be read two ways?
- Is any information missing or extra in a way that is not deliberate?
- Report where you got stuck and why.

## 4. Teaching checker
- Tag each question with the skill it tests: direct use, working backwards, explaining or justifying, finding a mistake, drawing or constructing, comparing or "what if", real-life application.
- An exercise set must test the learning objective from several angles. **At most one** question per set may be plain substitution into a formula.
- Questions should go from easy to hard.
- Flag anything that looks fine but weakens learning: a question that can be answered without understanding, a wrong idea that could be reinforced, or an answer explanation that does not teach the idea.
- Check that the questions match the learning objectives of the section.

## 5. Proofreader
- Typos, grammar, punctuation, notation (the same symbol for the same thing every time), units and number formats.
- House style: "Assignment" + date heading on homework, no section labels or question titles on student sheets, Century Schoolbook font, full-size fractions, ₹ for rupees.
- The student copy and the fc must match **word for word** in every question. The only difference is the teacher-only text.
- Plain English with Indian settings. No regional words that students may not know.

## 6. Language checker (fc teacher-only text)
This applies to notes, the overview and answer explanations. The aim: any teacher can use the fc without help.
- Use the core rules of Simplified Technical English (ASD-STE100): short sentences (up to about 20 words), one point per sentence, active voice, simple common words, the same term for the same thing.
- No internal or technical words: TikZ, trap, invariant, structural, scaffold, and similar.
- **Common mistake notes:** keep one only if (a) students really make this mistake with this exact idea, and (b) knowing it in advance changes what the teacher does. It is at most 2 short sentences: the mistake, then what to ask or say. Remove any note that fails this test. Most sections need none.
- Answer explanations must be simple and clear, and show the steps a student should write.

## After the review
- Fix every Must fix. Fix Should fix items unless there is a good reason not to (note the reason).
- **Never use global find-and-replace on numbers.** Edit each place by hand.
- After any fix, rebuild both PDFs, check **all pages** of both copies again, and compare the old and new text so only the intended changes got through.
- Send Shashi a short review note: what was checked, what was found, and what was fixed.
````

### Appendix E. Working LaTeX preambles (copied from the files)

#### E.1 Class notes preamble (`body-source.tex`, Class 2 revised, 11 Oct 2026)

Prepend `\newif\ifteacher\teacherfalse` (student) or `\newif\ifteacher\teachertrue` (fc) as the first line.

````latex
\documentclass[11pt,a4paper]{article}

\usepackage[margin=2.3cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}
\usepackage{tgschola}
\usepackage{fouriernc}
\usepackage{microtype}
\usepackage{tfrupee}
\linespread{1.04}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{tikz}
\usetikzlibrary{angles,quotes,calc,arrows.meta}
\usepackage{enumitem}
\usepackage{needspace}
\usepackage{fancyhdr}
\usepackage[hidelinks]{hyperref}

\definecolor{accent}{RGB}{38,52,70}
\definecolor{panel}{RGB}{236,238,241}

\newtheoremstyle{brand}{9pt}{9pt}{\itshape}{}{\bfseries\color{accent}}{.}{ }{}
\newtheoremstyle{branddef}{9pt}{9pt}{}{}{\bfseries\color{accent}}{.}{ }{}
\theoremstyle{brand}
\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\theoremstyle{branddef}
\newtheorem{definition}{Definition}
\newtheorem{example}{Example}[section]
\newtheorem{illus}{Illustration}
\newtheorem{remark}{Remark}
\newtheorem*{activity}{Activity}

\newcommand{\tr}{\triangle}
\newenvironment{exercise}[1]
  {\par\medskip\Needspace{7\baselineskip}\noindent{\large\bfseries\color{accent}Exercise #1}
   \par\smallskip
   \begin{enumerate}[leftmargin=*,itemsep=4pt]}
  {\end{enumerate}}
\definecolor{muted}{RGB}{70,72,76}
\newcommand{\nl}{\\[3pt]}
\ifteacher
\newenvironment{answerblock}
  {\par\smallskip\begingroup\small\linespread{1.15}\selectfont\color{muted}\noindent\textit{Answers.}\par}
  {\par\endgroup\medskip}
\newcommand{\ans}[1]{\par\smallskip\noindent\textbf{#1}\ }
\else
\usepackage{comment}
\excludecomment{answerblock}
\fi
\newcommand{\figph}[1]{\begin{center}\fbox{FIGURE #1}\end{center}}
\newcommand{\rememberbox}[1]{%
  \par\medskip\noindent
  \colorbox{panel}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \medskip
      \textbf{\color{accent}\large Things to Remember}
      \par\smallskip #1 \medskip}}
  \par\medskip}
\ifteacher
\newcommand{\facilitatornote}[1]{%
  \par\medskip\noindent
  \colorbox{panel}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \smallskip
      {\small\textbf{Note for the teacher.}\ #1}
      \smallskip}}
  \par\medskip}
\else
\newcommand{\facilitatornote}[1]{}
\fi

\newcommand{\ModuleTitle}{PERIMETER AND AREA}
\newcommand{\PartTitle}{Class 2}
\newcommand{\ModuleDescriptor}{Grade 9 mathematics facilitator copy}

\pagestyle{plain}
\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}


\titleformat{\section}{\large\bfseries}{\thesection}{0.8em}{}
\titlespacing*{\section}{0pt}{16pt}{6pt}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{0.6em}{}
% plain ruled panels instead of coloured boxes
\renewcommand{\colorbox}[2]{\par\smallskip\noindent\textcolor{black!35}{\rule{\linewidth}{0.4pt}}\par\nointerlineskip\vspace{3pt}\noindent#2\par\vspace{2pt}\noindent\textcolor{black!35}{\rule{\linewidth}{0.4pt}}\par\smallskip}
````

#### E.2 Class notes opening (heading and the two overview blocks)

````latex
\begin{document}

\noindent{\LARGE Perimeter and Area}\hfill{\large Class 2}\par\vspace{3pt}
\noindent\rule{\linewidth}{0.6pt}\par\medskip

\ifteacher
\colorbox{panel}{%
  \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \small\textbf{Teacher's copy: overview.}
    \begin{itemize}[leftmargin=1.6em,itemsep=1pt,topsep=2pt]
      \item \textbf{Aims.} Students find arc length and the perimeter of a sector. They find the area of a parallelogram and a triangle with the perpendicular height. They explain why two shapes have equal area. They use Heron's formula. They find the area of a circle and a sector. They use cm for lengths and cm$^2$ for areas.
      \item \textbf{Before the class.} Have a ruler, a compass and a set square. Revise the circumference of a circle, the area of a rectangle, the midpoint of a line and the Pythagoras theorem.
      \item \textbf{If time is short.} Teach the first example in each section. Give the second examples and the last two sections as homework.
      \item \textbf{Exercises.} Each exercise starts with one direct question. The other questions ask students to work backwards, find a mistake, explain, draw or compare. Ask students to write every step.
    \end{itemize}}}
\else
\colorbox{panel}{%
  \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \textbf{\color{accent}How to use this companion.}
    Read, discuss, and refer to the diagrams and questions during class. Do every calculation and write every explanation in your notebook.}}
\fi
````

#### E.3 Homework preamble (`homework 2 fc.tex`, 11 Oct 2026; the student copy differs only in its first line)

````latex
\newif\ifteacher\teachertrue
\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.4cm,top=2.2cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{tgschola}\usepackage{fouriernc}
\linespread{1.08}
\usepackage[T1]{fontenc}
\usepackage{microtype}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{angles,quotes,calc,arrows.meta}
\usepackage{enumitem}
\usepackage{needspace}
\definecolor{accent}{RGB}{38,52,70}
\definecolor{panel}{RGB}{233,236,240}
\definecolor{muted}{RGB}{70,72,76}
\pagestyle{plain}
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt}
\setlength{\lineskiplimit}{2pt}\setlength{\lineskip}{4pt}
\newcommand{\tr}{\triangle}
\newcommand{\nl}{\\[3pt]}
\ifteacher
\newenvironment{answerblock}
  {\par\needspace{8\baselineskip}\smallskip\begingroup\small\linespread{1.15}\selectfont\color{muted}\noindent\textit{Answer.}\par}
  {\par\endgroup\medskip}
\newcommand{\ap}[1]{\par\smallskip\noindent\textbf{(#1)}\ }
\else
\usepackage{comment}
\excludecomment{answerblock}
\fi
\newcounter{hwn}
\newenvironment{hwq}{\stepcounter{hwn}\begin{enumerate}[label=\textbf{\arabic*.},leftmargin=1.6em,labelsep=0.5em,itemsep=4pt,start=\value{hwn},topsep=11pt]}{\end{enumerate}}
\newlist{parts}{enumerate}{1}
\setlist[parts]{label=(\alph*),itemsep=1pt,topsep=3pt,leftmargin=2em}
````

#### E.4 Homework opening (Assignment heading, student instruction, teacher overview)

````latex
\begin{document}
\thispagestyle{plain}
\noindent{\LARGE Assignment}\hfill{\large 11 October 2026}\par\vspace{3pt}
\noindent\rule{\linewidth}{0.6pt}\par
\vspace{2pt}{\small\itshape For every question, first draw a rough diagram in your notebook and mark all the given measurements on it. Write every step of your reasoning, not only the answer.}\par
\ifteacher
\vspace{4pt}{\small\color{muted}\textit{Teacher's copy.} This homework uses four ideas:
\begin{itemize}[leftmargin=1.5em,itemsep=0pt,topsep=2pt]
\item Area of a parallelogram $=$ base $\times$ height.
\item Area of a triangle $=\dfrac12\times$ base $\times$ height.
\item The height of an obtuse triangle can fall outside the triangle.
\item A median divides a triangle into two triangles of equal area.
\end{itemize}
The height is the distance at right angles to the base line. In an obtuse triangle, extend the base line to meet the height. Questions 1 to 3 are easy to medium. Questions 4 to 6 are medium to hard. Only Question 4(b) needs the Pythagoras theorem.

\textbf{Common mistake:} Students often use a slanting side as the height. Ask: ``Is this length at right angles to the base?''}\par
\fi
````

---

*End of handbook. Compiled 27 October 2026 from the project instructions, project memory, Shashi's account skills, the review checklist, the project LaTeX files, all project threads and chat, and the rule files and memory on Shashi's laptop.*
