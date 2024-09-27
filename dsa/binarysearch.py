
def search(nums: list[int], target: int) -> int:

    left = 0
    right = len(nums)-1
    mid = int((left+right)/2)
    
    if target not in nums:
        return -1
    
    #check if target is less than or greater than mid
    #update left or right pointer to the mid according to it
    #repeat until you find the target
    while nums[mid]!=target:
        
        if target < nums[mid]:
            right = mid-1
            
        else:
            left = mid+1
        
        mid = int((right+left)/2)

    
    return mid

def findMin(nums) -> int:
    
    pass

# print(int(2.5))