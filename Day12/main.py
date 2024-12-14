import sys
import math
from enum import Enum

running_corners = 0
running_area = 0

io = sys.stdin
lines = []
for line in io:
    lines.append([x for x in line.strip()])

print(lines)

def solve(y, x):
    global lines
    global running_corners
    global running_area
    running_area += 1
    char = lines[y][x]
    lines[y][x] = '.' + char

    no_up = False
    no_down = False
    no_left = False
    no_right = False

    is_up_left = False
    is_up_right = False
    is_down_right = False
    is_down_left = False

    if y > 0 and lines[y-1][x] == char:
        solve(y-1, x)
    elif not (y > 0 and lines[y-1][x][-1] == char):
        no_up = True

    if y < len(lines) - 1 and lines[y+1][x] == char:
        solve(y+1, x)
    elif not (y < len(lines) - 1 and lines[y+1][x][-1] == char):
        no_down = True

    if x > 0 and lines[y][x-1] == char:
        solve(y, x-1)
    elif not (x > 0 and lines[y][x-1][-1] == char):
        no_left = True

    if x < len(lines[y]) - 1 and lines[y][x+1] == char:
        solve(y, x+1)
    elif not (x < len(lines[y]) - 1 and lines[y][x+1][-1] == char):
        no_right = True

    if x < len(lines[y]) - 1 and y > 0 and lines[y-1][x+1][-1] == char:
        is_up_right = True

    if x > 0 and y > 0 and lines[y-1][x-1][-1] == char:
        is_up_left = True

    if x < len(lines[y]) - 1 and y < len(lines) - 1 and lines[y+1][x+1][-1] == char:
        is_down_right = True

    if x > 0 and y < len(lines) - 1 and lines[y+1][x-1][-1] == char:
        is_down_left = True

    if no_up and no_left:
        running_corners += 1
    if no_up and no_right:
        running_corners += 1
    if no_down and no_right:
        running_corners += 1
    if no_down and no_left:
        running_corners += 1
    
    if (not no_up) and (not no_left) and (not is_up_left):
        running_corners += 1
    if (not no_up) and (not no_right) and (not is_up_right):
        running_corners += 1
    if (not no_down) and (not no_left) and (not is_down_left):
        running_corners += 1
    if (not no_down) and (not no_right) and (not is_down_right):
        running_corners += 1

sum = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x][0] is not '.':
            running_corners = 0
            running_area = 0
            print(f"starting area {lines[y][x]}, y: {y}, x: {x}")
            solve(y, x)
            print(f"area {running_area}, corners: {running_corners}")
            sum += running_corners * running_area

print(sum)
