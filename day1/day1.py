import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import aoc

input = aoc.load().read()
input = aoc.read()
input = aoc.loadlines()
input = aoc.loadlines(discard_empty_lines=True)

aoc.result("unknown", "unknown")