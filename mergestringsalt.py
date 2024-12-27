class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #two pointer solution
        #initialize pointer 1 and pointer 2 in the two words respectively
        p1 = 0
        # get the len of the shorter string

        short_len = min(len(word1), len(word2))
        short = word1 if len(word1)==short_len else word2 
        long = word1 if len(word1)!=short_len else word2
        merge=""
        while p1<len(short):
            merge+=word1[p1]
            merge+=word2[p1]

            p1+=1
        
        merge+=long[p1:]

        return merge



sol = Solution()
word1 = "abc"
word2 = "pqr"

ret = sol.mergeAlternately(word1, word2)
print(ret)
