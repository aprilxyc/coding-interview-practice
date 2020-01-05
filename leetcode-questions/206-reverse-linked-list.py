"""
Reverse a singly linked list.
"""
def reverseList(self, head: ListNode) -> ListNode:
    # iterative manner
    current = head
    prev = None
    while current is not None: # while there still exists a node after
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev