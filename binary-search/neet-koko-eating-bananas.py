# NeetCode Problem : [Koko Eating Bananas]
# Difficulty: [Medium]
# Date: [08/07/2026]
# Time: [1h6m] couldn't solve
# Topic: [Binary Search]

## Intuition & Approach
# The Core Idea: 
## Complexity Analysis
# Time Complexity: 
# Why: 
# Space Complexity: 
# Why: 

# Code
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if len(piles) == h:
            largest = 0
            for pile in piles:
                largest = max(largest, pile)
            return largest
        else:
            piles = sorted(piles)
            temp = 0
            for i in range(len(piles) - 1):
                for pile in piles:
                    temp += round(pile/piles[i])
                if temp < h:
                    return piles[i]
                temp = 0

# Solution 
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
'''

if __name__ == "__main__":
    s = Solution()
    piles1 = [1,4,3,2]
    h1 = 9
    print(f"Test 1 Result: {s.minEatingSpeed(piles1, h1)}") # Expected Output: 2

    piles2 = [25,10,23,4]
    h2 = 4
    print(f"Test 2 Result: {s.minEatingSpeed(piles2, h2)}") # Expected Output: 25

    piles3 = [3,6,7,11]
    h3 = 8
    print(f"Test 3 Result: {s.minEatingSpeed(piles3, h3)}") # Expected Output: 4

    h = 6
    [4, 11, 20, 23, 30] # 23
    

