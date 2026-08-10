# NeetCode Problem : [Evaluate Reverse Polish Notation]
# Difficulty: [Medium]
# Date: [08/10/2026]
# Time: [1h10m]
# Topic: [Stack]

## Intuition & Approach
# The Core Idea: Use stack to store numbers while traversing the list. When an operator appears,
#                pop 2 numbers and calculate the result, and push it to the stack.
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the list exactly once.
# Space Complexity: O(N)
# Why: We create a stack to store numbers and the result.


# Code
import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {'+' : operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        res_stack = []

        if not tokens:
            return None
        
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token in ops:
                op = ops[token]
                int2 = int(res_stack.pop())
                int1 = int(res_stack.pop())
                res_stack.append(op(int1, int2))
            else:
                res_stack.append(token)
        return int(res_stack[0])
                
# Solution
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack.pop()
'''

if __name__ == "__main__":
    s = Solution()
    tokens1 = ["0","3","/"]
    print(f"Test 1 Result: {s.evalRPN(tokens1)}")  # Expected Output: 6
