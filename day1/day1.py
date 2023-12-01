import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

part1 = sum([int(number[0] + number[-1]) for number in ["".join(filter(lambda x: x.isdigit(), map(str, line))) for line in aoc.loadlines()]])

aoc.result(part1, "unknown")

#oneliner
#print(sum([int(nr[0] + nr[-1]) for nr in ["".join(filter(lambda x: x.isdigit(), map(str, line))) for line in open("input.txt").readlines()]]))