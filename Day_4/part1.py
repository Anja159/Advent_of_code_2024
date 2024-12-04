from scripts.utils import *

file = "input.txt"
grid = parse_grid(file)
word = 'XMAS'
moves = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
total = 0

def isvalid(x,y,dx,dy,grid):
    for i in range(1, len(word)):
        # Break if it exceeds the borders of our grid
        if x + dx*i < 0 or y + dy*i < 0 or x + dx*i > len(grid) - 1 or y+dy*i > len(grid) - 1:
            return False
        # Break if the letter on i-th index is not correct 
        if not grid[x + dx*i][y + dy*i] == word[i]:
            return False
    return True

for x in range(len(grid[0])):
    for y in range(len(grid)):
        # Continue if the letter equals X 
        if grid[x][y] == word[0]:
            # Iterate over all possible moves
            for dx, dy in moves:
                if isvalid(x,y,dx,dy,grid):
                    total += 1

print(total)
