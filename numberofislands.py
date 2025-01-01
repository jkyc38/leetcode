from typing import List
from collections import deque
#TODO
#i still need to finish this
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
            pass

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in seen:
                    bfs(r, c)
                    islands+=1

        pass