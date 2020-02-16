"""
https://leetcode.com/problems/permutation-in-string/
"""

# got excited since I only just learned how to write permutations of string recursively before so rushed it and didn't use the right data structure :(

# below is my initial solution
# class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # total complexity is O(N!)
        
        if not s1 or not s2:
            return False
        
        if s1 == None or s2 == False:
            return False
        
        possiblePermutations = self.getPermutation(s1)
        
        
        # checking the list is O(N^2)
        # go through list of possible permutations. If word exists, then it is true
        for word in possiblePermutations:
            if word in s2:
                return True
        return False
        
        
    # get the permutation of the first string
    # getting the permutations of O(N!)
    def getPermutation(self, word):
        result = []

        if len(word) <= 1:
            return word

        perms = self.getPermutation(word[1:])
        char = word[0]

        for perm in perms:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])
        return result)

# faster than 5% of submissions --> need to optimise
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if not s1 or not s2:
            return 0
        
        s1_map = {}
        for i in s1:
            s1_map[i] = s1_map.get(i, 0) + 1

        s2_map = {}

        s1_len = len(s1)
        j = 0
        i = 0
        while j <= len(s2) - s1_len:
            for i in range(j, j + s1_len):
                s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
            if s1_map.items() == s2_map.items():
                return True
            j += 1
            s2_map = {}
        return False