import sys
import math
from enum import Enum

class Node:
    def __init__(self, num):
        self.num = num
        self.score = -1
        self.children = []
        self.x = 0
        self.y = 0

io = sys.stdin
lines = []
for line in io:
    lines.append([Node(int(x)) for x in line.strip()])

starts = []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j].x = j
        lines[i][j].y = i
        if lines[i][j].num == 0:
            starts.append(lines[i][j])

        if i > 0 and lines[i-1][j].num == lines[i][j].num + 1:
            lines[i][j].children.append(lines[i-1][j])

        if i < len(lines) - 1 and lines[i+1][j].num == lines[i][j].num + 1:
            lines[i][j].children.append(lines[i+1][j])
            
        if j > 0 and lines[i][j-1].num == lines[i][j].num + 1:
            lines[i][j].children.append(lines[i][j-1])

        if j < len(lines[i]) - 1 and lines[i][j+1].num == lines[i][j].num + 1:
            lines[i][j].children.append(lines[i][j+1])


def recurse_2(node):
    if node.num == 9:
        node.score = 1
    if node.score != -1:
        return node.score
    if node.num < 9 and len(node.children) == 0:
        return 0
    node.score = sum([recurse_2(x) for x in node.children])
    return node.score

def solve_1(node):
    ends = set()
    def recurse_1(node):
        if node.num == 9:
            ends.add((node.x, node.y))
        else:
            for x in node.children:
                recurse_1(x)
    recurse_1(node)
    return len(ends)

print(sum([solve_1(x) for x in starts]))
print(sum([recurse_2(x) for x in starts]))

