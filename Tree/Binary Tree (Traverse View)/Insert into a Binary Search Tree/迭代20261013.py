# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(h)
# 空间复杂度：O(1)
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)
        cur = root

        # 寻找需要插入的位置
        while cur is not None:
            parent = cur # 用来记录待插入位置的父亲节点
            if cur.val<val:
                cur = cur.right
            else:
                cur = cur.left

        node = TreeNode(val)
        if val<parent.val: # 当前节点应该插入在左子树
            parent.left = node
        else:
            parent.right = node
        return root