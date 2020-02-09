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
        # This is O(N) worst case where N is the height of the BST
        bst_sum = 0
        
        if root.val >= L and root.val <= R:
            bst_sum += root.val
        
        if root.left and root.val > L: # optimisation note that if the current node is less than the left value, then there is no point looking at the left subtree because all those values are all going to be less than the left value
            # need to make sure current node is greater than the left value
            bst_sum += self.rangeSumBST(root.left, L, R) # we know this because the left nodes will never be greater tthan L now
        
        if root.right and root.val < R:
            bst_sum += self.rangeSumBST(root.right, L, R)
        
        return bst_sum
    
def rangeSumBST(root, L, R):
    bst_sum = 0

    if root.val is None:
        return 0
    
    if root.val >= L and root.val <= R:
        bst_sum += root.val
    left = rangeSumBST(root.left, L, R)
    right = rangeSumBST(root.right, L, R)
    return bst_sum
        
        