import sys
import re
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
directions = list(Direction)

initial_coordinates = (0, 0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            initial_coordinates = (i, j)
coordinates = initial_coordinates
direction = Direction.UP
spaces = set()
spaces.add(coordinates)
while ((direction == Direction.UP and coordinates[0] > 0) or (direction == Direction.DOWN and coordinates[0] < len(lines) - 1) or
       (direction == Direction.LEFT and coordinates[1] > 0) or (direction == Direction.RIGHT and coordinates[1] < len(lines[0]) - 1)):
    next_space = (0, 0)
    if direction == Direction.UP:
        next_space = (coordinates[0] - 1, coordinates[1])
    if direction == Direction.RIGHT:
        next_space = (coordinates[0], coordinates[1] + 1)
    if direction == Direction.DOWN:
        next_space = (coordinates[0] + 1, coordinates[1])
    if direction == Direction.LEFT:
        next_space = (coordinates[0], coordinates[1] - 1)
    if lines[next_space[0]][next_space[1]] == '#':
        idx = directions.index(direction)
        next_idx = (idx + 1) % 4
        direction = directions[next_idx]
    else:
        coordinates = next_space
        spaces.add(next_space)

print(len(spaces))

sum = 0
for space in spaces:
    direction = Direction.UP
    space_direction_set = set()
    state = (space[0], space[1], direction)
    lines[space[0]] = lines[space[0]][:space[1]] + '#' + lines[space[0]][space[1] + 1:]
    coordinates = initial_coordinates
    while ((direction == Direction.UP and coordinates[0] > 0) or (direction == Direction.DOWN and coordinates[0] < len(lines) - 1) or
           (direction == Direction.LEFT and coordinates[1] > 0) or (direction == Direction.RIGHT and coordinates[1] < len(lines[0]) - 1)):
        next_space = (0, 0)
        if direction == Direction.UP:
            next_space = (coordinates[0] - 1, coordinates[1])
        if direction == Direction.RIGHT:
            next_space = (coordinates[0], coordinates[1] + 1)
        if direction == Direction.DOWN:
            next_space = (coordinates[0] + 1, coordinates[1])
        if direction == Direction.LEFT:
            next_space = (coordinates[0], coordinates[1] - 1)
        if lines[next_space[0]][next_space[1]] == '#':
            idx = directions.index(direction)
            next_idx = (idx + 1) % 4
            direction = directions[next_idx]
        else:
            coordinates = next_space
            state = (next_space[0], next_space[1], direction)
            if state in space_direction_set:
                sum += 1
                break
            space_direction_set.add(state)
    lines[space[0]] = lines[space[0]][:space[1]] + '.' + lines[space[0]][space[1] + 1:]

print(sum)