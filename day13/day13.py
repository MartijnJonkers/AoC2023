import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

part = 2
blocks = [block.split('\n') for block in aoc.read().strip().split('\n\n')]

def run_block(block):
  for factor in [100,1]:                          # first time top down, second time left right
    for y in range(1, len(block)):                  # go over all rows
      l = min(len(block) - y, y)                      # determin shortest steps to top or bottom
      above = block[y-l: y][::-1]                       # get rows above a line, reversed
      below = block[y: y+l]                             # get rows below a line
      if part == 1:                                     # part 1:
        if( above == below):                              # check above and below are the same
          return y * factor                                 # they are the same
      elif part == 2:                                   # part 2:
        ab = zip("".join(above), "".join(below))          # combine
        diffs = [1 for a,b in ab if a != b]               # get the diffs at index
        if( len(diffs) == 1 ):                            # check 1 diff
          return y * factor                                 # exactly 1 diff found, so must be smutge
    block = ["".join(line) for line in list(zip(*block[::-1]))] # rotate the block 90 degrees and run again

result = 0
for block in blocks:
  result = result + run_block(block)   # compute result by adding up all results
aoc.result(result)
