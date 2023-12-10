import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file="example.txt"
file="input.txt"

lines = [[int(val) for val in line.strip().split(' ')] for line in aoc.loadlines(file=file, discard_empty_lines=True)]

parts = [0,0]

# part 1
for line in lines:
  depth = 0
  lasts = []
  while(len([1 for e in line if e != 0]) != 0):
    lasts.append(line[-1])
    depth = depth + 1
    diffs = []
    for i in range(0, len(line)-1):
      diffs.append(line[i+1] - line[i])
    line = diffs
  parts[0] += sum(lasts)

# part 2
for line in lines:
  depth = 0
  firsts = []
  while(len([1 for e in line if e != 0]) != 0):
    firsts.append(line[0])
    depth = depth + 1
    diffs = []
    for i in range(0, len(line)-1):
      diffs.append(line[i+1] - line[i])
    line = diffs

  prev = 0
  for i in range(len(firsts)-1, -1, -1):
    prev = firsts[i] - prev

  parts[1] += prev

aoc.result(parts[0], parts[1])
