from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        numRows = len(words)
        # numCols = len(words[0])

        # print(f'Num Rows: {numRows}')
        # print(f'Num Cols: {numCols}')


        for i in range(numRows):
            print("beginning of word")
            rowWord = words[i]
            numCols = len(words[i])
            colWord = ""
            if len(words[i])> numRows: #if the current length of the word is greater than the rows the
                return False
            for j in range(numCols):
                if j>=numRows:
                    return False
                if i>=len(words[j]):
                    return False
                colWord+=words[j][i]

                # print(words[j][i])
         
            if rowWord!=colWord:
                return False
            
        return True
            



sol = Solution()
words = ["ball","asee","let","lep"]
words2 = ["abc","b"]
sol.validWordSquare(words=words)