"""

"""

# Before writing any code, it's good to make a list of edge cases that we need to consider. This is so that we can be certain that we're not overlooking anything while coming up with our algorithm, and that we're testing all special cases when we're ready to test. These are the edge cases that I came up with.

# The linked list is empty, i.e. the head node is None.
# Multiple nodes with the target value in a row.
# The head node has the target value.
# The head node, and any number of nodes immediately after it have the target value.
# All of the nodes have the target value.
# The last node has the target value.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_node = ListNode(-1)    
        dummy_node.next = head
        
        curr = dummy_node
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_node.next