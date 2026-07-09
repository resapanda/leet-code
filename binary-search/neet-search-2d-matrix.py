# NeetCode Problem : [Search a 2D Matrix]
# Difficulty: [Medium]
# Date: [07/09/2026]
# Time: [22m]
# Topic: [Binary Search]

## Intuition & Approach
# The Core Idea: Use binary search to find the row that might contain target and use another binary search to find the target in the row.
## Complexity Analysis
# Time Complexity: O(log N + log M) -> O(log N * log M)
# Why: We use binary search two times for detecting row and finding target inside the row.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.


# Code
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = l + ((r - l) // 2)
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            elif matrix[mid][0] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


# Solution
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
'''


if __name__ == "__main__":
    s = Solution()
    matrix1 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target1 = 10
    print(f"Test 1 Result: {s.searchMatrix(matrix1, target1)}")  # Expected Output: true

    matrix2 = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target2 = 15
    print(f"Test 2 Result: {s.searchMatrix(matrix2, target2)}")  # Expected Output: false