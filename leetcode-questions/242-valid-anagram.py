"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""

#1 sort it and see if they are identical
#2 put letters into hash table and see if they are the same frequency

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st method is to simply sort it and see if they're the same 
        # 2nd method: hash table and see if they are the same frequency
        if len(s) != len(t):
            return False

        freq_dict = {}
        
        for i in s:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        
        for j in t:
            if j not in freq_dict:
                return False
            else:
                freq_dict[j] -= 1
        
        for val in freq_dict.values():
            if val != 0:
                return False
            
        return True

# can also use a counting sort method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for ch1, ch2 in zip(s, t):
            count[ord(ch1)-ord('a')] += 1 
            count[ord(ch2)-ord('a')] -= 1
        return not any(count)
            