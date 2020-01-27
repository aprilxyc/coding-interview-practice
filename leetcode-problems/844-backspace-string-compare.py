"""
https://leetcode.com/problems/backspace-string-compare/
"""
# my first attempt at a solution
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # O(S+T) where S is num of elements in S and T is number of elements in T
        
        stack1 = []
        stack2 = []
        for i in S:
            if i.isalpha():
                stack1.append(i)
            elif stack1 and i == '#':
                stack1.pop()
        
        for i in T:
            if i.isalpha():
                stack2.append(i)
            elif stack2 and i == '#':
                stack2.pop()
        
        if stack1 == stack2:
            return True
        return False

# try to learn the second solution with two pointers
        
        