class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(S, step, curr, res):
            # already go through the entire string, S
            if step == len(S):
                res.append(curr)
                return
            
            # not alphabets => one backtrack case
            if S[step].lower() == S[step].upper():
                backtrack(S, step+1, curr+S[step], res)
            
            # having upper and lower letters => two backtrack cases
            else:
                backtrack(S, step+1, curr+S[step].lower(), res)
                backtrack(S, step+1, curr+S[step].upper(), res)
        
        res = []
        backtrack(S, 0, "", res)
        return res