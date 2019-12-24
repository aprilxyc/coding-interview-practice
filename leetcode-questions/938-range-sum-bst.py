# Tree traversals: BFS guarantees we touch every single node in our tree
# while doing BFS, modify it to add all the sum values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        bst_sum = 0
        
        if root.val >= L and root.val <= R:
            bst_sum += root.val
        
        if root.left:
            bst_sum += self.rangeSumBST(root.left, L, R)
        
        if root.right:
            bst_sum += self.rangeSumBST(root.right, L, R)
        
        return bst_sum
        
        