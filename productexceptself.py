from typing import List
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefixArr = []
        for i in range(len(nums)):
            prod*=nums[i]
            prefixArr.append(prod)
        
        print(prefixArr)
        postfixArr = []
        postProd = 1
        for i in range(len(nums)-1, -1, -1):
            postProd*=nums[i]
            # postfixArr.insert(0, postProd)
            postfixArr.append(postProd)
        #[24,24,12,4]
        #[4,12,24,24]
        print(postfixArr)
        ret = []
        for i in range(len(nums)):
            prefix, postfix = 1, 1
            if (i-1) in range(len(nums)):
                prefix = prefixArr[i-1] 
            if (i+1) in range(len(nums)):
                postfix = postfixArr[(len(nums)-2)-i]
            
            ret.append(prefix*postfix)
        print(ret)
        return ret

# sol = Solution()
# nums = [1,2,3,4]
# sol.productExceptSelf(nums=nums)

#optimized solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print('optimized solution')
        n = len(nums)
        ret = [1] * n #creates n elements of 1's
        prefix = 1
        for i in range(n):
            ret[i] = prefix #set the current prefix
            prefix*=nums[i] #update the prefix value
        
        # print(ret)

        postfix = 1
        for i in range(n-1, -1, -1): #iterate backwards from len(nums)-1 to 0
            ret[i] *= postfix
            postfix*=nums[i]
        print(ret)

        return ret

sol = Solution()
nums = [1,2,3,4]
sol.productExceptSelf(nums=nums)
