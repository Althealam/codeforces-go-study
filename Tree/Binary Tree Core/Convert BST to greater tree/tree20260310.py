# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0 
        self.traversal(root)
        return root
    
    def traversal(self, root):
        if root is None:
            return None
        # 先从右子树开始，再到左子树，这是题目的要求
        self.traversal(root.right)
        root.val+=self.pre
        self.pre = root.val
        self.traversal(root.left)
        