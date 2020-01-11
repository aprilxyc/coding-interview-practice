class Solution:
    def isArmstrong(self, N: int) -> bool:
        #O(N) where N is the number of digits in the number

        # get the length of the digit
        original_num = N
        num_len = len(str(N))
    
        final_sum = 0
        while N != 0:    
            new_number = N % 10 # get the last digit
            final_sum += new_number ** num_len
            N //= 10
        return final_sum == original_num

    
    # alternate solution using for loop
    def isArmstrong(N):
        k = len(str(N))
        final_sum = 0
        for i in str(N):
            final_sum += int(N) ** k
            if final_sum == N:
                return True

    #TODO LEARN HOW TO THINK IN THIS MANNER
    def isArmstrong(N):
        t = str(N)
        return sum(int(x) ** len(t) for x in t) == N

# my latest solution 11/01
class Solution:
    def isArmstrong(self, N: int) -> bool:
        original = N
        power = len(str(N)) # 3
        result = 0
        while N != 0:# 153 
            last_digit = N % 10 # last digit is 1
            result += (last_digit ** power) # 153
            N //= 10 # # 1
        return result == original
