"""
https://leetcode.com/problems/linked-list-cycle/
"""

# have two pointers but have a lag pointer that is slower and one that is faster
# if there is a cycle, eventually the fast one will catch up to the slow one and they will meet
# If there is no cycle, they will both reach the end of the list
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        
        fast = head.next
        slow = head
        while fast is not None and fast.next is not None and slow is not None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False