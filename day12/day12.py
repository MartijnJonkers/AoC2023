import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

file = "example.txt"
#file = "input.txt"
lines = aoc.loadlines(file=file, discard_empty_lines=True)

lines = [[num.split(',') for num in line.split(' ')] for line in lines]
for i in range(0, len(lines)):
  record = [n for n in lines[i][0][0].split('.') if n != '']
  groups = [int(n) for n in lines[i][1]]

  



aoc.result()
