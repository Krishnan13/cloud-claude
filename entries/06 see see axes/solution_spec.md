# Spec: SEE + SEE = AXES — problem and solution (LaTeX + PDF)

Create `solution.tex` in this folder and compile it with `pdflatex -interaction=nonstopmode solution.tex`
(run twice) to `solution.pdf`. Then delete solution.aux, solution.log, solution.out.
Zero errors, zero overfull boxes.

Preamble: copy EXACTLY from `C:/Users/Krishnanvp/.claude/latex-style/template.tex`
(article 11pt a4paper, geometry margin=2cm, amsmath, amssymb, tikz, pgfplots compat 1.18, booktabs,
enumitem, parskip, hyperref with pdfauthor={Krishnan}), with pdftitle={SEE + SEE = AXES}.

Title (template style): `\begin{center}{\Large\bfseries SEE + SEE = AXES}\end{center}`

Style rules:
- Unnumbered headings: `\section*{...}`.
- Short sentences. Each step ends with its key rule as one `\textbf{...}` paragraph.
- Letters of the puzzle are always in maths italics: $S$, $E$, $A$, $X$. Words SEE / AXES as $SEE$, $AXES$.
- Column sums are typeset with this exact macro pattern (define once in the preamble):
  ```
  \newcommand{\colsum}[3]{%
  \begin{center}\large
  \renewcommand{\arraystretch}{1.3}
  \begin{tabular}{c@{\hspace{1.2em}}c@{\hspace{1.2em}}c@{\hspace{1.2em}}c@{\hspace{1.2em}}c}
  #1\\
  #2\\ \midrule
  #3
  \end{tabular}
  \end{center}}
  ```
  Each argument is one row of 5 cells: a sign cell, then thousands, hundreds, tens, units.
- Do NOT add any section, sentence, example, figure or decoration not listed here.

---------------------------------------------------------------------------
## Section: Problem   (`\section*{Problem}`)

Text:
In the addition sum below, each letter stands for a different non-zero digit. What digit does $X$ stand for?

Column sum: `\colsum{ & & $S$ & $E$ & $E$}{$+$ & & $S$ & $E$ & $E$}{ & $A$ & $X$ & $E$ & $S$}`

## Section: Solution   (`\section*{Solution}`)

Text:
Work through the columns from right to left, as in ordinary addition. When a column adds up to 10 or more,
write its last digit (the \emph{units digit}) and pass 1 to the next column on the left. That 1 is the
\emph{carry}. Adding two numbers, the carry is always 0 or 1.

Then four steps, each a paragraph starting with a bold run-in label, e.g. `\textbf{Step 1: the digit $A$.}`
followed by the text on the same line.

**Step 1: the digit $A$.**
Text: Both rows are the same number, so the sum is $2 \times SEE$. Since $SEE \le 999$, we get
$2 \times SEE \le 1998$, which is less than 2000.
Bold rule: **The 4-digit answer starts with 1, so $A = 1$.**

**Step 2: the digit $E$ (tens column).**
Text: In the tens column, $E + E + \text{carry}$ has units digit $E$. Take one $E$ away:
$E + \text{carry}$ has units digit 0. But $E + \text{carry}$ lies between 1 and 10, so it must equal 10.
With carry 0 we would need $E = 10$, which is not a digit. So the carry is 1 and $E = 9$.
Bold rule: **$E = 9$, and the units column must send a carry of 1.**

**Step 3: the digit $S$ (units column).**
Text: $E + E = 9 + 9 = 18$. Write 8, carry 1 --- exactly the carry Step 2 needed.
Bold rule: **$S = 8$.**

**Step 4: the digit $X$ (hundreds column).**
Text: The tens column is $9 + 9 + 1 = 19$: write 9, carry 1. The hundreds column is
$S + S + 1 = 8 + 8 + 1 = 17$: write 7, carry 1. That last carry is the leading 1, which is $A$.
Bold rule: **$X = 7$.**

## Section: Check   (`\section*{Check}`)

Column sum: `\colsum{ & & 8 & 9 & 9}{$+$ & & 8 & 9 & 9}{ & 1 & 7 & 9 & 8}`

Text: $899 + 899 = 1798$. The digits $S = 8$, $E = 9$, $A = 1$, $X = 7$ are all different and non-zero.

Bold line (centred, `\begin{center}\textbf{Answer: $X = 7$}\end{center}`).
