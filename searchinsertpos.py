from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search but insert it the desired pos
        
        def helper(nums, target):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return mid

                if target< nums[mid]:
                    r = mid -1
                
                elif target> nums[mid]:
                    l = mid+1

            return l
            
        return helper(nums,target)




