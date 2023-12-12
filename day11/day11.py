import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file = "example.txt"
file = "input.txt"
lines = aoc.loadlines(file=file, discard_empty_lines=True)

# expand
expand_column = [1 for _ in range(0, len(lines[0]))]
expanded = lines.copy()
added = 0
for y in range(0, len(lines)):
  if '#' not in lines[y]:
    expanded.insert(added + y, lines[y])
    added = added + 1
  for x in range(0, len(lines[y])):
    expand_column[x] = 0 if lines[y][x] == '#' else expand_column[x]

offset = 0
for i in range(0, len(expand_column)):
  if expand_column[i]:
    for y in  range(0, len(expanded)):
      row = list(expanded[y])
      row.insert(i+offset, '.')
      expanded[y] = "".join(row)
    offset = offset + 1

galaxies = []
for y in range(0, len(expanded)):
  for x in range(0, len(expanded[y])):
    if expanded[y][x] == '#':
      galaxies.append({"X":x,"Y":y})

part1 = 0
for start in range(0, len(galaxies)-1):
  for end in range(start+1, len(galaxies)):
    x = abs( (galaxies[end]['X'])-(galaxies[start]['X']) )
    y = abs( (galaxies[end]['Y'])-(galaxies[start]['Y']) )
    part1 = part1 + y + x

aoc.result(part1) # 3304176 too low
