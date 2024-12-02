from scripts.utils import *

# Declaring the checks from part1 as a function
def is_safe(nums):
    diffs = []
    prev = nums[0]
    for num in nums:
        diffs.append(num - prev)
        prev = num

    if max(abs(max(diffs)), abs(min(diffs))) < 4 and not (max(diffs) > 0 and min(diffs) < 0) and not 0 in diffs[1:]:
        return True
    return False

file = "input.txt"
total = 0

for line in parse_input(file):
    nums = list(map(int, line.split()))

    # Is the original list safe?
    if is_safe(nums):
        total += 1
        continue
    
    # Second chance
    for i in range(0, len(nums)):
        modified_nums = nums[:i] + nums[i + 1:]
        if is_safe(modified_nums):
            total += 1
            break

print(total)

