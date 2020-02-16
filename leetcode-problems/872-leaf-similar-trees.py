"""
https://leetcode.com/problems/leaf-similar-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        if root1 is None and root2 is None:
            return True
        
        arr1 = []
        arr2 = []
        self.leafSimilarHelper(root1, arr1)
        self.leafSimilarHelper(root2, arr2)
        
        if arr1 == arr2:
            return True
        return False
    
    def leafSimilarHelper(self, node, myArray):
        if node:
            if node.left is None and node.right is None:
                myArray.append(node.val)
            self.leafSimilarHelper(node.left, myArray)
            self.leafSimilarHelper(node.right, myArray)
            return myArray