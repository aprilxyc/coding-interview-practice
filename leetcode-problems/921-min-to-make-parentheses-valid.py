class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        if S is None or not S:
            return 0
        
        # push into stack backwards
        stack = []
        
        for i in range(len(S) - 1, -1, -1):
            stack.append(S[i])
        
        opened = 0
        closed = 0
        b_count = 0
        
        while stack:
            item = stack.pop()
            if item == "(":
                opened += 1
            if item == ")" and opened == 0:
                b_count += 1
            if item == ")" and opened > 0:
                closed += 1
            if opened == closed:
                opened = 0
                closed = 0
        if opened > closed:
            b_count += (opened - closed)
        if closed and opened == 0:
            b_count += closed
        return b_count