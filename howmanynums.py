from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #sort the list in ascending order
        temp = sorted(nums)
        
        print(temp)


        #use hashmap to contain the index of the list
        map = {}
        for i, num in enumerate(temp):
            if num not in map: # if the element is not in the map then you add it if it is then you skip over it
                map[num] = i
        
        res = []
        for i in nums: #loop through original list and add any numbers that are in the map
            res.append(map[i])

        return res
        

sol = Solution()
n = [8,1,2,2,3]
sol.smallerNumbersThanCurrent(n)
