"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1_s = {}
        hashmap2_t = {}
        for i in range(len(s)):
            if s[i] not in hashmap1_s:
            #check if character is not in hashmap and if its not then
            #add the character along with the index
                hashmap1_s[s[i]] = i
            if t[i] not in hashmap2_t:
                hashmap2_t[t[i]] = i
            if hashmap1_s[s[i]]!=hashmap2_t[t[i]]:
                return False
        
        return True

        
        
sol = Solution()
# s = "bbbaaaba"
# t = "aaabbbba"
s = "egg"
t = "add"
sol.isIsomorphic(s, t)