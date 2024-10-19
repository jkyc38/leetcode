from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #set markers for the rows that have a zero in it

        #if the row or column has the 0 then you make all of the either row
        #or columninto a zero
        #literlaly making bomber man lol
        
        row, col = len(matrix), len(matrix[0]) #matrix length = row, matrix[i] length = column
        row_marker = []
        col_marker = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_marker.append(i) #keep track of the row that has the zero
                    col_marker.append(j) #keep track of the col that has the zero
        
        for i in row_marker:
            for j in range(col):
                matrix[i][j] = 0
                

        for i in col_marker:
            for j in range(row):
                matrix[j][i] = 0
            

