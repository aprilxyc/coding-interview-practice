"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# go over this and study it
# there is also a slicing method that takes up a lot more memory
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, low, high):
        if low > high:
            return None
        mid = (low + high) // 2 # this should be left + (right - left) / 2 to account for very large numbers
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, low, mid - 1)
        root.right = self.helper(nums, mid + 1, high)
        
        return root