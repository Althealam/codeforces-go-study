# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 1, 1)] # 父亲的值，祖父的值
        while stack:
            node, p_val ,gp_val = stack.pop()
            if not node:
                continue
            # 祖父是偶数，就累加当前节点的值
            if gp_val%2==0:
                res+=node.val
            
            # 子节点推入栈中
            if node.right:
                stack.append((node.right, node.val, p_val))
            if node.left:
                stack.append((node.left, node.val, p_val))
        return res
