from scripts.utils import *

file = "input.txt"
total = 0

for line in parse_input(file):
    nums = list(map(int, line.split()))
    diffs = []
    prev = nums[0]

    # Calculate the differences between elements
    for num in nums:
        diffs.append(num - prev)
        prev = num

    # If the difference never exceeds 3, if the values never go from positive to negative, and if there are no 0s in the list (except for the first element which is excluded)
    if max(abs(max(diffs)), abs(min(diffs))) < 4 and not (max(diffs) > 0 and min(diffs) < 0) and not 0 in diffs[1:]:
        total += 1

print(total)
