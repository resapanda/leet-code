# NeetCode Problem : [Two Integer Sum II]
# Difficulty: [Medium]
# Date: [07/09/2026]
# Time: [7m]
# Topic: [Two Pointers]

## Intuition & Approach
# The Core Idea: Use two pointers to traverse the array.
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the array of size N exactly once.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.


# Code
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

# Solution - it's almost same as mine
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
'''

if __name__ == "__main__":
    s = Solution()
    numbers1 = [1,2,3,4]
    target1 = 3
    print(f"Test 1 Result: {s.twoSum(numbers1, target1)}")  # Expected Output: [1,2]