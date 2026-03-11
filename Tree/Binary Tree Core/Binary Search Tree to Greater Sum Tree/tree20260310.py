# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.traversal(root)
        return root
    
    def traversal(self, root):
        if not root:
            return None
        self.traversal(root.right)
        root.val+=self.pre
        self.pre = root.val
        self.traversal(root.left)