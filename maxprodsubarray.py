from typing import List
"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #for each element in the array keep multiplying and get the max product
        maxProd = nums[0]

        for idx,i in enumerate(nums):
            currProd = 1
            for idx2, j in enumerate(nums[idx-1:]):
                if idx ==idx2:
                    continue

                currProd*=j
                maxProd = max(maxProd, currProd)

        return maxProd
    

tc = [-1,-1]

sol = Solution()

sol.maxProduct(nums=tc)
