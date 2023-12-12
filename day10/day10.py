import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

grid = [list('.' + line + '.') for line in aoc.loadlines(discard_empty_lines=True)]
grid.insert(0, list("." * len(grid[0])))
grid.append(list("." * len(grid[0])))

start_y,start_x = 25+1,77+1         # starting pos
curr_y,curr_x = start_y-1,start_x   # first step
steps = 0

dir = 'up'
line_chars = [{'Y':start_y,'X':start_x,'Dir':dir,'Char':'|'}]# S = '|'
while curr_y != start_y or curr_x != start_x:

  # count steps (part1)
  steps = steps +1

  # get current line char and replace in grid, so it is not handled for future checks
  curr_pipe = grid[curr_y][curr_x]
  grid[curr_y][curr_x] = '*'
  
  # store info for part 2
  line_chars.append({'Y':curr_y,'X':curr_x,'Dir':dir, 'Char':curr_pipe})

  # determine step to take (direction for part 2)
  if   ( curr_pipe in ['|', 'J', 'L'] and grid[curr_y-1][curr_x] in ['|','7','F','S'] ):
    curr_y = curr_y - 1
    dir = 'up'
  elif ( curr_pipe in ['-', 'L', 'F'] and grid[curr_y][curr_x+1] in ['-','7','J','S'] ):
    curr_x = curr_x + 1
    dir = 'right'
  elif ( curr_pipe in ['|', 'F', '7'] and grid[curr_y+1][curr_x] in ['|','L','J','S'] ):
    curr_y = curr_y + 1
    dir = 'down'
  elif ( curr_pipe in ['-', '7', 'J'] and grid[curr_y][curr_x-1] in ['-','L','F','S'] ):
    curr_x = curr_x - 1
    dir = 'left'

# furthest away is half the length of the line (rounded up)
part1 = int((steps/2) + 0.5)

# replace all none loop chars with space
for y in range(0, len(grid)):
  for x in range(0, len(grid[y])):
    if grid[y][x] != '*' : grid[y][x] = ' '

# go over all chars of the line and mark inside and outside of the line.
for pos in line_chars:
  grid[pos['Y']][pos['X']] = '.' # draw line as '.'

  # '+' = left side of line: is outside of loop
  # '$' = right side of line: is inside of loop
  # only replace none line chars

  # entering current line position from the bottom, so going 'up'
  if pos['Dir'] == 'up' and pos['Char'] == '|':
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '+'  # left center (outside)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '$'  # right center (inside)
  if pos['Dir'] == 'up' and pos['Char'] == '7':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '$'  # left top (inside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '$'  # center top (inside)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '$'  # right top (inside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = ' '  # left center (line)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '$'  # right center (inside)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '+'  # left bottom (outside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = ' '  # center bottom (line)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '$'  # right bottom (inside)
  if pos['Dir'] == 'up' and pos['Char'] == 'F':   
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '+'  # left top (outside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '+'  # center top (outside)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '+'  # right top (outside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '+'  # left center (outside)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = ' '  # right center (line)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '+'  # left bottom (outside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = ' '  # center bottom (line)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '$'  # right bottom (inside)

  # entering current line position from the left, so going 'right'
  if pos['Dir'] == 'right' and pos['Char'] == '-':
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '+'  # center top (outside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '$'  # center bottom (inside)
  if pos['Dir'] == 'right' and pos['Char'] == '7':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '+'  # left top (outside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '+'  # center top (outside)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '+'  # right top (outside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = ' '  # left center (line)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '+'  # right center (outside)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '$'  # left bottom (inside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = ' '  # center bottom (line)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '+'  # right bottom (outside)
  if pos['Dir'] == 'right' and pos['Char'] == 'J':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '+'  # left top (outside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = ' '  # center top (line)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '$'  # right top (inside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = ' '  # left center (line)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '$'  # right center (inside)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '$'  # left bottom (inside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '$'  # center bottom (inside)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '$'  # right bottom (inside)

  # entering current line position from the top, so going 'down'
  if pos['Dir'] == 'down' and pos['Char'] == '|':
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '$'  # left center (inside)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '+'  # right cener (outside)
  if pos['Dir'] == 'down' and pos['Char'] == 'L':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '$'  # left top (inside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = ' '  # center top (line)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '+'  # right top (outside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '$'  # left center (inside)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = ' '  # right center (line)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '$'  # left bottom (inside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '$'  # center bottom (inside)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '$'  # right bottom (inside)
  if pos['Dir'] == 'down' and pos['Char'] == 'J':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '$'  # left top (inside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = ' '  # center top (line)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '+'  # right top (outside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = ' '  # left center (line)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = '+'  # right center (outside)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '+'  # left bottom (outside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '+'  # center bottom (outside)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '+'  # right bottom (outside)

  # entering current line position from the right, so going 'left'
  if pos['Dir'] == 'left' and pos['Char'] == '-':
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '$'  # center top (inside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '+'  # center bottom (outside)
  if pos['Dir'] == 'left' and pos['Char'] == 'L':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '+'  # left top (outside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = ' '  # center top (line)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '$'  # right top (inside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '+'  # left center (outside)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = ' '  # right center (line)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '+'  # left bottom (outside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = '+'  # center bottom (outside)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '+'  # right bottom (outside)
  if pos['Dir'] == 'left' and pos['Char'] == 'F':
    if grid[pos['Y'] - 1][pos['X'] - 1] == ' ':     grid[pos['Y'] - 1][pos['X'] - 1] = '$'  # left top (inside)
    if grid[pos['Y'] - 1][pos['X']    ] == ' ':     grid[pos['Y'] - 1][pos['X']    ] = '$'  # center top (inside)
    if grid[pos['Y'] - 1][pos['X'] + 1] == ' ':     grid[pos['Y'] - 1][pos['X'] + 1] = '$'  # right top (inside)
    if grid[pos['Y']    ][pos['X'] - 1] == ' ':     grid[pos['Y']    ][pos['X'] - 1] = '$'  # left center (inside)
    if grid[pos['Y']    ][pos['X']    ] == ' ':     grid[pos['Y']    ][pos['X']    ] = ' '  # center center (line)
    if grid[pos['Y']    ][pos['X'] + 1] == ' ':     grid[pos['Y']    ][pos['X'] + 1] = ' '  # right center (line)
    if grid[pos['Y'] + 1][pos['X'] - 1] == ' ':     grid[pos['Y'] + 1][pos['X'] - 1] = '$'  # left bottom (inside)
    if grid[pos['Y'] + 1][pos['X']    ] == ' ':     grid[pos['Y'] + 1][pos['X']    ] = ' '  # center bottom (line)
    if grid[pos['Y'] + 1][pos['X'] + 1] == ' ':     grid[pos['Y'] + 1][pos['X'] + 1] = '+'  # right bottom (outside)


# '$' chars are on the inside or the loop
# color in all '$' circles and count them
part2 = 0
for y in range(0,len(grid)):
  for x in range(0, len(grid[y])-1):
    if( grid[y][x] == '$' and grid[y][x+1] == ' ' ):
      grid[y][x+1] = '$'
    if( grid[y][x] == '$' ):
      part2 = part2 + 1

# write current grid to file for visualisation
f = open("day10/output.txt", "w")
for line in grid:
  f.write("".join(line) + '\n')
f.close()

aoc.result(part1, part2)
