from collections import deque
import heapq
import math
def lastStoneWeight(stones)->int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones)>1:
        first = abs(heapq.heappop(stones))
        second = abs(heapq.heappop(stones))
        new = first - second
        heapq.heappush(stones, -new)
        #return it back to the index
    
    if len(stones) ==0:
        return 0
    
    return abs(stones[0])

stones=[9,10,1,7,3]
stones = [-s for s in stones]
heapq.heapify(stones)
num = abs(heapq.heappop(stones))
num2 = abs(heapq.heappop(stones))
new = num - num2
heapq.heappush(stones, new)
print(num)
print(num2)
print(stones)
# stones=[9,10,1,7,3]

# num = lastStoneWeight(stones)
# print(num)
