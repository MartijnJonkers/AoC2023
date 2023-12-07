
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file="example.txt"
file="input.txt"

# ----- part 1

hands = [line.split(' ') for line in aoc.loadlines(file=file, discard_empty_lines=True)]
for i in range(0, len(hands)):
  hands[i] = [
    [int(card) for card in hands[i][0]
     .replace('2','2 ').replace('3','3 ').replace('4','4 ')
     .replace('5','5 ').replace('6','6 ').replace('7','7 ') 
     .replace('8','8 ').replace('9','9 ').replace('T','10 ')
     .replace('J','11 ').replace('Q','12 ').replace('K','13 ')
     .replace('A','14 ').strip().split(' ')],
    int(hands[i][1])
  ]

def hand_strength_part1(hand):
  type_count = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}
  for card in hand[0]:
    type_count[card] = type_count[card] + 1
  n_of_kind_type = max(type_count, key=type_count.get)
  n_of_kind_num = type_count[n_of_kind_type]
  if( n_of_kind_num == 5 ):
    strength = 7  # 5 of a kind
  elif( n_of_kind_num == 4 ):
    strength = 6  # 4 of a kind
  elif( n_of_kind_num == 3 ) and (2 in type_count.values()):
    strength = 5  # full house
  elif( n_of_kind_num == 3 ):
    strength = 4  # 3 of a kind
  elif(list(type_count.values()).count(2) == 2 ):
    strength = 3  # 2 pair
  elif( n_of_kind_num == 2 ):
    strength = 2  # 1 pair
  elif( n_of_kind_num == 1 ):
    strength = 1  # high card

  # make room for high card compare in order (first * 100_000_000, second * 1_000_000, third * 10_000, etc)
  strength = strength * 10_000_000_000
  for i in range(0,len(hand[0])):
    shift  = pow(100, (len(hand[0])-i-1))
    strength = strength + (hand[0][i] * shift)
  return strength

# sort by strength
sorted_hands_part1 = sorted(hands, key=hand_strength_part1)

# winnings
part1_sum = 0
for rank in range(1, len(sorted_hands_part1)+1):
  part1_sum = part1_sum + (sorted_hands_part1[rank-1][1] * rank)

# ----- part 2

hands = [line.split(' ') for line in aoc.loadlines(file=file, discard_empty_lines=True)]
for i in range(0, len(hands)):
  hands[i] = [
    [int(card) for card in hands[i][0]
     .replace('2','2 ').replace('3','3 ').replace('4','4 ')
     .replace('5','5 ').replace('6','6 ').replace('7','7 ') 
     .replace('8','8 ').replace('9','9 ').replace('T','10 ')
     .replace('J','1 ').replace('Q','12 ').replace('K','13 ')  # J = 1 !
     .replace('A','14 ').strip().split(' ')],
    int(hands[i][1])
  ]

def hand_strength_part2(hand):
  type_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 12:0, 13:0, 14:0}
  for card in hand[0]:
    type_count[card] = type_count[card] + 1
  n_of_kind_type = max(type_count, key=type_count.get)
  n_of_kind_num = type_count[n_of_kind_type]
  n_j = type_count[1] # number of J's
  if( ( n_of_kind_num == 5 ) or 
      ( n_of_kind_num == 4 and n_j == 1 ) or 
      ( n_of_kind_num == 3 and n_j == 2 ) or 
      ( (2 in type_count.values()) and n_j == 3 ) or # 1 pair and 3 J's
      ( n_j == 4 ) ):                                # 4 J's
    strength = 7  # 5 of a kind
  elif( ( n_of_kind_num == 4 ) or 
        ( n_of_kind_num == 3 and n_j == 1 ) or 
        ( (list(type_count.values()).count(2) == 2) and n_j == 2 ) or # 1 pair and 2 J's
        ( n_j == 3 ) ):
    strength = 6  # 4 of a kind
  elif(list(type_count.values()).count(2) == 2 ) and (n_j == 1):
    strength = 5  # full house (2 pairs and 1 J)
  elif( n_of_kind_num == 3 ) and (2 in type_count.values()):
    strength = 5  # full house (no J)
  elif( ( n_of_kind_num == 3 ) or 
        ( n_of_kind_num == 2 and n_j == 1 ) or 
        ( n_j == 2 ) ):
    strength = 4  # 3 of a kind
  elif(list(type_count.values()).count(2) == 2 ):
    strength = 3  # 2 pair
  elif( ( n_of_kind_num == 2 ) or
        ( n_of_kind_num == 1 and n_j == 1 ) ):
    strength = 2  # 1 pair
  elif( n_of_kind_num == 1 ):
    strength = 1  # high card

  # make room for high card compare in order (first * 100_000_000, second * 1_000_000, third * 10_000, etc)
  strength = strength * 10_000_000_000
  for i in range(0,len(hand[0])):
    shift  = pow(100, (len(hand[0])-i-1))
    strength = strength + (hand[0][i] * shift)
  return strength

# sort by strength
sorted_hands_part2 = sorted(hands, key=hand_strength_part2)

# winnings
part2_sum = 0
for rank in range(1, len(sorted_hands_part2)+1):
  part2_sum = part2_sum + (sorted_hands_part2[rank-1][1] * rank)

aoc.result(part1_sum, part2_sum)

