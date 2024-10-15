class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c in hashmap and len(stack)>0:
                #check if stack has the same open parenthesis
                if (hashmap[c]!=stack[-1]):
                    return False
                
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        
        if len(stack)!=0:
            return False
        
        return True


sol = Solution()

testcase = "([])"
testcase2 = "){"
print(sol.isValid(testcase2))