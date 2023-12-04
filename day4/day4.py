import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

# get list of 2 list of seperated number per line
lines = aoc.loadlines(discard_empty_lines=True)
cards =[[part.strip().split(' ') for part in line.replace("  ", " ").split(':')[1].split('|')] for line in lines]

num_cards = [1 for _ in range(0,len(cards))]              # part 2: prepare number of cards list (1 each)
part1_sum = 0
for i in range(0, len(cards)):
  matches = len(set(cards[i][0]) & set(cards[i][1]))      # get nr of overlapping entries
  if( matches > 0 ):
    part1_sum = part1_sum + pow(2,matches-1)              # part 1
  for j in range(1, matches+1):
    num_cards[i+j] = num_cards[i+j] + num_cards[i]        # part 2
part2_sum = sum(num_cards)

aoc.result(part1_sum, part2_sum)
