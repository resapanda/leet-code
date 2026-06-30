# NeetCode Problem : [Binary Search]
# Difficulty: [Easy]
# Date: [06/29/2026]
# Time: [1h30m couldn't solve completely 13/18]
# Topic: [Binary Search]

## Intuition & Approach
# The Core Idea: Apply binary search to look for the target.
## Complexity Analysis
# Time Complexity: O(logN)
# Why: Binary search allows us to cut the search area in half.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.


# Code - previous messy solution is in neetcode
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
            
        return -1

# Solution
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
'''

if __name__ == "__main__":
    s = Solution()
    nums1 = [-1,0,2,4,6,8]
    target1 = 4
    print(f"Test 1 Result: {s.search(nums1, target1)}")  # Expected Output: 3

    nums2 = [-1,0,2,4,6,8]
    target2 = 3
    print(f"Test 2 Result: {s.search(nums2, target2)}")  # Expected Output: -1

    nums3 = [-1,0,3,5,9,12]
    target3 = 9
    print(f"Test 3 Result: {s.search(nums3, target3)}")  # Expected Output: 4

    nums4 = [-1,0,3,5,9,12]
    target4 = 12
    print(f"Test 4 Result: {s.search(nums4, target4)}")  # Expected Output: 5
