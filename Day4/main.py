import sys
import re
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line)

sum = 0

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8

def walk_line(char, direction, i, j):
    if i < 0 or i >= len(lines):
        return 0
    if j < 0 or j >= len(lines[i]):
        return 0
    next_char = ''
    match char:
        case 'X':
            next_char = 'M'
        case 'M':
            next_char = 'A'
        case 'A': 
            next_char = 'S'
    if lines[i][j] != next_char:
        return 0
    if lines[i][j] == 'S':
        return 1
    match direction:
        case Direction.UP:
            return walk_line(next_char, direction, i - 1, j)
        case Direction.DOWN:
            return walk_line(next_char, direction, i + 1, j)
        case Direction.LEFT:
            return walk_line(next_char, direction, i, j - 1)
        case Direction.RIGHT:
            return walk_line(next_char, direction, i, j + 1)
        case Direction.UP_LEFT:
            return walk_line(next_char, direction, i - 1, j - 1)
        case Direction.UP_RIGHT:
            return walk_line(next_char, direction, i - 1, j + 1)
        case Direction.DOWN_LEFT:
            return walk_line(next_char, direction, i + 1, j - 1)
        case Direction.DOWN_RIGHT:
            return walk_line(next_char, direction, i + 1, j + 1)
        

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            sum += walk_line('X', Direction.UP, i - 1, j)
            sum += walk_line('X', Direction.DOWN, i + 1, j)
            sum += walk_line('X', Direction.LEFT, i, j - 1)
            sum += walk_line('X', Direction.RIGHT, i, j + 1)
            sum += walk_line('X', Direction.UP_LEFT, i - 1, j - 1)
            sum += walk_line('X', Direction.UP_RIGHT, i - 1, j + 1)
            sum += walk_line('X', Direction.DOWN_LEFT, i + 1, j - 1)
            sum += walk_line('X', Direction.DOWN_RIGHT, i + 1, j + 1)
print(sum)

sum = 0
for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == 'A':
            if (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M') or (lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S'):
                if (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M') or (lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S'):
                    sum += 1
print(sum)