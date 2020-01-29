"""
"""

# my solution using bit manipulation
if len(s) == 0 and len(t) == 0:
    return None
new_string = s + t
result = 0
for i in new_string:
    i = ord(i) 
    result ^= i
return chr(result)


# dictionary solution
def findTheDifference(self, s: str, t: str) -> str:
    
    word_dict = {}
    for letter in s:
        word_dict[letter] = word_dict.get(letter, 0) + 1
    
    for letter in t:
        if word_dict.get(letter, 0) == 0:
            return letter
        else:
            word_dict[letter] -= 1
    
    
    dic = {}
    for ch in s:
        dic[ch] = dic.get(ch, 0) + 1
    for ch in t:
        if dic.get(ch, 0) == 0:
            return ch
        else:
            dic[ch] -= 1

# THINK OF THE EDGE CASES SUCH AS "A", "AA"
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        word_dict = {}
        for letter in s:
            word_dict[letter] = word_dict.get(letter, 0) + 1
        
        for letter in t:
            if word_dict.get(letter, 0) == 0:
                return letter
            else:
                word_dict[letter] -= 1 # this is to account for duplicates e.g. "a" and "aa"
                
        
                