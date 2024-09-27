from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l,r = 0, k
        num = 0 
        for i in range(r):
            num+=nums[i]

        maxNum = num
        while r<len(nums):
            r+=1
            l+=1
            num+=nums[r]
            num-=nums[l]

            maxNum = max(maxNum, num)
            r+=1
            l+=1
        return maxNum/k