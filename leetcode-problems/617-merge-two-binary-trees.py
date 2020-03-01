"""
https://leetcode.com/problems/merge-two-binary-trees/
Really not sure what I wrote here tbh wow help
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        if t1 is None and t2 is None:
            return None
        
        t3 = TreeNode(t1.val + t2.val)
        
        queue = []
        queue.append((t1.left, t2.left))
        queue.append((t1.right, t2.right))
        
        while queue:    
            left_t1, left_t2 = queue.pop()
            right_t1, right_t2 = queue.pop()
            
            if left_t1 is None and left_t2 is None and right_t1 is None and right_t2 is None:
                return t3
            
            if left_t1 and left_t2:
                t3.left = TreeNode(left_t1.val + left_t2.val)
            elif left_t1 and left_t2 is None:
                t3.left = TreeNode(left_t1.val)
            elif left_t2 and left_t1 is None:
                t3.left = TreeNode(left_t2.val)
                
            if right_t1 and right_t2:
                t3.right = TreeNode(right_t1.val + right_t2.val)
            elif right_t1 and right_t2 is None:
                t3.right = TreeNode(right_t1.val)
            elif right_t2 and right_t1 is None:
                t3.right = TreeNode(right_t2.val)
            
            left_t1, left_t2= left_t1.left, left_t2.left
            right_t1, right_t2 = right_t1.right, right_t2.right

# actual solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if t1 is None:
            return t2
        
        if t2 is None:
            return t1
        
        if t1 is None and t2 is None:
            return None
        
        t1.val += t2.val # add the values together 
        # but we need to do this for all trees
        # so we have to do this recursively for the rest of the tree
        # this is very common traversal
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right) # save it into t1
        return t1
            
# relook at this
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        root_node = None
        
        if not t1:
			# t1 is empty, new tree is decided by t2
            return t2
        
        elif not t2:
			# t2 is empty, new tree is decided by t1
            return t1
        
        else:
            # both t1 and t2 exist, merge current node, and traverse on DFS again
            root_node =  TreeNode( t1.val + t2.val )
            root_node.left = self.mergeTrees( t1.left, t2.left )
            root_node.right = self.mergeTrees( t1.right, t2.right )
            
            return root_node