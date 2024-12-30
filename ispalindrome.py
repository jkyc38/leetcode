class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
            
        return True
    

sol = Solution()
s = "A man, a plan, a canal: Panama"
sol.isPalindrome(s)