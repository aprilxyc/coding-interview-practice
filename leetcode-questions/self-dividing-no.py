"""
Problem 782
Time complexity: O(N) where N is number of numbers between left and right
Space complexity: O(1)
https://leetcode.com/problems/self-dividing-numbers/

Notes: 
Know map, reduce, filter and list comprehensions well. 
"""
def selfDividingNumbers(left, right):
    is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
    return filter(is_self_dividing, range(left, right+1))