# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 是否需要遍历所有节点：是的
# 2. 是否需要子节点的返回值：是的
# 3. 思路
# - if root1.val!=root2.val: return False
# - if root1 is None and root2 is None: return True
# - if root1 is None or root2 is None: return False
# - if root1.val==root2.val: 递归判断一下左右子树
# * self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
# * self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        if root1.val==root2.val:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))\
            or\
            (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))