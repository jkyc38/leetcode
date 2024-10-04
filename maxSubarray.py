from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum <0: #if the current sum is negative
                curSum = 0 #reset it to 0



        