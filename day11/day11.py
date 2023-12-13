import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file = "example.txt"
file = "input.txt"
lines = aoc.loadlines(file=file, discard_empty_lines=True)

#EXPANSION = 1         # part 1
EXPANSION = 1000000-1 # part 2

# create lists to keep track of expanded rows and columns (assume all expanded at first)
expand_column = [True for _ in range(0, len(lines[0]))]
expand_row = [True for _ in range(0, len(lines))]

# go over all data and determine the expansion per row and column
for y in range(0, len(lines)):
  for x in range(0, len(lines[y])):
    if lines[y][x] == '#':
      expand_row[y] = False 
      expand_column[x] = False

offset = {'X':0,'Y':0}
result = 0
galaxies = []
for y in range(0, len(lines)):
  
  if expand_row[y]:
    offset['Y'] = offset['Y'] + EXPANSION     # determine current row offset

  offset['X'] = 0
  for x in range(0, len(lines[y])):

    if expand_column[x]:
      offset['X'] = offset['X'] + EXPANSION   # determine current column offset
    
    # is it a new galaxy?
    if lines[y][x] == '#':
      new = {"X":x+offset['X'],"Y":y+offset['Y']}

      # compute length to al already known galaxies
      for old in galaxies:
        result = result + abs( old['X']-new['X'] ) +  abs( old['Y']-new['Y'] )

      # add new one to the list
      galaxies.append(new)

aoc.result(result)
