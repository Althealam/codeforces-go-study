# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        res = []
        path = []
        self.dfs(root, path, res)
        return res
    
    def dfs(self, node, path, res):
        if not node:
            return 
        path.append(str(node.val))
        # 遇到叶子节点时要path.pop()
        if node.left is None and node.right is None:
            res.append("->".join(path[:]))
            path.pop()
            return
        self.dfs(node.left, path, res)
        self.dfs(node.right, path, res)
        path.pop()