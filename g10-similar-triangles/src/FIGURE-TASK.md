# Figure task (for one body file)

You edit ONE file only: the body file named in the command. Do not edit or create any other file
except the matching testN.pdf/aux/log produced by compiling. Do not change any text, maths, question or answer.

Replace every figure placeholder in that file with TikZ:

1. `\figph{ID: description}` -> a full block
   `\begin{center}\begin{tikzpicture}[scale=0.85, every node/.style={font=\small}] ... \end{tikzpicture}\end{center}`
2. `\exfig{ID: description}` -> `\exfig{ <tikz commands only> }` (the macro already opens the tikzpicture).
3. `\ansfig{ID: description}` -> `\ansfig{ <tikz commands only> }` (the macro already opens the tikzpicture).
   Keep the ID as a TeX comment on the line above, e.g. `% B3`.

House style (strict):
- Black-and-white print. No colour words. Main lines `[thick,accent]` (accent is a dark slate already defined).
  Inside `\ansfig` use plain `thick` lines (they inherit the grey colour). Soft fills use `panel` (already defined), e.g. `\fill[panel]`.
- Draw to true proportions: if lengths are given, choose coordinates so the drawn lengths are in those ratios
  (use a common scale, e.g. 1 unit = 1 cm scaled down, and compute points with calc, e.g. `($(A)!0.4!(B)$)`).
  Parallel lines must really be parallel: place D and E with the SAME fraction along AB and AC.
- Mark parallel segments with small arrow marks or say nothing; never draw a dashed line with a solid line on top.
  Dashed lines: `[dashed]`.
- Right angles: use the macro `\ramark{V}{P}{Q}` (draws a right-angle mark at vertex V between rays V->P and V->Q).
- Angles: `\pic[draw,angle radius=8pt] {angle=B--A--C};` (libraries angles, quotes, calc are loaded). Equal angles get
  matching marks (single arc, double arc).
- Labels: vertex letters in maths mode, placed outside the figure (above/below left/right), not touching lines.
  Lengths with units where the text gives units, e.g. `$6$ cm`; unknown marked `$?$`.
  Algebraic lengths like `$x+2$` as given.
- Keep each figure compact: width at most about 9 cm after scaling. Two triangles side by side are fine.

When done, compile from this folder:
`pdflatex -interaction=nonstopmode testN.tex` (N = 1, 2 or 3 matching your body file) twice.
Fix every error until it compiles with no errors. Report "DONE" and the number of figures replaced.
