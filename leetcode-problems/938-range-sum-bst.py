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

# using BFS to traverse al the nodes
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root == None:
            return 0
        
        result = 0
        
        # using BFS
        queue = []
        queue.append(root)
        while queue:
            item = queue.pop(0) # remove the first item
            if item.val >= L and item.val <= R:
                result += item.val
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        return result

# to make it even faster
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root == None:
            return 0
        
        result = 0
        
        # using BFS
        queue = []
        queue.append(root)
        while queue:
            item = queue.pop(0) # remove the first item
            if item.val >= L and item.val <= R:
                result += item.val
            if item.left and item.val > L: # automatiaclly ensures the current node is > L so we don't waste time looking at the left if it is < L
                queue.append(item.left)
            if item.right and item.val < R: # automatically ensures the current node is < R so we don't waste time looking at the right if it is > R
                queue.append(item.right)
        return result
        
        