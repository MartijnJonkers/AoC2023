import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file="example.txt"
file="input.txt"

lines = aoc.loadlines(file=file, discard_empty_lines=True)
instructions = lines[0]

nodes = {}
for node in lines[1:]:
  parts = node.strip().split(' ')
  nodes[parts[0]] = {
    'name': parts[0],
    'L': parts[2][1:4],
    'R': parts[3][:3],
  }

part1 = 0
current_node = nodes['AAA']
loop = 0
while part1 == 0:
  for step in range(0, len(instructions)):
    current_node = nodes[current_node[instructions[step]]]
    if(current_node['name'] == 'ZZZ'):
      part1 = step + 1 + (loop * len(instructions))
      break
  loop = loop + 1

aoc.result(part1)
