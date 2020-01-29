"""
https://leetcode.com/problems/unique-number-of-occurrences/
"""

# my original code:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        if len(arr) == 0:
            return None
        
        freq_dict = {}
        for i in arr:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        freq_list = []
        for key, value in freq_dict.items():
            freq_list.append(value)
    
        if len(set(freq_list)) == len(freq_list):
            return True
        return False

# took me forever cos i'm still bad at this
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_list = []
        for i in set(arr[::]): # note I overcomplicated here because you can do set() on an array and it does not change anything - the array is not mutated
            count = arr.count(i)
            if count not in freq_list:
                freq_list.append(count)
            else:
                return False
        return True

# better solution:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l = []
        for i in set(arr):
            count = arr.count(i)
        if not count in l:
            l += [count]
        else:
            return False
        return True
    