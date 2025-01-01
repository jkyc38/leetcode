from typing import List
from collections import deque
#TODO
#i still need to finish this
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands=0
        def bfs(r,c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                #dfs version
                #row, col = q.pop()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                
                for dir1, dir2 in directions:
                    check_row, check_col = row+dir1, col + dir2
                    if(check_row in range(rows)
                    and check_col in range(cols)
                    and (check_row,check_col) not in seen
                    and grid[check_row][check_col]=="1"):
                        q.append((check_row, check_col))
                        seen.add((check_row, check_col))
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r, c)
                    islands+=1

        return islands

grid = [
    ['1', '1', '0'],
    ['1', '0', '1'],
    ['0', '1', '1']
]

row = len(grid)  # row = 3
directions = [(0,1), (1,0), (-1,0), (0,-1)]  # right, down, up, left

# Let's start at bottom-right corner (2,2)
current_row, current_col = 2, 2  # bottom-right position

print(f"Starting at corner position ({current_row}, {current_col})")
print("Grid bounds are 0-2 for both row and column\n")

for dir1, dir2 in directions:
    check_row = current_row + dir1
    check_col = current_col + dir2
    print(f"Moving {dir1},{dir2}")
    print(f"Checking position ({check_row}, {check_col})")
    print(f"Is {check_row} in range({row})? {check_row in range(row)}")
    if check_row in range(row):
        print("✓ Position is valid for row")
    else:
        print("✗ Position is OUT OF BOUNDS for row")
    
    print("---")