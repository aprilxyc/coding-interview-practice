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