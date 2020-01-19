"""
 https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head