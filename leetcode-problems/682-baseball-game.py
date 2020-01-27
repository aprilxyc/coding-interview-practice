"""
https://leetcode.com/problems/baseball-game/
"""

# my solution
# note that isdigit() does not work for negatives so you need to lstrip it first
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # O(N) where N is the number recordings in the baseball game point recorder
        # O(N) space where N is the number of recordings in the baseball game point recorder because we need to make a new list (stack)
        stack = []
        for i in ops:
            if i.isdigit() or i.lstrip('-').isdigit(): # if it is a number, then simply add it up
                stack.append(int(i))
            elif i == 'C':
                if stack: # accounts for popping an empty stack
                    stack.pop() # remove the most recent round's points
            elif i == '+':
                # get the sum of the last two
                new_points = int(stack[-1]) + int(stack[-2])
                stack.append(new_points)
            else:
                # if D, then double the last round's points
                last_round = stack[-1]
                stack.append(2 * int(last_round))
        print(stack)
        return sum(stack)