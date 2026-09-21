# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        stack = [(left, right)]
        while stack:
            x, y = stack.pop()
            if x is None and y is None:
                continue
            if x is None or y is None:
                return False
            if x.val!=y.val:
                return False
            stack.append((x.left, y.right))
            stack.append((x.right, y.left))
        return True