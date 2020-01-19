"""
https://leetcode.com/problems/plus-one/
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - i - 1)
        return [int(i) for i in str(num + 1)]

# study this solution where you shift the place
def plusOne(self, digits):
    length = len(digits) - 1
    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if(length < 0):
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits