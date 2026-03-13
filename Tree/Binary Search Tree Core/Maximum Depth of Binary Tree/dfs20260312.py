# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.res
    
    def traversal(self, root):
        if root is None:
            return 
        self.depth+=1
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)
        self.traversal(root.left)
        self.traversal(root.right)
        self.depth-=1
