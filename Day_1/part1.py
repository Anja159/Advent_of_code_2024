from scripts.utils import *

file = "input.txt"
left_list, right_list = [], []

for line in parse_input(file):
    left,right = int(line.split("   ")[0]), int(line.split("   ")[1])
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()
total = 0

for leftone, rightone in zip(left_list, right_list):
    total += abs(leftone - rightone)

print(total)