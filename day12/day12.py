import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

file = "example.txt"
#file = "input.txt"
lines = aoc.loadlines(file=file, discard_empty_lines=True)

def check(line, groups, matches):
  if '?' not in line:
    g = []
    for j in range(0, len(line)-1):
      if( line[j] == '.' and line[j+1] == '#' ):
        g.append(0)
      elif( line[j] == '#' ):
        g[-1] = g[-1] + 1
    if( len(g) != len(groups) ):
      return matches
    for j in range(0, len(g)):
      if( g[j] != groups[j] ):
        return matches
    return matches + 1
  else :
    for i in range(0, len(line)):
      if line[i] == '?':
        for c in ['#', '.']:
          line[i] = c
          matches = check(line, groups, matches)
        line[i] = '?'
        break
    return matches

lines = [[num.split(',') for num in line.split(' ')] for line in lines]


def run_part():
  matches = 0
  c = 0
  for line in lines:

    line[0][0] = "." + line[0][0] + "."
    matches = check(list(line[0][0]), [int(n) for n in line[1]] , matches)
    c = c+1
    print( c, '/', len(lines), '-', matches )

  aoc.result(matches)

# part1
run_part()

for line in [lines[1]]:
  l = line[0][0]
  g = line[1].copy()
  for i in range(0,4):
    line[0][0] = line[0][0] + '?' + l 
    line[1].extend(g)

# part2
run_part()
