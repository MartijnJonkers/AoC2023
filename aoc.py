import os
import sys

def load(file="input.txt", rights="r"):
  return open(os.path.join(sys.path[0], file), rights)

def read(file="input.txt", rights="r"):
  return load(file, rights).read()

def loadlines(file="input.txt", rights="r", strip = True, discard_empty_lines = False):
  return [(line.strip() if strip else line) for line in load(file, rights).readlines() if (line.strip() if discard_empty_lines else line)]

def result(p1 = "", p2 = ""):
  if( len(str(p1)) > 0 ):
    print("part 1 =", p1)
  if( len(str(p2)) > 0 ):
    print("part 2 =", p2)

# Greatest Common Divisor
def gcd(a, b):
  if (a == 0):
    return b
  return gcd(b % a, a)

# Lowest Common Multiple
def lcm(a, b):
  return (a / gcd(a, b)) * b

def add_perimeter( char , lines):
  lines = [char + line + char for line in lines]
  lines.insert(0, char * len(lines[0]))
  lines.append(char * len(lines[0]))
  return lines

