# FUNCTIONS
def parse_input(file):
    with open(file) as f:
        return [line.strip() for line in f]

def whole_input(file):
    return open(file, "r").read().strip()

# Get neighbors
def get_neighbors(x, y, grid, diagonal=False):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    if diagonal:
        directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

# Parses input into a 2d grid
def parse_grid(file):
    with open(file) as f:
        return [list(line.strip()) for line in f]
    

from itertools import permutations, combinations

# All permutations
def all_permutations(elements):
    return list(permutations(elements))

# All combinations
def all_combinations(elements, r):
    return list(combinations(elements, r))
# -----------------------------------
# COPY into code

# Line by line
file = "input.txt"
for line in parse_input(file):
    a = line

# Whole input
file = "input.txt"
a = whole_input(file)

# Split at *
a = line.split("*")

# Split all chars
a = list(whole_input(file))

# Min, max, count
"""
a = max(a,b)
a = min(a,b)
a.count(2)
"""

# ---------------------------------
# ALGOS
from heapq import heappop, heappush

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]  # (cost, (x, y))
    distances = {start: 0}
    
    while pq:
        cost, (x, y) = heappop(pq)
        if (x, y) == end:
            return cost
        
        for nx, ny in get_neighbors(x, y, grid):
            new_cost = cost + grid[nx][ny]
            if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                distances[(nx, ny)] = new_cost
                heappush(pq, (new_cost, (nx, ny)))
    
    return float("inf")  # No path found