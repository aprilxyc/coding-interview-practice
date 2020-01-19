"""
Write code to remove duplicates from an unsorted linked list.
"""

LinkedList = [1, 3, 2, 3, 4]

def removeDupes(head):
    prev = None
    curr = head

    # in linked list, we get access to the head
    freq_dict = {}
    if curr.val not in freq_dict:
        freq_dict[curr.val] = 1
        prev = curr
    else:
        prev.next = curr.next
    curr = curr.next

# method that doesn't use temporary buffer

