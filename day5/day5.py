import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file = "example.txt"
#file = "input.txt"
file = "input_christiaan_15880236.txt" #part1 = 621354867

# get maps. format: 
#  [<map name>] = 
#     [src_start] = [dst_start, length]
#     [src_start] = [dst_start, length]
#     [src_start] = [dst_start, length]
lines = aoc.loadlines(file, discard_empty_lines=True)[1:]
map_name = ""
maps = {}
for line in lines:
  if(line[0].isdigit() == False):
    map_name = line.split()[0]
    maps[map_name] = {}
  else:
    map = [int(num) for num in line.split()]
    maps[map_name][map[1]] = [map[0], map[2]]

# do value conversion based on map
def map_convert(value, map:dict):
  for src_start in map:             # go over all map entries
    src_start = src_start
    dst_start = map[src_start][0]
    map_len = map[src_start][1]

    # is value in this map entry?
    if( (value >= src_start) and (value < src_start + map_len)):
      # value is in range, convert it
      return value + (dst_start - src_start)
  return value  # value not in any map

seed_locations = {}
def compute_location(seed):
  global seed_locations

  if( seed in seed_locations ):
    return seed_locations[seed]

  soil        = map_convert(seed,        maps['seed-to-soil'])
  fertilizer  = map_convert(soil,        maps['soil-to-fertilizer'])
  water       = map_convert(fertilizer,  maps['fertilizer-to-water'])
  light       = map_convert(water,       maps['water-to-light'])  
  temperature = map_convert(light,       maps['light-to-temperature'])
  humidity    = map_convert(temperature, maps['temperature-to-humidity'])
  location    = map_convert(humidity,    maps['humidity-to-location'])

  seed_locations[seed] = location

  return location

# ----- part 1 - brute force location for all seeds
seeds = [int(num) for num in aoc.load(file).readline().split(': ')[1].strip().split(' ')]

part1_result = 0
for seed in seeds:
  location = compute_location(seed)
  if part1_result == 0 or part1_result > location:
    part1_result = location

# ----- part 2 - binary search lowest location per seed range
seed_ranges = {}
nums = [int(num) for num in aoc.load(file).readline().split(': ')[1].strip().split(' ')]
for i in range(0, len(nums), 2):
  seed_ranges[nums[i]] = range(nums[i], nums[i] + nums[i+1] - 1)

part2_result = 0
# go over all seed ranges
for key in seed_ranges:

  # binary search lowest number in seed range
  left = seed_ranges[key].start
  right = seed_ranges[key].stop
  while True:
    #seed= left
    seed = int(((right - left) / 2) + left) # determine center seed in range
    location = compute_location(seed)       # get location for this seed

    # binary search ended?
    if left == right:
      # found lowest number in range, is it lowest overall?
      if part2_result == 0 or part2_result > location:
        part2_result = location
      break # no more seeds to check in this range, go to next seed range

    # left = left+1
    # continue

    # determine which half to search next
    if left + 1 == right:
      left = right    # 1 seed remaining to check
    elif location < part2_result:
      right = seed    # found location is lower, even lower number could be in left half
    else:
      left = seed     # found location is higher, lowest in range is in right half

print(part1_result)
print(part2_result)

#aoc.result(part1_result,part2_result)
