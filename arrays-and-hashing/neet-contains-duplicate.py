# NeetCode Problem #0001: [Contains Duplicate]
# Difficulty: [Easy]
# Date: [06/18/2026]
# Time: [10m]
# Topic: [Array & Hashing]

## Intuition & Approach
# The Core Idea: create a hashset from array values. Iterate the array and look up the duplicate in the hashset.

## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the array of size N exactly once.
# Space Complexity: O(N)
# Why: In the worst case, we store all N elements in the hash set.

## Code
class Solution(object):
    def hasDuplicate(self, nums: list[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 3]
    print(f"Test 1 Result: {s.hasDuplicate(nums1)}")  # Expected Output: true

    nums2 = [1, 2, 3, 4]
    print(f"Test 2 Result: {s.hasDuplicate(nums2)}")  # Expected Output: false
