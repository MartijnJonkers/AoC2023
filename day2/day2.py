import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

sum_part1 = 0
sum_part2 = 0
lines = aoc.loadlines(discard_empty_lines=True)
games = [str.split(str.split(line, ":")[1],";") for line in lines]
for game_id in range(1,len(games)+1):
  game = [game.strip().replace(",","").split(" ") for game in games[game_id-1]]
  min_cubes = {"red":0,"green":0,"blue":0}
  valid = True
  for hand in game:
    for i in range(0, len(hand), 2):
      
      # part 1
      if( ( hand[i+1] == "red"   and int(hand[i]) > 12 ) or
          ( hand[i+1] == "green" and int(hand[i]) > 13 ) or
          ( hand[i+1] == "blue"  and int(hand[i]) > 14 ) ) :
        valid = False
      
      # part 2
      if(min_cubes[hand[i+1]] < int(hand[i])):
        min_cubes[hand[i+1]] = int(hand[i])

  # part 1
  if valid:
    sum_part1 = sum_part1 + game_id

  # part 2
  power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
  sum_part2 = sum_part2 + power

aoc.result(sum_part1, sum_part2)
