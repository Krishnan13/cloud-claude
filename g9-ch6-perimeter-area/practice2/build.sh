#!/bin/bash
# build.sh: assemble practice questions 2 (student) and practice questions 2 fc (teacher) from src/ and compile
cd "$(dirname "$0")"; mkdir -p build
for mode in false true; do
  name="practice questions 2"; [ $mode = true ] && name="practice questions 2 fc"
  { echo "\\newif\\ifteacher\\teacher$mode"; cat src/preamble.tex; echo '\begin{document}'; cat src/head.tex src/part1.tex src/part2.tex src/part3.tex; echo '\end{document}'; } > "build/$name.tex"
  (cd build && pdflatex -interaction=nonstopmode "$name.tex" >/dev/null; pdflatex -interaction=nonstopmode "$name.tex" > /dev/null)
  grep -c '^!' "build/$name.log" | sed "s/^/$name errors: /"
  grep -A3 '^!' "build/$name.log" | head -20
  grep -E 'Overfull' "build/$name.log" | sed "s/^/$name: /" | head -10
  pdfinfo "build/$name.pdf" | grep Pages
done
