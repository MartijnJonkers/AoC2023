import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#grid = aoc.add_perimeter('.', aoc.loadlines(discard_empty_lines=True))
grid = [list('.' + line + '.') for line in aoc.loadlines(discard_empty_lines=True)]
grid.insert(0, list("." * len(grid[0])))
grid.append(list("." * len(grid[0])))

start_y,start_x = 25 +1,77+1             # starting pos
prev_y,prev_x = start_y,start_x     # starting pos
curr_y,curr_x = start_y-1,start_x   # first step
steps = 0

c = grid[start_y][start_x]
while curr_y != start_y or curr_x != start_x:
  steps = steps +1
  c = grid[curr_y][curr_x]
  curr_pipe = grid[curr_y][curr_x]
  grid[curr_y][curr_x] = '*'

  # determine step to take
  if ( curr_pipe in ['|', 'J', 'L'] and grid[curr_y-1][curr_x] in ['|','7','F','S'] ):
    curr_y = curr_y - 1
  elif ( curr_pipe in ['-', 'L', 'F'] and grid[curr_y][curr_x+1] in ['-','7','J','S'] ):
    curr_x = curr_x + 1
  elif ( curr_pipe in ['|', 'F', '7'] and grid[curr_y+1][curr_x] in ['|','L','J','S'] ):
    curr_y = curr_y + 1
  elif ( curr_pipe in ['-', '7', 'J'] and grid[curr_y][curr_x-1] in ['-','L','F','S'] ):
    curr_x = curr_x - 1

part1 = (steps/2) + 1
aoc.result(part1)
