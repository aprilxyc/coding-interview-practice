"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        # using depth first search
        stack = [] 
        stack.append(root) 
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        # using breadth first search
        queue = [] 
        queue.append(root) 
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return None

# recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return None
        
        if root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

