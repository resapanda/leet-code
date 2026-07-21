# NeetCode Problem : [Reverse Linked List]
# Difficulty: [Easy]
# Date: [07/21/2026]
# Time: [40m]
# Topic: [Linked List]

## Intuition & Approach
# The Core Idea: Track previous of each Node and return it as a new head.
## Complexity Analysis
# Time Complexity: O(N)
# Why: We traverse the list exactly one time.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.

# Code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        curr = head
        
        while curr is not None:
            next_node = curr.next
            curr.next = previous

            previous = curr
            curr = next_node
        
        return previous
        

if __name__ == "__main__":
    s = Solution()
    head1 = [0,1,2,3]
    print(f"Test 1 Result: {s.reverseList(head1)}")  # Expected Output: [3,2,1,0]

    head2 = []
    print(f"Test 2 Result: {s.reverseList(head2)}")  # Expected Output: []
