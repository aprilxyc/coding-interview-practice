# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.minimumBST(nums, 0, len(nums) - 1)
    
    def minimumBST(self, nums, start, end):
        if end < start:
            return None               

        mid = (start + end + 1) // 2
        node = TreeNode(nums[mid])
        node.left = self.minimumBST(nums, start, mid - 1)
        node.right = self.minimumBST(nums, mid + 1, end)
        return node


        
            