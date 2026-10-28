#!/bin/bash
# check.sh N: compile only src/partN.tex (both copies) into check_N/ for a quick test
cd "$(dirname "$0")"; n=$1; mkdir -p check_$n
for mode in false true; do
  { echo "\\newif\\ifteacher\\teacher$mode"; cat src/preamble.tex; echo '\begin{document}'; cat src/part$n.tex; echo '\end{document}'; } > check_$n/t$mode.tex
  (cd check_$n && pdflatex -interaction=nonstopmode t$mode.tex >/dev/null)
  echo "teacher=$mode errors: $(grep -c '^!' check_$n/t$mode.log)"; grep -A3 '^!' check_$n/t$mode.log | head -15
  grep Overfull check_$n/t$mode.log | head -5
done
