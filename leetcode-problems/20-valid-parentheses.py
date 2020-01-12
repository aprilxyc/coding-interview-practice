"""
https://leetcode.com/problems/valid-parentheses/
"""
# my first attempt at a solution
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "([{"
        closed_brackets = ")]}"
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                
                # if it is empty, you cannot pop anything
                if len(stack) == 0:
                    return False
                
                current_bracket = stack[-1]
                if open_brackets.index(current_bracket) == closed_brackets.index(i):
                    stack.pop()
                else:
                    return False
                
        if len(stack) != 0:
            return False
        return True

# you can also use a dictionary to keep the bracket pairs
# https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []