# NeetCode Problem #0002: [Valid Anagram]
# Difficulty: [Easy]
# Date: [06/18/2026]
# Time: [12m]
# Topic: [Array & Hashing]

## Intuition & Approach
# The Core Idea: sort both input strings and compare if they are same or not. 
## Complexity Analysis
# Time Complexity: O(N log N + M log M)
# Why: We use sroted() for both strings and the worst case of sort time complexity is n log n.
# Space Complexity: O(N + M)
# Why: sorted() create a new list for s and t.

# sorted() - create a new list of sorted strings
# .sort() - change the original list itself


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

# Solution1 (using sort but no for loop)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
'''

# Solution2 (Using array) can save time and space
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        countt = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            countt[ord(c) - ord('a')] += 1

        return counts == countt
'''

if __name__ == "__main__":
    s = Solution()
    s1 = "racecar"
    t1 = "carrace"
    print(f"Test 1 Result: {s.isAnagram(s1, t1)}")  # Expected Output: true

    s2 = "jar"
    t2 = "jam"
    print(f"Test 2 Result: {s.isAnagram(s2, t2)}")  # Expected Output: false
