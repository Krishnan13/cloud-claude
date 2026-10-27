import re

BS = chr(92)
NEED = BS + 'Needspace{16' + BS + 'baselineskip}'
for f in ['body1.tex', 'body2.tex', 'body3.tex']:
    lines = open(f, encoding='utf-8').read().split('\n')
    out = []
    n = 0
    for i, line in enumerate(lines):
        if line.lstrip().startswith(BS + 'item') and NEED not in line:
            # does a centred figure follow before the next item or the end of the list?
            for nxt in lines[i + 1:i + 6]:
                s = nxt.lstrip()
                if s.startswith(BS + 'item') or s.startswith(BS + 'end{exercise}'):
                    break
                if s.startswith(BS + 'begin{center}') or s.startswith('% '):
                    line = line.replace(BS + 'item', NEED + BS + 'item', 1)
                    n += 1
                    break
        out.append(line)
    open(f, 'w', encoding='utf-8').write('\n'.join(out))
    print(f, n)
