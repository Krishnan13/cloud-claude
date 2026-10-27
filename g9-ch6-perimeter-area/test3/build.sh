#!/bin/bash
# build.sh: assemble test 3 (student) and test 3 fc (teacher) from src/ and compile
cd "$(dirname "$0")"; mkdir -p build
for mode in false true; do
  name="test 3"; [ $mode = true ] && name="test 3 fc"
  { echo "\\newif\\ifteacher\\teacher$mode"; sed '/input{..\/src\/figs.tex}/d' src/preamble.tex; echo '\makeatletter'; cat src/figs.tex; echo '\makeatother'; echo '\begin{document}'; cat src/body.tex; echo '\end{document}'; } > "build/$name.tex"
  (cd build && pdflatex -interaction=nonstopmode "$name.tex" >/dev/null; pdflatex -interaction=nonstopmode "$name.tex" > /dev/null)
  grep -c '^!' "build/$name.log" | sed "s/^/$name errors: /"
  grep -A3 '^!' "build/$name.log" | head -20
  grep -E 'Overfull' "build/$name.log" | sed "s/^/$name: /" | head -10
  pdfinfo "build/$name.pdf" | grep Pages
done
