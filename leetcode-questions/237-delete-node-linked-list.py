"""
te a function to delete a node (except the tail) in a singly linked list, given only access to that node.
"""

def deleteNode(node):
    current = node
    current.val = current.next.val
    current.next = current.next.next
    