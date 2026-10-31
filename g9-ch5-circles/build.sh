# usage: bash build.sh N   -> builds "circles class N" and "circles class N fc"
N=$1
for t in false true; do
  if [ $t = true ]; then n="circles class $N fc"; else n="circles class $N"; fi
  { echo "\newif\ifteacher\teacher$t"; cat preamble.tex; echo '\begin{document}'; cat class$N-body.tex; echo '\end{document}'; } > "$n.tex"
  pdflatex -interaction=nonstopmode -halt-on-error "$n.tex" > /dev/null; pdflatex -interaction=nonstopmode "$n.tex" > /dev/null
  echo "== $n"; grep -E "^!|Overfull|Undefined|Missing" "$n.log" | sort | uniq -c | head
done
