"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        print(f'input={num}')

        digits = sorted([int(c) for c in str(num)], reverse=True)
        #sort the digits from highest to lowest
        highest_num = digits[0]
        #create hashmap to track indices of nums
        hashmap = {int(digit):index for index,digit in enumerate(str(num))}
        num_list = list(str(num))
        for idx, num in enumerate(num_list):
            #check if larger digit appears later
            for j in range(9, int(num), -1):  
                if int(num)<highest_num and hashmap[highest_num]>idx:
                    #swap
                    temp = num
                    num_list[idx] = str(highest_num)
                    high_num_idx = hashmap[highest_num]
                    num_list[high_num_idx] = temp
                    break
        
        print(num_list)
        return int("".join(num_list))




# sol = Solution()

# sol.maximumSwap(num=2736)


grades = ["A", "A", "A-", "B-", "B-", "C+", "B", "C", "B+", "B-", "B"]
hashmap = {"A": 4, "A-": 3.67, "B+":3.33, "B":3, "B-":2.67, "C+":2.33, "C":2}

avg = 0

for grade in grades:
    grade = grade.upper()
    avg+=hashmap[grade]

print(avg/len(grades))