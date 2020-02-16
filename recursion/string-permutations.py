"""
Write a recursive function for generating all permutations of an input string. Return them as a set.

Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.
"""

def permutations(word):
    if len(word) <= 1:
        return [word]

    # get the permutations of N - 1
    perms = permutations(word[1:])
    # the first letter of the word before
    char = word[0]
    result = []

    for perm in perms:
        # iterate through the letters and make the permutations
        for i in range(0, len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result

# redo this backtracking question
# for a given list
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)