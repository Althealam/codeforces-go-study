# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 如果root是空的，则直接返回TreeNode(val)
# 2. 如果root.val<val: 将val作为新的节点，并且root作为val的左子树
# 3. 如果root.val>val: 将val放在root的右子树上（因为val是被添加到末尾的，所以一定在右子树）
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        elif root.val<val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root

        