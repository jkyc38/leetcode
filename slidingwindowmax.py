from typing import List

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window 
moves right by one position.

Return the max sliding window.'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)< k:
            return max(nums)
        
        q = deque()
        ret = []


        for n in range(k):
            q.append(nums[n]) #adds everything to q up until size k
        
        l, r = 0, k-1
        maxNum = max(q)

        while r<len(nums):
            if r<len(nums):
                if q.popleft() == maxNum:
                    maxNum = max(q)
                    ret.append(maxNum)
                else:
                    ret.append(maxNum)
                r+=1
                if r<len(nums):
                    q.append(nums[r])
            
        return ret
    

nums = [1,3,-1,-3,5,3,6,7]
exp = [3,3,5,5,6,7]
k = 3
sol = Solution()

ret = sol.maxSlidingWindow(nums=nums, k=k)
print(ret)

#my solution/ brute force approach
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)< k:
            return max(nums)
        
        q = deque()
        ret = []


        for n in range(k):
            q.append(nums[n]) #adds everything to q up until size k
        
        l, r = 0, k-1
        # maxNum = max(q)
        while r<len(nums):
            ret.append(max(q))
            q.popleft()
            r+=1
            if r<len(nums):
                q.append(nums[r])

        return ret
        

#optimized and better solution
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()

        l = r = 0

        while r<len(nums):
            while q and nums[[q[-1]]]<nums[r]:
                q.pop()
            
            q.append(r)

            if q[0]< r-k+1:
                q.popleft()
            
            if(r-l+1)>k:
                output.append(nums[q[0]])
                l+=1
        return output
