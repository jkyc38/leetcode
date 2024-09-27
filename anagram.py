from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}

        for i in s:
            if i in map:
                map[i]+=1
            else:
                map.get(i, 1)

        

        for i in t:
            if i in map:
                map2[i]+=1
            else:
                map2.get(i, 1)
        
        print(map)
        print(map2)
        
        return Counter(t)==Counter(s)
        

sol = Solution()
s = "jam"
t = "jar"
sol.isAnagram(s, t)