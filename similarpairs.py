from typing import List
from collections import Counter


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        frozenset()
        def uniqueChar(word):
            map = {}
            for char in word:
                if char not in map:
                    map[char] = 1
            return map
        
        def similarStrings(word1, word2):
            return uniqueChar(word1) == uniqueChar(word2)
        
        map = {}
        for idx, word in enumerate(words):
            map[idx] = word
        
        pairs = set()
    
        for idx, i in enumerate(words):
            for idx2, j in enumerate(words):
                if i==j:
                    continue
                if similarStrings(i,j):
                    if(idx2, idx) not in pairs:

                        pairs.add((idx,idx2))

           
        return len(pairs)
        

sol = Solution()

# words = ["aba","aabb","abcd","bac","aabc"]

words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
count = sol.similarPairs(words)
print(count)