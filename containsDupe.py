class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        checked_list = []
        for num in nums:
            if num in checked_list:
                return True
            checked_list.append(num)
            
        return False
    

