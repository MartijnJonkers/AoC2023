import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file = "example.txt"
file = "input.txt"
blocks = [[l for l in block.split('\n') if len(l.strip())>0] for block in aoc.read(file=file).split('\n\n')]

def run_block(block):
  if '###...#...#.#..' in block[0]:
  #if '#' in block[0]:
    pass
  for factor in [100,1]:
    for y in range(1, len(block)):
      l = min(len(block) - y, y)
      above = block[y-l: y]
      below = block[y: y+l]
      above.reverse()
      # for i in range(2, len(above)):
      #   if( "".join(above[0:i]) == "".join(below[0:i]) ):
      #     return (y+1) * factor
      
      if( "".join(above) == "".join(below) ):
        return y * factor

    # do it again but now rotated 90 degrees
    org = block.copy()
    block = list(zip(*block[::-1]))
    block = ["".join(line) for line in block]
  #return 0

part1 = 0
for block in blocks:
  part1 = part1 + run_block(block.copy())

aoc.result(part1)
