# NeetCode Problem : [Maximum Depth of Binary Tree]
# Difficulty: [Easy]
# Date: [08/03/2026]
# Time: [1h] couldn't solve
# Topic: [Tree]

## Intuition & Approach
# The Core Idea: Recursively traverse the left and right subtrees in postorder, calculate their maximum depths, and return 1 plus the larger depth.
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse each node exactly one time.
# Space Complexity: O(N)
# Why: In the worst case, call stack grows the height of the tree.

# Code
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        rightDepth = 0   
        leftDepth = 0
        if root.left is not None:
            leftDepth += 1
        self.maxDepth(root.left)
        
        rightDepth = leftDepth
        if root.right is not None:
            rightDepth += 1
        self.maxDepth(root.right)
        
        return 1 + max(leftDepth, rightDepth)

# Solution
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
'''
'''
left_depth = self.maxDepth(root.left)
right_depth = self.maxDepth(root.right)

current_depth = 1 + max(left_depth, right_depth)
return current_depth
'''

if __name__ == "__main__":
    s = Solution()
    root = [1,2,3,None,None,4]
    print(f"Test 1 Result: {s.maxDepth(root)}") # Expected Output: 3
