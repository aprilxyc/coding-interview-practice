class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        store_bracket = ""
        stack = []
        
        if len(S) == 0:
            return None
        
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
            store_bracket += i
        
            if not stack:
                result += store_bracket[1:-1]
                store_bracket= ""
        return result

# a cool method but O(N^2) because concatenating strings is technically O(N^2) in Python
# since it requires you to copy string over again
def removeOuterParentheses(S):
    count = 0
    result = ""
    for c in S:
        if c == ')':
            count -= 1
        if count != 0:
            result += c
        if c == '(':
            count += 1
    return result

# redid 27/01
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        string_basket = ""
        stack = []
        result = ""
        
        for i in S:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
            string_basket += i
            
            if not stack:
                result += string_basket[1:-1]
                string_basket = ""
        return result
    