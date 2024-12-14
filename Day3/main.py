import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line)
    
sum = 0
big_line = " ".join(lines)
split_lines = big_line.split("do()")
for split_line in split_lines:
    do_line = split_line.split("don't()")
    matches = re.finditer(r'mul\(([0-9][0-9]?[0-9]?),([0-9][0-9]?[0-9]?)\)', do_line[0])
    if not matches:
        continue
    for match in matches:
        sum += int(match.group(1)) * int(match.group(2))
print(sum)