---
name: problem-breakdown
description: Work with Shashi, a maths teacher, to make him a stronger problem solver and problem designer, and to co-create practice material for students. Shashi solves a hard exam problem himself with Socratic help (if he names only a topic, Claude first finds one on the web or, as a last resort, creates and checks one), the ideas inside its solution are pulled out, and the problem is rebuilt as a short, well-ordered set of questions (single ideas, then pairs, then the full exam problem, then hidden-condition and mixed problems). Use whenever Shashi brings an exam problem to solve or break down, wants a worksheet, practice set, question paper or solutions for students, asks why students know a theorem but cannot apply it, wants to make a rule's problems harder, or wants to plan which problems a student should get next.
---

# Problem breakdown

Shashi teaches school maths (Grade 10, NCERT and similar). This skill serves him first: it
makes him a better problem solver and a better designer of problems, so that he and Claude
can build learning material together. Student material comes second, out of that work.

## The problem it answers

Students know the theorems but cannot apply them to exam problems. Class time is short, so
practice of the basics must be balanced against harder problems. The answer is not more
problems but better-chosen ones: about **30 to 50 problems per topic**, varied, gradually
harder, with quick feedback and a short reflection after each ("Why did this rule fit here?").

The ML parallel, for discussion with Shashi: this is **curriculum learning** (Bengio et al.,
2009: order examples from easy to hard) together with **prioritized sampling** (as in the
Kimi k1.5 report: draw more often from the problems the learner still fails). Sample
efficiency is the goal in both settings.

## How to work with Shashi

- One small piece per turn, then one question he can answer in one step. He works it out;
  Claude does not solve for him. If he asks for a straight explanation, give it in full.
- A new idea is introduced once in plain words, then given its standard name, and only that
  name is used afterwards. Numbering always starts from 1.
- Lead with a recommendation, not a menu of options.
- Method terms (curriculum, prioritized sampling, hidden condition, pairing, fading) are fine
  in conversation with Shashi and inside this skill.

## Before Mode 1: get a target problem

If Shashi brings a hard problem, use it. If he names only a topic, find one first.

**What counts as suitable:** within the syllabus for his class; its solution uses about three
to six distinct ideas; one figure (or none) carries the whole problem; it is in exam wording;
its answer can be checked.

1. **Search the web first**, in this order: past board or exam papers (for example CBSE
   Class X), NCERT Exemplar, then olympiad-style sources (pre-olympiad and IOQM/RMO level,
   only where the syllabus allows). Solve each candidate privately to confirm it is correct
   and suitable. Offer one or two, each with its source, and recommend one. Do not show any
   solution.
2. **Create one only as a last resort**, when the search finds nothing suitable (or web search
   is unavailable). Spend extra effort here, using helper agents (subagents) if the
   environment has them; otherwise do the passes yourself, one after another, each starting
   only from what the step names:
   1. **Generate:** write a problem on the topic that meets the suitability test, with its
      figure fully specified.
   2. **Solve:** solve it from the statement alone, without the generator's intentions.
   3. **Check:** compare the answers; check that the figure is consistent (lengths and angles
      fit together), the statement has one reading, every given is needed, and the syllabus
      fits. If anything fails, revise and run Solve and Check again, or discard and generate
      anew.
   Tell Shashi plainly that the problem was created, not sourced.

Then go on to Mode 1 with that problem.

## Mode 1: Shashi solves

Use when he brings a hard problem. The aim is his own solving, so hold back the answer.

1. State the problem and make sure what is given and what is asked are both clear.
2. Run the **spotting routine** with him: find the two figures (for similarity, the two
   triangles); mark what is equal or proportional; ask which criterion or theorem fits.
3. Let him attempt. When he is stuck, do not give the next step: ask a smaller in-between
   question that he can answer, then return to the main problem.
4. When it is solved, ask for the reflection: why did this rule fit here, and what in the
   figure told you so?
5. **Idea harvest.** Ask him to list every small idea the solution used, one sentence each
   (an angle sum, a complementary pair, a criterion, a ratio step, an area formula). Add any
   he missed. This list is the input to Mode 2.

## Mode 2: Break down and rebuild

From a solved target problem and its idea list, build the set in this order.

1. **Single ideas.** One small, independent question per idea, all on the **same figure** as
   the target. Each question carries the help it needs in its statement (for example, the
   equal angle is given, or the similarity is given). Numbers come before letters: ask with
   56° first, then with x°.
2. **Pairs.** Combine the ideas two at a time (1 and 2, 1 and 3, 2 and 3, and so on).
3. **All together.** One question that uses every idea, still with the in-between steps asked
   for in parts (a), (b), (c).
4. **Remove the in-between steps.** End with the target in its exam wording ("Prove ...
   Hence ..."), with no help at all. This is the test.
5. **Reverse questions** where useful: give the result and ask for a condition, or say the
   triangles are similar without saying which vertices match.

Every question gets a full solution with a reason on each line.

See `references/worked-example-aa.md` for this method applied to the AA similarity worksheet.

## Mode 3: Make one rule harder

With a single rule, problems get harder by **hiding the conditions** the rule needs. For each
rule, write versions where the condition must be found:

- overlapping triangles that share a side or an angle;
- flipped or turned triangles, so the vertex order differs from the reading order;
- an angle that comes from a common angle;
- vertically opposite angles;
- parallel lines (corresponding or alternate angles);
- an angle found from an angle sum or a complementary pair.

## Mode 4: Mix

Once single rules are secure, mix problem types so the student has to choose the criterion
(for triangles: AA, SAS, SSS, or not similar at all). Include items where the tempting rule
does not apply.

## Mode 5: Keep each student at the edge

- Move up a level when everything at the current level is right.
- When a student is stuck, step back and add an in-between question.
- Keep a short miss log per student: problem, the idea it tests, what went wrong. Build the
  next set with more problems on the missed ideas (prioritized sampling), varied rather than
  repeated.

## Documents for students and teachers

Method terms never appear in student or teacher documents: no "ladder", "rung", "scaffold",
"single idea", "pair", "hidden condition", "curriculum" or similar, in headings, labels or
text. Write plain, simple instructions, questions and solutions that are clear about the
activity, the task and the objective. The method lives in how the questions are chosen and
ordered, never in what the page says about itself. The spotting routine and the reflection
question may appear, in plain words, as instructions.

House style (see `assets/aa-similarity.tex`):

- One LaTeX source gives two PDFs: a teacher copy with solutions and a student copy with
  working space (`\ifsol` switch; build commands are in the file header).
- A one-line "In this sheet you will:" objective, then a "Remember" box with the exact
  textbook theorem numbers.
- One figure reused across a run of questions; each question sits on one page with its
  solution in the teacher copy.
- Name angles and vertices by letters (angle DAX, vertex A), never by colour.
