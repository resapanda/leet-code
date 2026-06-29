# NeetCode Problem : [Best Time to Buy and Sell Stock]
# Difficulty: [Easy]
# Date: [06/27/2026]
# Time: [1h9m couldn't solve completely]
# Topic: [Sliding Window]

## Intuition & Approach
# The Core Idea: Use two pointers to keep track of the largest profit.
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the list of size N exactly once.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.

# Code
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 1
        largest = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                temp = prices[sell] - prices[buy]
                largest = max(largest, temp)
            else:
                buy = sell
            sell += 1
        return largest

if __name__ == "__main__":
    s = Solution()
    prices1 = [10,1,5,6,7,1]
    print(f"Test 1 Result: {s.maxProfit(prices1)}")  # Expected Output: 6

    prices2 = [10,8,7,5,2]
    print(f"Test 2 Result: {s.maxProfit(prices2)}")  # Expected Output: 0

    prices3=[5,1,5,6,7,1,10]
    print(f"Test 3 Result: {s.maxProfit(prices3)}")  # Expected Output: 9

    prices4=[2,1,2,1,0,1,2]
    print(f"Test 4 Result: {s.maxProfit(prices4)}")  # Expected Output: 2
