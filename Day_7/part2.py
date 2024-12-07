from scripts.utils import *

# Only difference in part2 is the operators list
operators = ["+", "*", "||"]

# Choose operator or concatenate the numbers
def make_op(x, y, op):
    if op == "+":
        return x + y
    elif op == "*":
        return x * y
    elif op == "||":
        length = len(str(y))
        return x * (10 ** length) + y
    return -1

# Check all combinations and return True if they match the criteria
def evaluate_combinations(numbers, result):
    nums = list(map(int, numbers))

    def check(e, n, total):
        if e == n:
            return total == result
        if e == 0:
            if check(e+1, n, nums[0]):
                return True
        else:
            for op in operators:
                res = make_op(total, nums[e], op)
                if res <= result:
                    if check(e+1, n, res):
                        return True
        return False

    return check(0, len(nums), 0)

file = "input.txt"
total = 0
for line in parse_input(file):
    result, numbers = line.split(":")
    numbers = numbers.strip().split()

    # If line is valid add the result to the total
    if evaluate_combinations(numbers, int(result)):
        total += int(result)

print(total)