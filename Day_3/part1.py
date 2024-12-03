from scripts.utils import *
import re

file = "input.txt"
whole = whole_input(file)

pattern = r"mul\((\d+),(\d+)\)"
all = re.findall(pattern, whole)

# Iterate over found mul() patterns
total = 0
for element in all:
    total += int(element[0]) * int(element[1])

print(total)