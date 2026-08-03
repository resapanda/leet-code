# NeetCode Problem : [Invert Binary Tree]
# Difficulty: [Easy]
# Date: [08/03/2026]
# Time: [1h9m]
# Topic: [Tree]

## Intuition & Approach
# The Core Idea: Recursivly invert left subtree and right subtree.
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
            
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


if __name__ == "__main__":
    s = Solution()
    root = [1,2,3,4,5,6,7]
    print(f"Test 1 Result: {s.invertTree(root)}") # Expected Output: [1,3,2,7,6,5,4]