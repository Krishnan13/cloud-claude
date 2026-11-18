# Spec: Eight balls in a row — problem and solution (LaTeX + PDF)

Create `5.tex` in this folder and compile it with `pdflatex -interaction=nonstopmode 5.tex`
(run twice) to `5.pdf`. Then delete 5.aux, 5.log, 5.out. Zero errors, zero overfull boxes.

Preamble: copy EXACTLY from `4.tex` in this folder, but REMOVE the `\colsum` macro definition
(not used here) and set pdftitle={Eight Balls in a Row}. Keep pdfauthor={Krishnan}.

Title (same style as 4.tex): `\begin{center}{\Large\bfseries Eight Balls in a Row}\end{center}`

Style rules (same as 4.tex):
- Unnumbered headings: `\section*{...}`.
- Short sentences. Each step is a paragraph starting with a bold run-in label, e.g.
  `\textbf{\boldmath Step 1: slide the group.}` followed by text on the same line.
- Each step ends with its key rule as one paragraph `\textbf{\boldmath ...}` (the \boldmath is required,
  so maths inside bold text is bold too). Same for the step labels and the final answer line.
- Tables: `\begin{center}\small\renewcommand{\arraystretch}{1.6}\begin{tabular}{c|cccccccc}
  \toprule ... \bottomrule\end{tabular}\end{center}`, first column is the row name.
- Do NOT add any section, sentence, example, figure or decoration not listed here.

---------------------------------------------------------------------------
## Section: Problem   (`\section*{Problem}`)

Text:
Eight balls stand in a row:

Table (rows "Position" and "Ball"):
Position: 1, 2, 3, 4, 5, 6, 7, 8
Ball: cricket, football, volleyball, tennis, golf, baseball, rugby, bowling

Text:
The volleyball has value 100, and the values of any three consecutive balls add up to 600.
What is the value of cricket ball $+$ bowling ball?

## Section: Solution   (`\section*{Solution}`)

Text:
Name each ball by its position: $b_1$ is the value of ball 1, $b_2$ the value of ball 2, and so on.
Then $b_3 = 100$, and we want $b_1 + b_8$.
Balls are \emph{consecutive} when they stand next to each other with no gap. There are six groups of three
consecutive balls: 1, 2, 3;\ 2, 3, 4;\ 3, 4, 5;\ 4, 5, 6;\ 5, 6, 7;\ 6, 7, 8. Each group adds up to 600.

**Step 1: slide the group.**
Text: Compare the first two groups:
Display (exactly this, so that $b_2$ and $b_3$ line up):
```
\[
\begin{array}{ccccccccc}
b_1 & + & b_2 & + & b_3 &   &     & = & 600\\
    &   & b_2 & + & b_3 & + & b_4 & = & 600
\end{array}
\]
```
Text: Both totals are 600 and both contain $b_2 + b_3$, so $b_1 = b_4$.
Bold rule: **When the group slides one place to the right, the ball that leaves and the ball that joins have equal values.**

**Step 2: the row repeats.**
Text: The ball that leaves and the ball that joins are always 3 places apart. So
$b_1 = b_4 = b_7$, $b_2 = b_5 = b_8$ and $b_3 = b_6$, and the row is the first three values repeating:

Table (rows "Position" and "Value"):
Position: 1, 2, 3, 4, 5, 6, 7, 8
Value: $b_1$, $b_2$, $b_3$, $b_1$, $b_2$, $b_3$, $b_1$, $b_2$

Bold rule: **Balls 3 places apart have equal values, so $b_8 = b_2$.**

**Step 3: the answer.**
Text: Using the first group and $b_3 = 100$:
Display: `\[ b_1 + b_8 = b_1 + b_2 = 600 - b_3 = 600 - 100 = 500. \]`

Final line (centred): `\begin{center}\textbf{\boldmath Answer: cricket ball $+$ bowling ball $= 500$}\end{center}`
