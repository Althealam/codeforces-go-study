# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 通过中序遍历获取二叉搜索树的数组
# 2. 建树

class Solution:
    def __init__(self):
        self.res = []

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inorder_traversal(root)
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.res: # 存储节点，而不是值
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right
    
    def inorder_traversal(self, root):
        if root.left:
            self.inorder_traversal(root.left)
        self.res.append(root)
        if root.right:
            self.inorder_traversal(root.right)
    
        