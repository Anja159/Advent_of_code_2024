from scripts.utils import *

file = "input.txt"
whole = whole_input(file).split("\n")
start_x, start_y, grid = 0, 0, []
curr_direction = (-1, 0)

# Find initial position of ^
for line in whole:
    grid.append(list(line.strip()))
    if "^" in line:
        start_x, start_y = (grid.index(list(line.strip())), line.index("^"))

for i in range(len(grid)*len(grid)):
    temp_x = start_x+curr_direction[0]
    temp_y = start_y+curr_direction[1]

    # Break if out of bounds
    if temp_x > len(grid)-1 or temp_y > len(grid[0])-1 or temp_x < 0 or temp_y < 0:
        break
    
    # If #, turn right
    if grid[temp_x][temp_y] == "#":
        curr_direction = (curr_direction[1], -curr_direction[0])
    
    # Mark visited with X
    grid[start_x][start_y] = "X"

    # Increase in direction
    start_x += curr_direction[0]
    start_y += curr_direction[1]

total = sum(line.count("X") for line in grid)
print(total + 1)
