import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

import time
start_time = round(time.time() * 1_000_000)

# part 1
#times =      [49,  78,  79,  80]
#distances = [298,1185,1066,1181]

# part 2
times =     [       49787980]
distances = [298118510661181]

result = 1
for i in range(0, len(times)):
  short_hold_time = 0
  short_hold_dist = 0
  long_hold_time = 0
  long_hold_dist = 0
  for j in [0,1]: # 0 = shortest hold time. 1 = longest hold time

    # binary search
    left = 0
    right = times[i]
    while True:
      center = int(((right-left)/2) + left)

      # compute distance
      race_dist = (times[i] - center) * center
      if j == 0:
        # shortest possible hold time?
        if race_dist > distances[i] and (race_dist < short_hold_dist or long_hold_dist == 0):
          short_hold_time = center
          short_hold_dist = race_dist
      else:
        # longest possible hold time?
        if race_dist > distances[i] and (race_dist < long_hold_dist or long_hold_dist == 0):
          long_hold_time = center
          long_hold_dist = race_dist

      if left + 1 == right:
        left = right
      elif left == right:
        break
      elif j == 0:
        # checking shorted possible hold time
        if race_dist > distances[i]:
          right = center
        elif race_dist <= distances[i]:
          left = center
      else:
        # checking longest possible hold time
        if race_dist > distances[i]:
          left = center
        elif race_dist <= distances[i]:
          right = center

  # multiply all ranges
  result = result * (long_hold_time - short_hold_time + 1)

time.sleep(1)
end_time = round(time.time() * 1_000_000)

print(result, "[" ,end_time - start_time, "us ]")

