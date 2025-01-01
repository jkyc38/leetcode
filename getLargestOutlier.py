from collections import Counter
from math import inf
from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums) #add all the numbers
        count = Counter(nums) #count the frequency of each number

        res = -inf #preset

        for num in nums:
            outlier = total - (2*num)
            # multiply num by 2 because special number and target num are equivalent to each other
            # as a result this would result in the outlier

            # if count[outlier] > (outlier==num): # check the outlier in the frequency map 
            #     res = max(res, outlier)
            
            if outlier!=num and count[outlier]:
                res=max(res,outlier)
            #if the outlier is not num and there exists an outlier in the hashmap then set res to that outlier
        return res
        