import sys
import math
from enum import Enum

running_perimeter = 0
running_area = 0

io = sys.stdin
lines = []
for line in io:
    lines.append([x for x in line.strip()])

print(lines)

def solve(y, x):
    global lines
    global running_perimeter
    global running_area
    running_area += 1
    char = lines[y][x]
    lines[y][x] = '.' + char



    if y > 0 and lines[y-1][x] == char:
        solve(y-1, x)
    elif not (y > 0 and lines[y-1][x][-1] == char):
        running_perimeter += 1

    if y < len(lines) - 1 and lines[y+1][x] == char:
        solve(y+1, x)
    elif not (y < len(lines) - 1 and lines[y+1][x][-1] == char):
        running_perimeter += 1

    if x > 0 and lines[y][x-1] == char:
        solve(y, x-1)
    elif not (x > 0 and lines[y][x-1][-1] == char):
        running_perimeter += 1

    if x < len(lines[y]) - 1 and lines[y][x+1] == char:
        solve(y, x+1)
    elif not (x < len(lines[y]) - 1 and lines[y][x+1][-1] == char):
        running_perimeter += 1
    


sum = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x][0] is not '.':
            running_perimeter = 0
            running_area = 0
            print(f"starting area {lines[y][x]}, y: {y}, x: {x}")
            solve(y, x)
            print(f"area {running_area}, perimeter: {running_perimeter}")
            sum += running_perimeter * running_area

print(sum)
