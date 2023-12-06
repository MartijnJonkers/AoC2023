import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file = "example.txt"
file = "input.txt"

# get sorted seeds
seeds = [int(num) for num in aoc.load(file).readline().split(': ')[1].strip().split(' ')]
seeds = sorted(seeds)

# get maps (skip first 2line)
lines = aoc.loadlines(file, discard_empty_lines=True)[1:]
key = ""
maps = {}
for line in lines:
  if(line[0].isdigit() == False):
    if(len(maps) > 0):
      maps[key] = dict(sorted(sorted(maps[key].items())))
    key = line.split()[0]
    maps[key] = {}
  else:
    map = [int(num) for num in line.split()]
    maps[key][map[1]] = [map[0], map[2]]
maps[key] = dict(sorted(sorted(maps[key].items()))) # sort last map

def binary_search_convert(value, map:dict):
  left = 0
  right = len(map)-1
  while True:
    center = int(((right - left) / 2) + left)
    src_start = list(map.keys())[center]
    dst_start = map[src_start][0]
    map_len = map[src_start][1]
    if( (value >= src_start) and (value < src_start + map_len)):
      offset = dst_start - src_start
      return value + offset # return conversion in map entry

    # not in this map entry
    if left == right:
      return value    # no map available
    if left + 1 == right:
      left = right    # 1 map left
    elif src_start > value:
      right = center  # search in left half
    else:
      left = center   # search in right half


def compute_location(seed):
  soil        = binary_search_convert(seed,        maps['seed-to-soil'])
  fertilizer  = binary_search_convert(soil,        maps['soil-to-fertilizer'])
  water       = binary_search_convert(fertilizer,  maps['fertilizer-to-water'])
  light       = binary_search_convert(water,       maps['water-to-light'])
  temperature = binary_search_convert(light,       maps['light-to-temperature'])
  humidity    = binary_search_convert(temperature, maps['temperature-to-humidity'])
  location    = binary_search_convert(humidity,    maps['humidity-to-location'])
  return location

# part 1
part1_result = 0
for seed in seeds:
  location = compute_location(seed)
  if part1_result == 0 or part1_result > location:
    part1_result = location

# lowest_location = -1
# while True:
#   left = 0
#   right = len(seeds)-1
#   while True:
#     center = int(((right - left) / 2) + left)
#     location = compute_location(seeds[center])
#     if lowest_location == -1 or lowest_location > location:
#       lowest_location = location

      
#     # not in this map entry
#     if left == right:
#       print( lowest_location )
#       exit()
#     if left + 1 == right:
#       left = right    # 1 map left
#     elif src_start > value:
#       right = center  # search in left half
#     else:
#       left = center   # search in right half

#location = compute_location(79)
aoc.result(part1_result, "")
