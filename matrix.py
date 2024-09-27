mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print every element
# for arr in array:
#     for j in arr:
#         print(j)



#print diagonal

#print everything

for row in range(len(mat)):
    for col in range(len(mat[0])):
        print(mat[row][col])

        
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m*n != r*c:
            return mat

    pass

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        pass