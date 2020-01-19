"""
https://leetcode.com/problems/rotate-array/
"""

# my solution
# works for small test cases
# does not work for big test cases
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(kN)
        if len(nums) == 1:
            return nums
        
        i = 0
        while i < k:
            end = len(nums) - 1
            temp = nums[end]
            while end > 0:
                nums[end] = nums[end - 1]
                end -= 1
            nums[0] = temp
            i += 1