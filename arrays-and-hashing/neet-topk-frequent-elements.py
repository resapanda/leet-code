# NeetCode Problem : [Top K Frequent Elements]
# Difficulty: [Medium]
# Date: [07/14/2026]
# Time: [1h30m] - couldn't solve with O(N)
# Topic: [Array & Hashing]

## Intuition & Approach
# The Core Idea: Use stack to track the min.
## Complexity Analysis
# Time Complexity: O(N} for pop() but everything else is O(1)
# Why: We traverse list N times inside pop function.
# Space Complexity: O(N)
# Why: We store N elements in the stack.


# Code
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_arr = [[] for _ in range(len(nums) + 1)]

        for i, inner_list in enumerate(num_arr):
            if nums[i] in inner_list:
                idx = num_arr.index(nums[i])
                num_arr[idx + 1].append(nums[i])
                num_arr[idx].remove(nums[i])
            else:
                num_arr[0].append(nums[i])
        
        res = []
        idx = len(num_arr) - 1
        while 0 < k:
            if not num_arr:
                return res
            if num_arr[idx]:
                val = num_arr[idx].pop()
                res.append(val)
                k -= 1
            else:
                idx -= 1
        
        return res


if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,2,3,3,3]
    k1 = 2
    print(f"Test 1 Result: {s.topKFrequent(nums1, k1)}")  # Expected Output: [2, 3]

    nums2 = [7,7]
    k2 = 1
    print(f"Test 2 Result: {s.topKFrequent(nums2, k2)}")  # Expected Output: [7]