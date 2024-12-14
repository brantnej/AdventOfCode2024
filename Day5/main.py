import sys
import re
from enum import Enum
io = sys.stdin
rule_lines = []
pages_lines = []
rules = True
for line in io:
    if line == "\n":
        rules = False
        continue
    if rules:
        rule_lines.append(line.strip())
    else:
        pages_lines.append(line.strip())

rules_dict = {}

for line in rule_lines:
    [before, after] = [int(x) for x in line.split("|")]
    if after in rules_dict:
        rules_dict[after].add(before)
    else:
        rules_dict[after] = set([before])

sum = 0
problem_2_pages = []
for pages in pages_lines:
    illegal_pages = set()
    legal = True
    page_nums = [int(x) for x in pages.split(',')]
    for page_num in page_nums:
        if page_num in illegal_pages:
            legal = False
            problem_2_pages.append(pages)
            break
        if page_num in rules_dict:
            illegal_pages.update(rules_dict[page_num])
    if legal:
        sum += page_nums[len(page_nums) // 2]

print(sum)

sum = 0
for pages in problem_2_pages:
    pages = set([int(x) for x in pages.split(',')])
    correct_order = []
    while len(pages) > 1:
        illegal_pages = set()
        for page in pages:
            if page in rules_dict:
                illegal_pages.update(rules_dict[page])
        for page in pages:
            if page not in illegal_pages:
                correct_order.append(page)
                pages.remove(page)
                break
    correct_order.append([pages])
    sum += correct_order[len(correct_order) // 2]
print(sum)