# NeetCode Problem : [Valid Parentheses]
# Difficulty: [Easy]
# Date: [06/29/2026]
# Time: [30m]
# Topic: [Stack]

## Intuition & Approach
# The Core Idea: Use stack to store opening brackets and when closing brackets appears, check if the latest opening brackets and the closing brackets are correct matching pair. 
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the string of size N exactly once.
# Space Complexity: O(N)
# Why: the worst case we need to store all opening brackets to the stack.


# Code
class Solution:
    def isValid(self, s: str) -> bool:
        # if str is odd length -> false
        if len(s) % 2 == 1:
            return False
        
        parentheses = {'(':')', '{':'}', '[':']'}
        keys = ['(', '{', '[']
    
        stack = []
        for i in range(len(s)):
            if s[i] in keys:
                stack.append(s[i])
            elif not stack:
                return False
            else:
                temp = stack.pop()
                if s[i] != parentheses.get(temp):
                    return False
        if stack:
            return False
        
        return True

# Solution
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
'''

if __name__ == "__main__":
    s = Solution()
    s1="(("
    print(f"Test 1 Result: {s.isValid(s1)}")  # Expected Output: false

    s2 = "[[[]"
    print(f"Test 2 Result: {s.isValid(s2)}")  # Expected Output: false

    s3 = "[(])"
    print(f"Test 3 Result: {s.isValid(s3)}")  # Expected Output: false

    s4 = "()[]{}"
    print(f"Test 4 Result: {s.isValid(s4)}")  # Expected Output: true