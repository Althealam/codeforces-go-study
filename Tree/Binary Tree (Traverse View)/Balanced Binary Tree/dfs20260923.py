# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(h)，递归栈的深度
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        if abs(leftheight-rightheight)>1:
            return False
        return True
    
    def getheight(self, node):
        if not node:
            return 0
        return max(self.getheight(node.left), self.getheight(node.right))+1