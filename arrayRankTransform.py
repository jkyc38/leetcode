"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
"""
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ret = []
        hashmap = {}

        sort_arr = sorted(arr) #returns a sorted iterable
        print(sort_arr)
        rank = 1
        for e in sort_arr:
            if e in hashmap: # account for duplicate numbers
                continue
            hashmap[e] = rank
            rank+=1
        
        for e in arr:
            ret.append(hashmap[e])
        print(f'return array: {ret}')
        return ret
    
sol = Solution()
arr = [37,12,28,9,100,56,80,5,12]
sol.arrayRankTransform(arr)
print(f'original array: {arr}')