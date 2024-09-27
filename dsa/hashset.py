#set or hashmap

def longestConsecutive(nums) -> int:
    numSet = set(nums)
    longest = 0

    #check if prev exists if not then start of seq exists then check if theres a +1 exists if it does then keep checking for the sequence
    for n in nums:
        if (n-1) not in numSet:
            length = 0 
            while(n +length) in numSet:
                length+=1
            longest = max(length, longest)
    return longest

def twoSum(nums: list[int], target: int) -> list[int]:
    
    pass
    
nums = [2,20,4,10,3,4,5]
#EXPECTED: 4
print("TEST CASE 1: ", longestConsecutive(nums))
nums = [0,3,2,5,4,6,1,1]
#EXPECTED: 7
print("TEST CASE 2: ", longestConsecutive(nums))
nums = [0,0]
#EXPECTED: 1
print("TEST CASE 3: ", longestConsecutive(nums))
nums=[0,-1]
#EXPECTED: 2
print("TEST CASE 4: ", longestConsecutive(nums))


