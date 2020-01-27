"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""
# my solution
class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        if len(S) == 1:
            return S
        
        stack = []
        stack.append(S[0])
        
        for i in range(1, len(S)):
            if stack:
                popped_item = stack.pop()
                if S[i] != popped_item:
                    stack.append(popped_item)
                    stack.append(S[i])
            else:
                stack.append(S[i])
        return "".join([i for i in stack])

# we can do this to avoid premature popping
def removeDuplicates(self, S):
    res = []
    for c in S:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
    return "".join(res)

# two pointer method from discussions
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294964/JavaPython-3-three-easy-iterative-codes-w-brief-explanation-and-analysis.
 def removeDuplicates(self, S: str) -> str:
        end, a = -1, list(S)
        for c in a:
            if end >= 0 and a[end] == c:
                end -= 1
            else:
                end += 1
                a[end] = c
        return ''.join(a[: end + 1])

# my solution 27/01
class Solution:
    def removeDuplicates(self, S: str) -> str: # abbaca
        
        if len(S) == 0:
            return None
        if len(S) == 1:
            return S
        
        stack = []
        
        stack.append(S[0]) # stack = [ca]
        
        for i in range(1, len(S)): # going through . if b == a
            if stack:
                if S[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(S[i])
            else:
                stack.append(S[i])
        # convert stack back to a string
        return "".join(stack)
        