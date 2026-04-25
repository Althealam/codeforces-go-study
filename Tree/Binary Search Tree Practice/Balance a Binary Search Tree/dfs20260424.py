# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 使用中序遍历获取递增数组
# 2. 使用递增数组构建平衡的二叉搜索树
class Solution:
    def __init__(self):
        self.res = []

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inordertraverse(root)
        return self.dfs(0, len(self.res)-1)
    
    def inordertraverse(self, root):
        if not root:
            return None
        self.inordertraverse(root.left)
        self.res.append(root.val)
        self.inordertraverse(root.right)
    
    def dfs(self, lo, hi):
        if lo>hi:
            return None
        mid = lo+(hi-lo)//2
        root = TreeNode(self.res[mid])
        root.left = self.dfs(lo, mid-1)
        root.right = self.dfs(mid+1, hi)
        return root