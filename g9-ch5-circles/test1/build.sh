# usage: bash build.sh  -> builds "circles test 1" and "circles test 1 fc"
cd "$(dirname "$0")"
for t in false true; do
  if [ $t = true ]; then n="circles test 1 fc"; else n="circles test 1"; fi
  { echo "\newif\ifteacher\teacher$t"; cat preamble.tex; echo '\begin{document}'; cat header.tex body1.tex body2.tex; echo '\end{document}'; } > "$n.tex"
  pdflatex -interaction=nonstopmode -halt-on-error "$n.tex" > /dev/null; pdflatex -interaction=nonstopmode "$n.tex" > /dev/null
  echo "== $n: $(pdfinfo "$n.pdf" 2>/dev/null | grep Pages)"; grep -E "^!|Overfull|Undefined|Missing" "$n.log" | sort | uniq -c | head
done
