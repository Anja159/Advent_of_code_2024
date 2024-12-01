from scripts.utils import *

file = "input.txt"
left_list, right_list = [], []

for line in parse_input(file):
    left,right = int(line.split("   ")[0]), int(line.split("   ")[1])
    left_list.append(left)
    right_list.append(right)

total = 0

for leftone in left_list:
    total += right_list.count(leftone) * leftone

print(total)