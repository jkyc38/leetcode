from typing import List
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #check the first index of the row check if target is less than or greater than the first
        #have two pointers to keep track of the row indices
        l, r = 0, len(matrix) -1

        while l<=r:
            middle = (l + r) //2
            if target < matrix[middle][0]:
                #update the right pointer
                r = middle - 1
            elif target > matrix[middle][-1]: #check last element of the row
                l = middle + 1
            else:
                break

        if l>r: #if out of bounds
            return False
        row = matrix[middle]

        l, r = 0, len(row)-1
        while l<=r:
            mid = (l+r)//2
            if row[mid] == target:
                return True
            if target> row[mid]:
                l = mid + 1
            else:
                r = mid -1
            
        return False


matrix = [[1]]
try:
    sol = Solution()
    res = sol.searchMatrix(matrix=matrix, target=1)
    print(res)
except IndexError:
    print("index error")
    print(f'this is the middle: {sol.middle}')
    
