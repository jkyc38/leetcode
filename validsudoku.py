class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        #check every row
        for r in range(rows):
            hashset = set()
            for c in range(cols):
                if board[r][c].isnumeric():
                    num = int(board[r][c])
                    if num in hashset:
                        return False
                    hashset.add(num)
        #check every column
        for c in range(cols):
            hashset = set()
            for r in range(rows):
                if board[r][c].isnumeric():
                    num = int(board[r][c])
                    if num in hashset:
                        return False
                    hashset.add(num)
        #check 3 by 3
        for box_r in range(0, rows, 3):  # Start positions for boxes: 0, 3, 6
            for box_c in range(0, cols, 3):  # Start positions for boxes: 0, 3, 6
                hashset = set()
                # Check each cell within the current 3x3 box
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        if board[r][c].isnumeric():
                            num = int(board[r][c])
                            if num in hashset:
                                return False
                            hashset.add(num)
        return True




x = "."
print(int(x))