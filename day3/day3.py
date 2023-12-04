import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

input = [
  "467..114..",
  "...*......",
  "..35..633.",
  "......#...",
  "617*......",
  ".....+.58.",
  "..592.....",
  "......755.",
  "...$.*....",
  ".664.598.."
]

# get lines and add a '.' perimeter
lines = ['.' + line + '.' for line in aoc.loadlines(discard_empty_lines=True)]
#lines = ['.' + line + '.' for line in input]
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

part1_sum = 0
for y in range(1, len(lines)-1):                        # go over all rows
  x = 1
  while x < len(lines[y]):                          # go over all columns
    number = 0                                          # reset number
    num_chars = 0
    while lines[y][x + num_chars].isdigit():                        # is location a number?
      number = number * 10 + int(lines[y][x + num_chars])           # compute the number
      num_chars = num_chars + 1
    if num_chars > 0:
      symbols = [[1 if lines[y+y_off][x+x_off].isdigit() is False and lines[y+y_off][x+x_off] is not '.' else 0 for x_off in range(-1,num_chars+1)] for y_off in range(-1,2)]
      has_symbol = max(max(symbols))
      if has_symbol:
        part1_sum = part1_sum + number
      x = x + num_chars
    else:
      x = x + 1

aoc.result(part1_sum, "")
