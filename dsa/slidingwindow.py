def maxProfit(prices:list[int])->int:
    buy = 0
    sell = 1
    max = 0

    while(sell<len(prices)):
        if(prices[sell]>prices[buy]):
            profit = prices[sell] - prices[buy]
            if(profit>max):
                max = profit
        else:
            buy=sell
        
        sell+=1
    

    return max

# prices = [10,1,3,6,10,1]
# num = maxProfit(prices)
# print(num)

'''
Input: prices = [10,1,5,6,7,1]

Output: 6
'''

def maxSubArray(nums) -> int:
    maxSub = nums[0] #init the max sub in beginning
    currSum = 0 
    for n in nums:
        if currSum<0:
            currSum=0
        currSum+=n
        maxSub = max(currSum, maxSub)

    return maxSub


def lengthOfLongestSubstring(s: str) -> int:

    #iterate through string with l and r pointer
    #iterating through the string you make a set for every unique character
    #if character is already in set you make a new set and reset the left pointer to the right pointer
    #continue until the end of string then you get the longest substring from that
    if len(s)==0:
        return 0
    l,r = 0,0
    hashset = set()
    longest = 0 
    while r<len(s):
        if s[r] not in hashset:
            hashset.add(s[r])
            longest = max(longest, r-l+1)
            r+=1
        else: 
            hashset.remove(s[l])
            l+=1

        
    return longest

s = " "
print(len(s))
# n = lengthOfLongestSubstring(s)
# print(n)

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l,r = 0, k
        mx = sum(nums[:k])
        avg = mx

        while r< len(nums):
            mx += nums[r]
            mx -= nums[l]

            avg = max(mx, avg)
            r+=1
            l+=1
        
        return avg/k

    