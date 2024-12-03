from scripts.utils import *
import re

file = "input.txt"
whole = whole_input(file)

pattern_m = r"mul\((\d+),(\d+)\)"
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"
all = re.finditer(pattern_m, whole)

do_nts = []

# Find where dos and don'ts start
donts = re.finditer(pattern_dont, whole)
dos = re.finditer(pattern_do, whole)

for x in donts:
    do_nts.append((x.start(0), "0"))

for x in dos:
    do_nts.append((x.start(0), "1"))

# An array of 0 and 1 corresponding to dos and don'ts
intervals = [1] * len(whole)
prev = 0
value = 1

for x,y in sorted(do_nts):
    for i in range(prev, x):
        intervals[i] = value
    value = int(y)
    prev = x

# Checking on which interval the mul() is
total = 0
for element in all:
    if intervals[element.start()]:
        total += int(element.group(1)) * int(element.group(2))

print(total)