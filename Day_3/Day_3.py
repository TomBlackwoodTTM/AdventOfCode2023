
import numpy as np
from pathlib import Path
from collections import defaultdict

input_set = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def parts_finder(input_set:list):
    data_set = [[d.replace('.', '') for d in row.replace('\n', '')] for row in input_set]
    data_set = np.array(data_set) 
    print(data_set)
    C, R  = data_set.shape
    nums = defaultdict(list)
    p1 = 0
    for y, row in enumerate(data_set):
        gears = set()
        n = 0
        is_part = False
        for x, val in enumerate(row):
            if x < C and val.isdigit():
                n = n * 10 + int(val)
                for dy in [-1, 0, 1]:
                   for dx in [-1, 0, 1]: 
                        if (0 <= y + dy < C) and (0 <= x + dx < R):
                            ch = data_set[y+dy, x+dx]
                            if ch and not ch.isdigit():
                               is_part=True
                            if ch == '*':
                                gears.add((y+dy, x+dx))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n) 

                if is_part:
                    # print(n)
                    p1 += n
                n=0
                is_part = False
                gears = set()

    print(p1)
    p2 = 0
    for k,v in nums.items():
        if len(v)==2:
            p2 += v[0]*v[1]
    print(p2)
    
# parts_finder(input_set.split('\n'))

with open (Path(__file__).parent / 'data/input.txt', 'r') as f:
    parts_finder(input_set = f.readlines())


D = open(Path(__file__).parent / 'data/input.txt').read().strip()
lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)
p2 = 0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)


import math
import re
from collections import defaultdict
from itertools import islice

with open('data/input.txt', 'r') as f:
    data = f.read()

line_len = len(data.split(maxsplit=1)[0])
data = data.replace("\n", "")

gears = re.finditer(r"\*", data)
numbers = re.finditer(r"\d+", data)
indices = defaultdict(list[int])

n = 0

for match in numbers:
    number = int(match.group())
    span = match.span()
    indices[span[0] - 1] += [number]
    indices[span[1]] += [number]
    for i in range(span[0] - 1, span[1] + 1):
        indices[i + line_len] += [number]
        indices[i - line_len] += [number]

for gear in gears:
    nums = indices.get(gear.span()[0], "")
    if len(nums) == 2:
        n += math.prod(nums)

print(n)
