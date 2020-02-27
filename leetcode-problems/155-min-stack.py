"""
https://leetcode.com/problems/min-stack/
"""

# you can do it with one stack but takes up more space
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # initialise the stack

    def push(self, x: int) -> None:
        curr_min = self.getMin()
        if curr_min == None or x < curr_min:
            curr_min = x
        self.stack.append((x, curr_min))
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop() # remove the element off the stack
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            # get the minimum 
            return self.stack[-1][1]


# or you can do it two stacks with optimised space
# my atrocious solution 27/01
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:   
        current_min = self.getMin()
        
        # if the main stack if empty
        if len(self.main_stack) == 0:
            self.main_stack.append(x)
            # this will have to be the minimum
            current_min = x
            self.min_stack.append([x, 1])
        else:
            if x < current_min:
                current_min = x
                self.main_stack.append(x)
                self.min_stack.append([x, 1])
            elif x == self.min_stack[-1][0]:
                self.main_stack.append(x)
                self.min_stack[-1][1] += 1 # increment the counter
            else:
                self.main_stack.append(x)

    def pop(self) -> None:
        # if the stack is empty and you cannot pop it
        if len(self.main_stack) == 0:
            return None
        else:
            min_value = self.main_stack.pop()
            if min_value == self.min_stack[-1][0]:
                if self.min_stack[-1][1] == 1:
                    self.min_stack.pop()
                else: # otherwise, there are multiple occurrences
                    self.min_stack[-1][1] -= 1 # decrement the occurrence
                
    def top(self) -> int:
        if len(self.main_stack) == 0:
            return None
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        if len(self.main_stack) == 0:
            return None
        return self.min_stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# I redid this again and managed to do this:
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min_stack = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min_stack: 
            self.min_stack.append([x, 1])
        else:
            if x < self.min_stack[-1][0]:
                self.min_stack.append([x, 1])
            else:
                self.min_stack[-1][1] += 1
                
    def pop(self) -> None:
        if self.items:
            popped_item = self.items.pop()
            if self.min_stack[-1][1] == 1:
                popped_min = self.min_stack.pop()
            else:
                self.min_stack[-1][1] -= 1
            return popped_item
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()