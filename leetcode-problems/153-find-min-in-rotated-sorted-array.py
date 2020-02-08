"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[hi] > nums[0]:
            return nums[0] # no rotation
        
        while lo <= hi:
            mid = lo + ((hi-lo) // 2)
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                hi = mid - 1
