"""
Reverse a singly linked list.
"""
def reverseList(self, head: ListNode) -> ListNode:
    # iterative manner
    # O(N) time but constant space
    current = head
    prev = None
    while current is not None: # while there still exists a node after
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

# recursive manner
# O(N) time because it touches N nodes but ON() space because it creates an O(N) recursive stack
def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    if curr is None:
        return None
    elif curr.next is None:
        return curr
    else:
        next_node = curr.next
        curr.next = None
        rest = self.reverseList(next_node)
        next_node.next = curr
    return rest
    