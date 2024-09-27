class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for index, num in enumerate(nums):
            if target<num:
                continue
            num1 = nums[index]
            for index2, n in enumerate(nums):
                if index2 == index: #skips the dupe
                    continue
                if target == num1+n:
                    return [index, index2]

      
            #grab the first number and add it to every subsequent number and check if its equivalent to the target and then increment if it doesn't

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for idx, num in enumerate(nums):
            n = target - num

            if n in map:
                return [idx, map[n]]
            else:
                map[num] = idx
                
        return []
        