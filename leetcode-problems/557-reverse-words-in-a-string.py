"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # turn the string into a list
        s = [i for i in s]
        
        start, end = 0, 0
        while end < len(s): 
            while s[end] != " " and end != len(s) - 1:
                end += 1
            
            # set end to the letter right before the space
            if end == len(s) - 1:
                right = len(s) - 1
            else:
                right = end - 1
            left = start
            # swap them
            while left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            start = end + 1
            end = end + 1
        
        return "".join([i for i in s])
        

        """
        1. Turn it into a list You have to reverse the letters by swapping
        2. If you encounter any punctutation, then you need to also swap it
        3. If you encounter a whitespace, then you simply add it in and continue

        Let's take Leetcode contest
        [L, e, t, ', s,  , t, a, k, e,  , L, e, e, t, ]
        
        
        """

# faster solutions but not O(1) space
def reverseWords(self, s):
    s = s.split()
    for i in range(0, len(s)):
        # reversing the entire word
        s[i] = s[i][::-1]
    return " ".join(s)