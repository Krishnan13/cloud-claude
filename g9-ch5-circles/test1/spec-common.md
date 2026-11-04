# LaTeX job: Grade 9 circles test (body only)

Output ONLY LaTeX body code (no \documentclass, no preamble, no \begin{document}). Do not create files. No markdown fences.

## Macros already defined in the preamble (use exactly these)
- `\sect{Section A (1 mark each)}` section heading.
- `\ques` starts a numbered question (auto-numbered). Put `\Needspace{8\baselineskip}` before each `\ques`.
- `\marks{2}` puts [2] at the right end of a line. Put it at the end of the question's last sentence, or at the end of each part when parts carry marks.
- `\pc{a}{text}` a part (a), (b), ... of a question.
- `\mcqtwo{A}{B}{C}{D}` four MCQ options in a 2x2 grid.
- `\aritem{Assertion (A)}{text}` and `\aritem{Reason (R)}{text}` for assertion-reason.
- `\begin{answerblock} ... \end{answerblock}` solution, printed only in the teacher copy. Put it right after each question.
- `\Given`, `\Tofind`, `\Toprove`, `\Constr`, `\Ans`, `\Hp` (prints "Hence proved.") bold labels. `\tr` prints a triangle sign. `\nl` = line break with small space.
- Inside answerblock write steps as `\begin{enumerate}[label=\arabic*.,leftmargin=1.6em,itemsep=0pt,topsep=2pt] \item ... \end{enumerate}`. Each step gives the reason in brackets.
- Use `\dfrac` for fractions, `^\circ` for degrees, `$5$~cm` for lengths.

## Figures (TikZ)
- Style: `\begin{tikzpicture}[fig,every node/.style={font=\scriptsize}]`. Lines dark grey (fig style), fills `figfill`. Centre O as a small filled dot `\fill[figline] (O) circle (0.035);`.
- Student figures: `\begin{center} ... \end{center}` after the question text, radius about 1.4 to 1.7 cm.
- Solution figures (inside answerblock): small, radius about 0.9 to 1.1 cm, placed on the RIGHT of the steps using
  `\begin{minipage}[t]{0.66\linewidth} steps... \end{minipage}\hfill\begin{minipage}[t]{0.3\linewidth}\centering tikz \end{minipage}`.
  Every question gets a small solution figure, with the given measurements marked.
- Compute every point with real trig/coordinates so the figure is geometrically correct (chords at the correct distance from O, right angles really right). Mark right angles with a small square. Equal segments with small tick marks.
- Labels must never touch or cross lines: place letters outside the circle (use anchors like above, below left, etc.) and lengths beside segments, not on them.
- Do not put numbers on figures that the student must find.
