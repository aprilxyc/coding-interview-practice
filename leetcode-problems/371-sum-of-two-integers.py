"""
https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Good explanation of this is:
https://github.com/bephrem1/backtobackswe/blob/master/Arrays,%20Primitives,%20Strings/AdditionWithOnlyBitshifting/AdditionWithOnlyBitshifting.java
"""

# this is a bit annoying in Python because you have to handle the negative number aspect otherwise it will go into an infinite loop
   def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff # mask is used to handle negative numbers
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # for overflow condition like
        # -1
        #  1
        return a & mask if b > mask else a