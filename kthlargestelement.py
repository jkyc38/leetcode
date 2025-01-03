from typing import List
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums_max_heap = [-n for n in nums]

        heapq.heapify(nums_max_heap)
        ret = 0
        for _ in range(k):
            ret = heapq.heappop(nums_max_heap)
        

        return -ret