# NeetCode Problem : [Linked List Cycle Detection]
# Difficulty: [Easy]
# Date: [11/09/2026]
# Time: [30m]
# Topic: [Linked List]

## Intuition & Approach
# The Core Idea: Create a set and add visited node and iterate the linked list.
## Complexity Analysis
# Time Complexity: O(N)
# Why: we iterate the linked list exactly once until we find a loop.
# Space Complexity: O(N)
# Why: visited is a data structure that stores at most n nodes.

# Code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next              

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head is not None:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return True
        return False
    
# different solution - using two pointers (Floyd's Cycle Detection Algorithm)
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
'''


# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle: index = 1
node4.next = node2

# Test
sol = Solution()
print(sol.hasCycle(node1))  # True

