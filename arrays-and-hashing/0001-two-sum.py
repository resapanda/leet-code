# LeetCode Problem #0001: [Two Sum]
# Difficulty: [Easy]
# Date: [05/31/2026]
# Time: [1hr+]
# Topic: [Array]

## Intuition & Approach
# The Core Idea: create a hashmap from array values to indices. Iterate the array and look up the compliment in the hashmap.

## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the array of size N exactly once.
# Space Complexity: O(N)
# Why: In the worst case, we store all N elements in the hash map.

## Code
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash and hash[comp] != i:
                return [i, hash[comp]]
            
## Solution
"""
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i
"""


if __name__ == "__main__":
    s = Solution()
    
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1 Result: {s.twoSum(nums1, target1)}")  # Expected Output: [0, 1] or [1, 0]

    nums2 = [3,2,4]
    target2 = 6
    print(f"Test 2 Result: {s.twoSum(nums2, target2)}")  # Expected Output: [1, 2] or [2, 1]