
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#file="example2.txt"
file="input.txt"

lines = aoc.loadlines(file=file)
instructions = lines[0]

# create a node list with the left and right entries
nodes = {}
for node in lines[2:]:
  parts = node.strip().split(' ')
  nodes[parts[0]] = {
    'name': parts[0],
    'L': parts[2][1:4],
    'R': parts[3][:3]
  }

# find the starting nodes
starts = []
for name in nodes:
  if( name[2] == 'A'):
    starts.append(nodes[name])

# get the number of steps from A to Z node for all starting nodes
steps_list = []
for current_node in starts:
  steps = 0

  # go to next node until Z node detected
  while True:

    # take step to next node
    instruction = instructions[steps % len(instructions)]
    current_node = nodes[current_node[instruction]]
    steps = steps + 1

    # is node a Z node?
    if(current_node['name'][2] == 'Z'):

      # store the number of steps from A node to Z node
      steps_list.append(steps)

      # somehow the number of steps from A to Z is the same as Z to Z ?? 
      # So stop at first Z node detected.
      break

# sort the resulting number of steps per starting node
steps_list = sorted(steps_list)

# find Lowest Common Multiple of all entries in list

if False: # Very slow way, takes forever (~400 sec). :( 

  for i in range(0, len(steps_list)-1):
    step = steps_list[i+1]
    while steps_list[i+1] % steps_list[i] > 0:
      steps_list[i+1] = steps_list[i+1] + step
  part2 = steps_list[-1]

else: # Fast way (~500 milli sec). :)

  # gcd and lcm source : https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/

  def gcd(a, b):  # Greatest Common Divisor
      if (a == 0):
          return b
      return gcd(b % a, a)

  def lcm(a, b):  # Lowest Common Multiple
      return (a / gcd(a, b)) * b

  part2 = lcm(steps_list[0], steps_list[1])
  for i in range(1, len(steps_list)):
    part2 = lcm(part2, steps_list[i])

aoc.result(p2=int(part2))
