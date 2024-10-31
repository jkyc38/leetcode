class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr = [w for w in arr if w]
        arr.reverse()
        ret = " ".join(arr)
        print(arr)
        print(ret)

        return ret
        




sol = Solution()
s = "  hello world   "
sol.reverseWords(s)