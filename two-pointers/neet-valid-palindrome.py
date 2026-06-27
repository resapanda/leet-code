# NeetCode Problem : [Valid Palindrome]
# Difficulty: [Easy]
# Date: [06/27/2026]
# Time: [38m]
# Topic: [Two Pointers]

## Intuition & Approach
# The Core Idea: Check characters from both left and right side and compare. Ignor unique characters and space using isalnum().
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the string of size N exactly once.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.

# Code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            # we need while loop here cuz we need to keep traversing until we find next valid character
            # isalnum() checks if the character is a-z or 0-9
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
    
    '''
    first attempt - check each character using ascii number, I could have created a helper function like the solution
    while left < right:
    if (48 > ord(s[left]) or ord(s[left]) > 57) and (97 > ord(s[left]) or ord(s[left]) > 122):
        left += 1
    if (48 > ord(s[right]) or ord(s[right]) > 57) and (97 > ord(s[right]) or ord(s[right]) > 122):
        right -= 1
    if s[left] != s[right]:
        return False
    '''
    
# Solution
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
'''

if __name__ == "__main__":
    s = Solution()
    strs1 = "Was it a car or a cat I saw?"
    print(f"Test 1 Result: {s.isPalindrome(strs1)}")  # Expected Output: true

    strs2 = "tab a cat"
    print(f"Test 2 Result: {s.isPalindrome(strs2)}")  # Expected Output: false

    strs3 = ".,"
    print(f"Test 3 Result: {s.isPalindrome(strs3)}")  # Expected Output: true