# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.res
    
    def traversal(self, root):
        if not root:
            return 0
        if root.val%2==0:
            if root.left is not None:
                if root.left.left is not None:
                    self.res+=root.left.left.val
                if root.left.right is not None:
                    self.res+=root.left.right.val
            
            if root.right is not None:
                if root.right.left is not None:
                    self.res+=root.right.left.val
                if root.right.right is not None:
                    self.res+=root.right.right.val
        self.traversal(root.left)
        self.traversal(root.right)

        