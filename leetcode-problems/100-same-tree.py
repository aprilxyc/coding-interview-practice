"""
https://leetcode.com/problems/same-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not p and not q: # the order of this matters!
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        # traverse the left side of the tree
        left = self.isSameTree(p.right, q.right) 
        # traverse the right side of the tree
        right = self.isSameTree(p.left, q.left)
        # if both trees are the same, they will not have returned false, hence will be TRUE
        # so if you AND it, it should return true in the end
        # otherwise it will return False in the end
        return left and right

        