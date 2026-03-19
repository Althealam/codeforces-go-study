# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 是否需要遍历所有的节点：是的
# 2. 是否依赖子节点的返回值：是的
# 3. 什么时候操作以及操作什么：
# if root1.val!=root2.val: return False
# if root1 is None and root2 is None: return True
# if not root1 or not root2: return False
# traversal(root1.left, root2.left) and traversal(root1.right, root2.right)
# traversal(root1.left, root2.right) and traversal(root1.right, root2.left)


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.traversal(root1, root2)

    def traversal(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        return (self.traversal(root1.left, root2.left) and self.traversal(root1.right, root2.right))\
                or\
                (self.traversal(root1.left, root2.right) and self.traversal(root1.right, root2.left))

        