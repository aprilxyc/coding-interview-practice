"""
Leetcode problem 461

Time Complexity: O(N)
Space Complexity: O(N) where N is the length of the smallest number
"""

def hammingDistance(x, y):
    result = 0
    while x > 0 or y > 0: #O(N) where N is the length of the smallest number
        result += (x % 2) ^ (y % 2) #O(1)
        x >>= 1 #O(1)
        y >>= 1 #O(1)
    return result
