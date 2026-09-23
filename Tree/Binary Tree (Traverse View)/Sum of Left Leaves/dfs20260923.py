# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(h)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.getleftsum(root.left)+self.getleftsum(root.right)
    
    def getleftsum(self, node):
        if not node:
            return 0
        # 寻找最左的叶子节点
        if node.left:
            node = node.left
        return node.val
        