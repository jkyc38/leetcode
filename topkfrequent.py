import heapq
from typing import List
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        #count frequency of each number
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n]+=1
        
        freq_list = [(-count, num) for num, count in hashmap.items()]
        
        heapq.heapify(freq_list)

        ret = []

        for _ in range(k):
            ret.append(heapq.heappop(freq_list)[1])
        
        return ret
