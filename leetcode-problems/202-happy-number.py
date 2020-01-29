class Solution(object):
    def isHappy(self, n):

        def square_sum(num):
            result = 0
            while num > 0:
                r = num % 10
                result = result + r * r
                num = num // 10
            return result
        
        seen = set()
        while square_sum(n) not in seen:
            sum1 = square_sum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1
        return False