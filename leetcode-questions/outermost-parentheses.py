"""
Leetcode problem #1021
Remove outermost parentheses
"""

# initial solution
def removeOuterParentheses(self, S):
output = ""
curr_composition = ""
bracket_check = []
for bracket in brackets: # O(N)
    if bracket = '(':
        bracket_check.append(bracket)
    else:
        bracket_check.pop()
    curr_composition += bracket
    if bracket_check == []:
        curr_composition = curr_composition[1:-1]
        output += curr_composition
        curr_composition = ""

# improved solution with less space
def removeOuterParenthesis(self, S):
    brackets = []
    left_pointer = 0
    right_pointer = 0
    j = 0
    for i in range(len(S)):
        if S[i] == '(':
            left_pointer += 1
        else:
            right_pointer += 1
        
    if left_pointer == right_pointer:
        brackets.append(S[j+1 : i])
        j = i + 1