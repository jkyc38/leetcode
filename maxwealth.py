from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0 
      
        for person in accounts:
            money = 0
            for wealth in person:
                money+=wealth
                maxWealth= max(maxWealth, money)

        return maxWealth