"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

# brute force method
# TRYING TO PLACE NON-ZEROES WITH ZEROES, SIMPLY USE TWO POINTERS
  def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lag], nums[i] = nums[i], nums[lag]
                lag += 1
        return nums