"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        ptr = 0
        ret = ""
        arr = []
        while ptr<len(s):
            if (ptr+1)<len(s) and s[ptr+1]==s[ptr]:
                arr.append(s)
                ptr+=1
                continue
            ret+=s[ptr]
            ptr+=1


sol = Solution()
s = "aab"
sol.reorganizeString(s)

        
        