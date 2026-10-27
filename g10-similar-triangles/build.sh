#!/bin/bash
# build.sh: assemble class 2 (student) and class 2 fc (teacher) from src/ and compile
cd "$(dirname "$0")"
for mode in false true; do
  name="class 2"; [ $mode = true ] && name="class 2 fc"
  { echo "\\newif\\ifteacher\\teacher$mode"; cat src/preamble.tex; echo '\begin{document}'; cat src/body1.tex src/body2.tex src/body3.tex; echo '\end{document}'; } > "build/$name.tex"
  (cd build && pdflatex -interaction=nonstopmode "$name.tex" >/dev/null && pdflatex -interaction=nonstopmode "$name.tex" > /dev/null)
  grep -c '^!' "build/$name.log" | sed "s/^/$name errors: /"
  grep -E 'Overfull' "build/$name.log" | sed "s/^/$name: /" | head -20
  pdfinfo "build/$name.pdf" | grep Pages
done
