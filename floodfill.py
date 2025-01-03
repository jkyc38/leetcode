from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        orig_color = image[sr][sc]
        image[sr][sc] = color
        directions = [[-1, 0], [0,-1], [1, 0], [0,1]]
        rows, cols = len(image), len(image[0])
        seen = set()
        def bfs(sr, sc):
            q = deque()
            q.append((sr,sc))
            #check if color is the same and also check all four directions
            while q:
                r, c = q.popleft()
                for dir1, dir2 in directions:
                    newRow, newCol = r+dir1, c+dir2

                    if (newRow in range(rows)
                        and newCol in range(cols)
                        and (image[newRow][newCol]==orig_color)
                        and (newRow, newCol) not in seen):

                        image[newRow][newCol] = color
                        q.append((newRow,newCol))
                        seen.add((newRow,newCol))

        bfs(sr,sc)

        return image
