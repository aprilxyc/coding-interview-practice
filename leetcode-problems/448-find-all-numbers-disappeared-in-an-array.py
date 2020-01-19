"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []
        
        # Loop through the array and turn the relevent indices negative
        for i in range(0, len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                # turn it into negative
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        
        result = []
        for i in range(0, len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result
            
        
        
        