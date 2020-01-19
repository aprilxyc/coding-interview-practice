"""
https://leetcode.com/problems/missing-number/
"""

# know this law
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
           # array containing n distinct numbers taken from 0, 1, 2, ..., n
        
        #   sum of ideal array without missing
        # = sum of array + missing element
        # = 0 + 1 + 2 + ... + missing element + ... + n 
        # = 0 + 1 + 2 + ... + n
        # = 1 + 2 + ... + n
        # = (1+n)*n // 2
        #
        # => sum of ideal array without missing - sum of array = missing element
		
        n = len(nums) + 1
        
        missing_element = int(n * (n-1)/2 - sum(nums))
        
        return missing_element

# we can have oferflow in the sum formula above because
# the numbers can get very large
# bit manipulation solution below is better:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
           # array containing n distinct numbers taken from 0, 1, 2, ..., n
        
        #   sum of ideal array without missing
        # = sum of array + missing element
        # = 0 + 1 + 2 + ... + missing element + ... + n 
        # = 0 + 1 + 2 + ... + n
        # = 1 + 2 + ... + n
        # = (1+n)*n // 2
        #
        # => sum of ideal array without missing - sum of array = missing element
		
        result = 0
        for i in range(0, len(nums) + 1):
            result ^= i
        for i in nums:
            result ^= i
        return result