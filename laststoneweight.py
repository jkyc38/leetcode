from typing import List
"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]

        heapq.heapify(maxHeap)
        
        while len(maxHeap)>=1:
            if len(maxHeap)==1:
                break
            
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            
            
            if stone1==stone2:
                continue
            if stone1!=stone2:
                heavier = max(stone1, stone2)
                lighter = min(stone1, stone2)
                newStone = heavier - lighter

            heapq.heappush(maxHeap, -newStone) 

        if len(maxHeap)==0:
            return 0

        return -heapq.heappop(maxHeap)    


sol = Solution()
stones = [2,7,4,1,8,1]
sol.lastStoneWeight(stones=stones)
