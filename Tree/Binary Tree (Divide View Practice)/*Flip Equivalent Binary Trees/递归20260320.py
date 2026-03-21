# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 是否需要遍历所有节点：是的
# 2. 是否依赖子节点的返回值：是的，可以通过分解左右子树来判断
# 3. 什么时候操作，以及做什么操作
# 如果root1==None and root2==None: return True
# 如果root1!=None or root2!=None: return False
# 如果root1.val!=root2.val: return False
# 如果root1.val==root2.val: 递归判断其左右子树
# - self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
# - self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        if root1.val==root2.val:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            or
            self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        