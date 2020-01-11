"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# my initial solution that didn't work:
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:        
        while l1 != l2:
            if l1.val <= l2.val:
                temp = l1.next
                l1.next = l2
                l1 = temp
            else:
                temp = l2.next
                l2.next = l1
                l2 = temp
        return l1

# after learning it, this is the correct solution:
# https://www.youtube.com/watch?v=GfRQvf7MB3k&feature=emb_title
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:   
        # m = length of first list
        # n = length of second list
        # time complexity is O(m + n) where worst case we have to traverse the length of both of the lists
        # O(1) space because we only manipulate pointers  
        p1, p2 = l1, l2
        dummy = ListNode(-1) # point to this at the beginning
        cur = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1= p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        
        if p2: # if p2 still exists
            cur.next = p2
        if p1:
            cur.next = p1
     
        return dummy.next