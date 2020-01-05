"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

# brute force method
# TRYING TO PLACE NON-ZEROES WITH ZEROES, SIMPLY USE TWO POINTERS
    def moveZeroes(self, nums: List[int]) -> None:
        # O(N) time complexity where N is the number of items in the nums list
        # O(M) space complexity where N is the number of items in the nums list
        """
        Do not return anything, modify nums in-place instead.
        """
        lag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[lag]
                nums[lag] = temp
                # or nums[i], nums[lag] = nums[lag], nums[i]
                lag += 1

# study this method
def moveZeroes(self, nums):
"""
:type nums: List[int]
:rtype: void Do not return anything, modify nums in-place instead.
"""
count=nums.count(0)
nums[:]=[i for i in nums if i != 0]
nums+=[0]*count