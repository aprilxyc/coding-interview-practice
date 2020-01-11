class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(N) time complexity where N is the number of elements in S
        # O(1) space
        L, R = 0, len(s) - 1
        
        while L < R:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            else:
                if s[L].upper() != s[R].upper():
                    return False
                L += 1
                R -= 1
        return True

# can also do it so that you simply join the letters together (condition where it isalnum) and then just check whether it is equal to its reverse
# This is faster but takes up more space
def validpalindrome(s):
        s = ''.join(ch.lower() for ch in s if ch.isalpha() or ch.isdigit())
        return s == s[::-1]
        #space: O(N)