from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            res = numbers[l] + numbers[r]

            if res > target:
                r -= 1
            elif res < target:
                l += 1
            else:
                return [l + 1, r + 1]  # Return 1-based indices

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        sol = Solution()
        
        # Test case 1
        nums = [1, 2, 3, 4, 5, 8, 10, 14]
        target = 13
        expected_output = [3, 7]  # 3rd (3) and 7th (10) indices add up to 13
        self.assertEqual(sol.twoSum(nums, target), expected_output)
        
        # # Additional test cases for more coverage
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [1, 2])  # 1-based indices
        self.assertEqual(sol.twoSum([1, 3, 4, 5, 6], 9), [2, 5])
        # self.assertEqual(sol.twoSum([5, 25, 75], 100), [2, 3])

# To run the tests
if __name__ == "__main__":
    unittest.main()
