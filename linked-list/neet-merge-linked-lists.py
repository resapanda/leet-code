# NeetCode Problem : [Merge Two Sorted Linked Lists]
# Difficulty: [Easy]
# Date: [07/21/2026]
# Time: [52m]
# Topic: [Linked List]

## Intuition & Approach
# The Core Idea: Compare two linked list and point to the list that has lower value.
## Complexity Analysis
# Time Complexity: O(N + M)
# Why: We traverse 2 lists exactly one time.
# Space Complexity: O(1)
# Why: No extra data structure grows with the input size.

# Code
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        start = None
        curr = None

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                if start is None and curr is None:
                    start = list2
                    curr = list2
                else:
                    curr.next = list2
                    curr = list2
                list2 = list2.next
            else:
                if start is None and curr is None:
                    start = list1
                    curr = list1
                else:
                    curr.next = list1
                    curr = list1
                list1 = list1.next

        if list1 is None:
            while list2 is not None:
                if start is None and curr is None:
                    start = list2
                    curr = list2
                else:
                    curr.next = list2
                    curr = list2
                list2 = list2.next
        elif list2 is None:
            while list1 is not None:
                if start is None and curr is None:
                    start = list1
                    curr = list1
                else:
                    curr.next = list1
                    curr = list1
                list1 = list1.next

        return start

# Solution
'''
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
'''

if __name__ == "__main__":
    s = Solution()
    list1 = [1,2,4]
    list2 = [1,3,5]
    print(f"Test 1 Result: {s.mergeTwoLists(list1, list2)}")  # Expected Output: [1,1,2,3,4,5]