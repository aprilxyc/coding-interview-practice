https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/470612/Python-simple-recursive-and-iterative-solutions
# for the recursive solution, remember that the base case is when it is not a root

# classic mistake I did here:
    def maxDepth(self, root: TreeNode) -> int:
        if root.left is not None and root.right is not None:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# 1) I don't need a while loop because I am just recursively going through the subtrees
# 2) I don't need to check if root.left is not None and root.right is not None. Once I know that a root doesn't exist, I can just return 0 immmediately? 
# i.e. if not root

def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    