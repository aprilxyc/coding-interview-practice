"""
https://leetcode.com/problems/find-common-characters/
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        comparing_word = list(A[0])
        
        for word in range(1, len(A)):
            new_check = []
            for j in A[word]:
                if j in comparing_word:
                    new_check.append(j)
                    comparing_word.remove(j)
            comparing_word = new_check
        return comparing_word
       