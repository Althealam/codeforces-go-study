# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        res = self.inorder(root)
        if len(res)==1:
            return True
        for i in range(1, len(res)):
            if res[i]<=res[i-1]:
                return False
        return True
    
    def inorder(self, root):
        res = []
        def dfs(node, res):
            if not node:
                return []
            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)
        dfs(root, res)
        return res