class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # O(N) time complexity where N is the number of elements in num
        # O(1) space complexity
        
        if nums == []:
            return 0
        
        is_even = 0 # keeps track of the number of nums that have even number of digits
        for num in nums:
            if len(str(num)) % 2 == 0:
                is_even += 1
        return is_even

# cleaner solution with list comprehension so it is faster
def findNumbers(nums):
    '''
    For faster execution use list comprehension. It creates a table with as many ones as there are even digits numbers.
    To calculate number of digits it's necessary to convert int into string as intigers don't have len method.
    '''
    return len["hello" for number in nums if len(str(number)) % 2 == 0])
    
nums = [12,345,2,6,7896]
findNumbers(nums)
