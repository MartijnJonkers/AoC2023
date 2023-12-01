import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

#part 1
part1 = sum([int(nr[0] + nr[-1]) for nr in ["".join(filter(lambda x: x.isdigit(), line)) for line in aoc.loadlines()]])

#part 2
lines = aoc.loadlines()
lines = [line.replace("one", "o1e") for line in lines]
lines = [line.replace("two", "t2o") for line in lines]
lines = [line.replace("three", "t3e") for line in lines]
lines = [line.replace("four", "f4r") for line in lines]
lines = [line.replace("five", "f5e") for line in lines]
lines = [line.replace("six", "s6x") for line in lines]
lines = [line.replace("seven", "s7n") for line in lines]
lines = [line.replace("eight", "e8t") for line in lines]
lines = [line.replace("nine", "n9e") for line in lines]
part2 = sum([int(nr[0] + nr[-1]) for nr in ["".join(filter(lambda x: x.isdigit(), line)) for line in lines]])

aoc.result(part1, part2)

#oneliner
#print(sum([int(nr[0] + nr[-1]) for nr in ["".join(filter(lambda x: x.isdigit(), line)) for line in open("input.txt").readlines()]]))