class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        d = {}
        count = 0
        
        for i in s:
            d[i] = d.get(i, 0) + 1 # create the dictionary
        
        l=list(d.keys())
        
        for i in l:
            if d[i] % 2 == 0:
                count += d[i]
                del(d[i])
            else:
                count += d[i] - 1
                d[i] = 1
        
        if d:
            return count + 1
        return count
        
        