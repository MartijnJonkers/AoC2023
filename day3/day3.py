import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

# get lines and add a '.' perimeter
lines = ['.' + line + '.' for line in aoc.loadlines(discard_empty_lines=True)]
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

possible_gears = {}
part1_sum = 0
for y in range(1, len(lines)-1):                        # go over all rows
  x = 1
  while x < len(lines[y]):                                # go over all columns in row
    number = 0                                              # reset number
    num_chars = 0
    while lines[y][x + num_chars].isdigit():                # is location a number?
      number = number * 10 + int(lines[y][x + num_chars])     # compute the number
      num_chars = num_chars + 1                               # count the number of chars
    if num_chars > 0:                                       # do we have a number?
      
      symbols = []                                            # prepare a symbol indicators list
      for y_off in range(-1,2):                               # go over row -1 to row +1 around number
        symbols.append([0 for _ in range(0,num_chars+2)])     # prepare 3 rows with symbols indicators
        for x_off in range(-1,num_chars+1):                     # go over x-1 to x+num_chars+1

          # part1: determine char is symbol and mark with 1 for symbol leave 0 for no symbol
          if lines[y+y_off][x+x_off].isdigit() is False and lines[y+y_off][x+x_off] != '.':
            symbols[y_off+1][x_off+1] = 1

          # part2: record possible gears in dictionary by location key, append more numbers later
          if lines[y+y_off][x+x_off] == '*':
            possible_gears.setdefault(str(x+x_off)+','+str(y+y_off), []).append(number)   # add to list. key = "x,y"

      # number handled
      if max(max(symbols)) :                                    # is an adjecent symbol present? symbols is a list of 3 lists
        part1_sum = part1_sum + number                          # compute sum of number with adjecent symbols

      x = x + num_chars                                     # jump over number
    else:
      x = x + 1                                             # not part of number, go to next char

# part 2
part2_sum = 0
for loc in possible_gears:
  if len(possible_gears[loc]) == 2:                           # determine the number of numbers around a '*'
    part2_sum = part2_sum + (possible_gears[loc][0] * possible_gears[loc][1])   # compute sum of gear ratios

aoc.result(part1_sum, part2_sum)
