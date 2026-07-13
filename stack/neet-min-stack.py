# NeetCode Problem : [Min Stack]
# Difficulty: [Medium]
# Date: [07/13/2026]
# Time: [1h] - couldn't solve with O(1)
# Topic: [Stack]

## Intuition & Approach
# The Core Idea: Use stack to track the min.
## Complexity Analysis
# Time Complexity: O(N} for pop() but everything else is O(1)
# Why: We traverse list N times inside pop function.
# Space Complexity: O(N)
# Why: We store N elements in the stack.


# Code
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None or val < self.min:
            self.min = val
    
    def pop(self) -> None:
        if self.stack[-1] == self.min:
            if len(self.stack) == 1:
                self.min = None
            else:
                self.min = self.stack[0]
                for i in range(1, len(self.stack)-1):
                    if self.stack[i] < self.min:
                        self.min = self.stack[i]
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
    
# Solution - use two stacks
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
'''

# Solution 2 - Use single stack
'''
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
'''


if __name__ == "__main__":
    minStack = MinStack()
    ["MinStack", "push", 2147483646, "push", 2147483646, "push", 2147483647, "top", "pop", "getMin", "pop", "getMin", "pop", "push", 2147483647, "top", "getMin", "push", -2147483648, "top", "getMin", "pop", "getMin", "pop"]
    # Expected Output: [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647,null]
    print(minStack.push(2147483646))
    print(minStack.push(2147483646))
    print(minStack.push(2147483647))
    print(minStack.top()) # 2147483647
    print(minStack.pop())
    print(minStack.getMin()) # 2147483646
    print(minStack.pop())
    print(minStack.getMin()) # 2147483646
    print(minStack.pop())
    print(minStack.push(2147483647))
    print(minStack.top())
    print(minStack.getMin())
    print(minStack.push(-2147483648))
    print(minStack.top())
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
    print(minStack.pop())  

    