from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # split_par = paragraph.split(" ")
        liststr = [c.lower() if c.isalnum() else " " for c in paragraph]
        # print(liststr)
        # convertStr = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        convertStr = "".join(c.lower() if c.isalnum() else " " for c in paragraph)
        
        # print(convertStr)
        split_par = convertStr.split()
        print(split_par)
        hashmap = {}
        # print(split_par)
        for word in split_par:

            # check if word is in banned
            if word in banned:
                continue # skip it

            if word not in hashmap:
                hashmap[word] = 1
                continue
            
            hashmap[word]+=1
        # print(hashmap.items())
        return max(hashmap.items(), key=lambda x:x[1])[0]
    

sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol.mostCommonWord(paragraph=paragraph, banned=banned)

