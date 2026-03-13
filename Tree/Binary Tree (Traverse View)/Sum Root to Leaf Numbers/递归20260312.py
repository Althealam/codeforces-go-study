# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, 0)
        return self.res
    
    def traversal(self, root, current_sum):
        if root is None:
            return 
        current_sum = current_sum*10+root.val
        if root.left is None and root.right is None:
            self.res+=current_sum
            return 
        self.traversal(root.left, current_sum)
        self.traversal(root.right, current_sum)

