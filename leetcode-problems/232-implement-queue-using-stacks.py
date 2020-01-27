"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""

# a very bad first implementation 27/01
# space is O(N)
# time complexity stays constant and is O(1) amortised
# we look at the overarching algorithm's worst case
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # simply push the element to the push stack
        self.push_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        if self.empty():
            return None
        
        if len(self.pop_stack) == 0: # if the pop stack is empty, check the push stack
            while self.push_stack:
                item = self.push_stack.pop()
                self.pop_stack.append(item)
        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None 
        
        if len(self.pop_stack) == 0:
            while self.push_stack:
                item = self.push_stack.pop()
                self.pop_stack.append(item)
        return self.pop_stack[-1]
 

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.pop_stack) == 0 and len(self.push_stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()