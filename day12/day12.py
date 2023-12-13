import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

file = "example.txt"
#file = "input.txt"
lines = aoc.loadlines(file=file, discard_empty_lines=True)

lines = [[num.split(',') for num in line.split(' ')] for line in lines]
for i in range(0, len(lines)):
  record = [n for n in lines[i][0][0].split('.') if n != '']
  lens = [int(n) for n in lines[i][1]]
  groups = [("#" * int(n)) for n in lines[i][1]]
  min_group_len = sum([len(g) for g in groups]) + len(groups) - 1

  record = list(".".join(record))
  record.insert(0, '.')
  record.append('.')
  #record = "".join(record)
  
  for g in range(len(groups)-1, -1, -1):
    for offset in range(0, len(record) - min_group_len):

      pass

  pass



aoc.result()
