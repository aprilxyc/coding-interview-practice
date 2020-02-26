"""
Write a recursive function for generating all permutations of an input string. Return them as a set.

Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.
"""

def permutations(word):
    if len(word) <= 1:
        return [word]
ƒ
    # get the permutations of N - 1
    perms = permutations(word[1:])
    # the first letter of the word before
    char = word[0]
    result = []

    for perm in perms:
        # iterate through the letters and make the permutations
        for i in range(0, len(perm) + 1):
            # know that this only works for strings of the length of the input
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

    # how to change this to make it work?
    class Solution:
def numTilePossibilities(self, tiles: str) -> int:
    # 1. create the permutations
    # 2. keep getting the permutations then loop over the possible permutations by slicing it
    # base case: if len(path) == len(tiles) then we append this and know it has hit the end
        
    if len(tiles) == 0 or tiles is None:
        return 0
    
    if len(tiles) <= 1:
        return [tiles]
    else:
        char = tiles[0]
        next_tile = tiles[1:]
        result = []
        
        possibilities = self.numTilePossibilities(next_tile)
        
        for possibility in possibilities:
            for i in range(len(possibility) + 1):
                result.append(possibility[:i] + char + possibility[i:])
    
    print(result)
    return (result)

# improved (optimised for strings and not lists)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # 1. create the permutations
        # 2. keep getting the permutations then loop over the possible permutations by slicing it
        # base case: if len(path) == len(tiles) then we append this and know it has hit the end
            
        path = ""
        result = set()
        nums = self.numTilePossibilitiesHelper(path, tiles, result)
        return len(nums)
        
    def numTilePossibilitiesHelper(self, path, tiles, result):

        if path:
            result.add(path)
        for i in range(len(tiles)):
            self.numTilePossibilitiesHelper(path + tiles[i], tiles[:i] + tiles[i+1:], result)
        return result

# this also worked and I did it
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        if len(tiles) == 0 or tiles is None:
            return 0
        
        num_list = [i for i in tiles]
        path = []
        result = []
        combo_result = self.numTilePossibilitiesHelper(num_list, path, result)
        combo_result = ["".join(i) for i in combo_result]
        print(combo_result)
        
        result_set = set()
        for i in combo_result:
            result_set.add(i)
        return len(result_set) - 1
    
    def numTilePossibilitiesHelper(self, num_list, path, result):
        if not num_list:
            result.append(path)
        else:
            for i in range(len(num_list)):
                result.append(path)
                self.numTilePossibilitiesHelper(num_list[:i] + num_list[i+1:], path + [num_list[i]], result)
        return result