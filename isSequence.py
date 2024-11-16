class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        if not s:
            return True
        
        while p2<len(t):
            if p1==len(s):
                break
            
            if s[p1]==t[p2]:
                p1+=1
            p2+=1
            

        if (p1!=len(s)):
            return False
        
        return True
        


# Input: s = "abc", t = "ahbgdc"
# Output: true
s = "axc"
t = "ahbgdc"

sol = Solution()

ret = sol.isSubsequence(s, t)
print(ret)