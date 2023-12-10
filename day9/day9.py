import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

lines = [[int(val) for val in line.strip().split(' ')] for line in aoc.loadlines(discard_empty_lines=True)]

parts = [0,0]
for line in lines:                                # go over all lines
  depth = 0                                         # count the diffs line depth
  lasts, firsts = [], []                            # prepare list for all the first and last values of a diff list
  while(len([1 for e in line if e != 0]) != 0):     # continue as long as all vals in line are not 0
    lasts.append(line[-1])                            # save last of diff list (part 1)
    firsts.append(line[0])                            # save first of diff list (part 2)
    depth = depth + 1                                 # count diff list depth
    diffs = []                                        # prepare new diff list
    for i in range(0, len(line)-1):                   # compute diffs for current vals
      diffs.append(line[i+1] - line[i])                 # add diff to list
    line = diffs                                      # diff list is now the line
  prev = 0                                          # start with previous of 0 for bottom line
  for i in range(len(firsts)-1, -1, -1):            # go over all stored firsts to compute top prev (part 2)
    prev = firsts[i] - prev                           # subtact current prev with last of previous line
  parts[0] += sum(lasts)                            # next val is sum of all lasts (part 1)
  parts[1] += prev                                  # prev is previously computed (part 2)

aoc.result(parts[0], parts[1])
