from scripts.utils import *

file = "input.txt"
dict = {}
total = 0

# Iterate though all numbers. If this a|b is true, then no b's hall be before an a.
def isvalid(numbers):
    for i in range(len(numbers)):
        if int(numbers[i]) not in dict.keys():
            continue
        for j in range(i):
            if int(numbers[j]) in dict.get(int(numbers[i])):
                return False
    return True

for line in parse_input(file):
    # Read the rules to a dictionary
    if "|" in line:
        number, post = line.split("|")
        if int(number) not in dict:
            dict[int(number)] = [int(post)]
        else:
            dict[int(number)].append(int(post))
    # Check if the numbers are valid 
    elif "," in line:
        numbers = line.split(",")
        if isvalid(numbers):
            total += int(numbers[len(numbers)//2])

print(total)