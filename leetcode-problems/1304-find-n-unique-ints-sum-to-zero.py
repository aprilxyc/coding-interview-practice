"""
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""

# this is my solution
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1:
            return [0]
        
        if n % 2 != 0:
            result = [0]
        else:
            result = []
        
        while len(result) < n:
            new_int = random.randint(-n, n)
            if new_int not in result and new_int != 0:
                result.append(new_int)
                result.append(-new_int)
        return result

# better solution
# we know that we want it to be symmetrical 
# i.e. n = 1 returns 0, n = 2 returns [-1, 1], n = 3 returns [0, -1, 1], n = 4 returns [-1, 1, -2, 2], n = 5 returns [0, -1, 1, -2, 2]
class Solution:
    def sumZero(self, n: int) -> List[int]:

        if n == 1:
            return [0]
        
        highest_num = n // 2
        remainder = n % 2

        if n % 2 != 0:
            result = [0]
        else:
            result = []
        
        for i in range(1, highest_num + 1):
            result.append(i)
            result.append(-i)
        return result