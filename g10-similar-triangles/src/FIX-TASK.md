# Figure fixes (round 2)

Edit only the TikZ code of the figures listed below, in body1.tex, body2.tex and body3.tex.
Do not change any text, maths, questions or answers. Do not touch preamble.tex or any other file.
Follow the house style in FIGURE-TASK.md.

body1.tex
1. Figure inside the example "Prove that AD/AB = AE/AC" (Example 2.2, the \exfig right after that example's first paragraph):
   remove the side labels AD, AB, AE, AC. Keep only the vertex letters A, B, C, D, E and the parallel arrow marks on DE and BC.
2. `% B5` answer figure: same fix. Vertex letters only, DE parallel to BC with arrow marks. No side labels.
3. Figure in the example "Prove that triangle PQR is isosceles" (Example 3.3): the angle mark at S is drawn as a full circle.
   Draw one small single arc for angle PST (between rays S->P and S->T) and one matching small single arc for angle PRQ at R
   (between rays R->P and R->Q). Use \pic[draw,angle radius=7pt] {angle=T--S--P}; and {angle=Q--R--P}; (check orientation so the arc is inside the angle).

body2.tex
4. `% F5.4`: the label "9 cm" is on side AB. It must be on segment AD, which lies along AC from A to D. Put "$9$ cm" beside AD
   (on the outer side of AC, near the middle of AD) and put "$?$" beside AB. Keep "25 cm" for AC (place it beside DC part, clearly on AC).
5. `% E1`, `% E3`, `% E5`: redraw each triangle as a complete solid triangle (no dotted or missing sides), computed from its three
   side lengths with the law of cosines so the shape is true, scaled to fit. Label each side length outside its side, and the vertex
   letters where the text names them (E3: A,B,C with AB=4, BC=6, CA=8 and P,Q,R with PQ=12, QR=9, RP=6; E5: X,Y,Z with XY=3, YZ=5,
   ZX=7 and the 120 degree angle at Y; L,M,N with LM=10, MN=6, NL=14 and "?" at M). E1: three rows (a), (b), (c), each a pair of
   complete triangles with their side lengths (a) 3,4,6 and 6,8,12; (b) 5,6,8 and 10,12,15; (c) 2,3,4 and 6,9,12.
6. `% F2`: remove the word "included" (it overlaps the angle label). Keep the 50 degree mark at A. Add a small double arc at B, unlabelled.
   Label the vertices A, B, C and the sides AB = 6, BC = 9.
7. `% F5`: the side labels are wrong. Triangle ABC with D on AB and E on AC. Label AD = 3 and DB = 6 along AB, AE = 4 and EC = 8 along AC.
   Show vertex letters A, B, C, D, E. Draw DE.

body3.tex
8. `% F9.5` (question figure) and `% H8` (answer figure): use these coordinates (scale 0.6):
   B=(-2,0), C=(2,0), A=(0,6), E=(-4,0), D=(0,0), F=(1.4,1.8). Draw triangle ABC, AD dashed with a right-angle mark at D,
   the base line from E to C, segment EF with a right-angle mark at F (\ramark{F}{E}{C}). In H8 also mark angle ABD and angle ECF
   (that is angle at C between C->E and C->A) with matching single arcs.
9. `% R2`: remove the large circle drawn at C. Mark angle AEC (at E, between E->A and E->C) and angle ACE (at C, between C->A and C->E)
   with matching small single arcs.
10. `% H4`: the labels overlap. Spread them: "5.4 m" left of the lamp post, "1.8 m" left of the man's line, "4 m" below BD,
    "$s$" or "?" below DE. Vertex letters A (lamp top), B (base), C (man's head), D (man's feet), E (shadow tip).

Then compile test1.tex, test2.tex and test3.tex (pdflatex -interaction=nonstopmode, twice each). Fix any error. Report DONE.
