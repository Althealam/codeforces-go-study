# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = [(root1, root2)]
        while stack:
            cur1, cur2 = stack.pop()
            if cur1 is None and cur2 is None:
                continue
            if not cur1 or not cur2:
                return False
            if cur1.val!=cur2.val:
                return False
            # 检查一下cur1.left==cur2.left（比较left就可以决定是否需要反转了）
            if (cur1.left and cur2.left and cur1.left.val==cur2.left.val) or (not cur1.left and not cur2.left):
                stack.append((cur1.left, cur2.left))
                stack.append((cur1.right, cur2.right))
            else:
                stack.append((cur1.left, cur2.right))
                stack.append((cur1.right, cur2.left))
        return True
            