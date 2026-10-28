# Circles lesson 1 (Grade 9, CBSE 2026-27), facilitator copy, 60 minutes
Title line: {\LARGE Circles}\hfill{\large Lesson 1}, then the rule (as in body1 style).
Register: formal teacher language, short sentences, active voice. No tool talk. Indian contexts.
Every worked example: rough diagram with measurements, **Given:**, **To find:**, numbered steps with reasons, **Answer:** with units.

## Part 1 (job 1): overview + Section 1 + Section 2
Overview panel (\colorbox{panel}{\parbox{...}{\small\textbf{Teacher's copy: overview.} itemize}}):
- Aims: students use the terms of a circle; explain why equal chords subtend equal angles at the centre and the converse; explain why the perpendicular from the centre bisects a chord and the converse; find chord lengths and distances with Pythagoras.
- Syllabus: CBSE Class IX 2026-27, Unit IV Geometry (25 of 80 marks). The syllabus asks students to "explain why" each result. Proofs here use congruence (SSS, SAS, RHS).
- Materials: compass, ruler, set square, protractor, paper circles (cut beforehand), scissors.
- Timing: Section 1, 5 min; Section 2, 15 min; Section 3, 20 min; Practice, 15 min; Exit question, 5 min.
- Later lessons: circle through three points, circumcircle.

Section 1 "Parts of a circle" (5 min). Open: wheels of a bullock cart, the Ashoka Chakra on the national flag. Definition: circle = set of all points in a plane at a fixed distance (radius) from a fixed point (centre). Terms: radius, chord (segment joining two points on the circle), diameter (chord through the centre, = 2r), arc (minor, major), segment (region between a chord and its arc), sector (region between two radii and an arc). One labelled TikZ figure with centre O: radius OA, chord PQ, diameter BC, shaded minor segment on chord PQ side (light grey), shaded sector with a different grey pattern or lighter fill. Labels must not touch lines. \facilitatornote: ask students to name each part on their own drawing; common confusion: segment vs sector.

Section 2 "Equal chords and angles at the centre" (15 min).
Activity: draw a circle centre O on tracing paper, draw two equal chords AB and CD (use compass to copy length), join OA, OB, OC, OD, measure angle AOB and angle COD. They are equal.
Theorem 1: Equal chords of a circle subtend equal angles at the centre.
Why it works: In triangles AOB and COD: OA = OC (radii), OB = OD (radii), AB = CD (given). So triangle AOB congruent to triangle COD (SSS). Hence angle AOB = angle COD (CPCT).
Theorem 2 (converse): If two chords subtend equal angles at the centre, the chords are equal. Why: OA=OC, angle AOB = angle COD, OB=OD, SAS, so AB = CD.
Figure: circle centre O, chords AB and CD in different places, radii drawn, equal-length tick marks on AB and CD, angle arcs at O.
Example 2.1: In a circle with centre O, chords PQ and RS are equal and angle POQ = 80 deg. Find angle ROS and angle ORS.
Given: PQ = RS, angle POQ = 80. To find: angle ROS, angle ORS. Steps: angle ROS = angle POQ = 80 (Theorem 1). OR = OS (radii) so triangle ORS is isosceles, angle ORS = angle OSR. 2 angle ORS = 180 - 80 = 100, so angle ORS = 50. Answer: angle ROS = 80 deg, angle ORS = 50 deg.
\facilitatornote: stress that the angles must be at the centre.

## Part 2 (job 2): Section 3 (20 min) "The perpendicular from the centre to a chord"
Activity: cut a paper circle, mark centre O. Fold to make a chord AB (crease). Fold again so A falls on B. The new crease passes through O and meets AB at right angles at its midpoint M.
Theorem 3: The perpendicular from the centre of a circle to a chord bisects the chord.
Why: OM perpendicular to AB. Triangles OMA and OMB: angle OMA = angle OMB = 90, OA = OB (radii), OM common. RHS, so AM = BM.
Theorem 4 (converse): The line joining the centre to the midpoint of a chord is perpendicular to the chord.
Why: AM = BM, OA = OB, OM common, SSS. So angle OMA = angle OMB. They form a linear pair, so each is 90.
Figure: circle centre O, chord AB horizontal below O, OM vertical to M on AB, right-angle mark at M (\ramark), OA and OB drawn, tick marks AM = MB.
Key relation box (\rememberbox): if r is the radius, d the distance of the chord from the centre and the chord has length c, then (c/2)^2 + d^2 = r^2. The distance of a chord from the centre is the length of the perpendicular from the centre.
Example 3.1: A chord is at distance 6 cm from the centre of a circle of radius 10 cm. Find the length of the chord. Diagram: O, chord AB, OM = 6, OA = 10. Given: r = 10 cm, OM = 6 cm, OM perpendicular AB. To find: AB. Steps: AM = MB (Theorem 3). Triangle OMA right-angled at M: AM^2 = OA^2 - OM^2 = 100 - 36 = 64, AM = 8. AB = 2 x 8 = 16. Answer: 16 cm.
Example 3.2 (work backwards): A chord of length 24 cm is drawn in a circle; it is 9 cm from the centre. Find the radius. AM = 12; OA^2 = 144 + 81 = 225; OA = 15. Answer 15 cm.
\facilitatornote: students often forget to halve the chord. Ask them to mark M first.

## Part 3 (job 3): Practice (15 min) + Exit question (5 min) + answers
Use \begin{exercise}{1A} ... \end{exercise} for practice, then \begin{answerblock} with \ans{1.} ... and an \ansfig rough diagram for EVERY question.
Questions (student wording, plain English):
1. The radius of a circle is 13 cm. A chord is 5 cm from the centre. Find the length of the chord. Draw a rough diagram first.
2. A chord of length 30 cm is drawn in a circle of radius 17 cm. Find the distance of the chord from the centre.
3. Chord AB of a circle with centre O is 48 cm long. OM is perpendicular to AB and OM = 7 cm. Ravi writes: radius = sqrt(48^2 + 7^2). Find his mistake, and find the correct radius.
4. In a circle with centre O, chords AB and CD are equal and angle AOB = 70 deg. Find angle COD and angle OCD. Give a reason for each step.
5. Draw a circle of radius 5 cm and a chord of length 8 cm in it. Use a set square to draw the perpendicular from the centre to the chord. Measure its length. Then find the length by calculation and compare.
6. A round dining table top has radius 50 cm. A carpenter fixes a straight wooden strip on the underside along a chord, 30 cm from the centre. Find the length of the strip.
Answers: 1) half = 12, chord 24 cm. 2) half 15, d^2 = 289 - 225 = 64, d = 8 cm. 3) He used the whole chord; AM = 24, r^2 = 576 + 49 = 625, r = 25 cm. 4) angle COD = 70 (equal chords, Theorem 1); OC = OD so angle OCD = (180 - 70)/2 = 55 deg. 5) half chord 4, d^2 = 25 - 16 = 9, d = 3 cm; the measurement should be close to 3 cm. 6) half = sqrt(2500 - 900) = 40, strip = 80 cm.
Exit question (5 min), heading "Exit question", two parts:
(a) True or false? "Every line through the midpoint of a chord passes through the centre." Give a reason. Answer: False. Only the line through the midpoint that is perpendicular to the chord passes through the centre (Theorems 3 and 4).
(b) A chord of length 10 cm is in a circle of radius 13 cm. How far is it from the centre? Answer: 12 cm (5^2 + d^2 = 169, d = 12).
\facilitatornote after practice: if time is short, set Questions 5 and 6 as homework.
