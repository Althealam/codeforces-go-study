# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)
# 当前路径->加上当前节点->如果是叶子节点，加入res->否则继续递归左右子树
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:        
        res = []
        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            # 1. 判断是否到达了叶子节点
            if node.left is None and node.right is None:
                res.append("->".join(path[:]))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            # 2. 回溯
            path.pop()
        dfs(root, [])
        return res