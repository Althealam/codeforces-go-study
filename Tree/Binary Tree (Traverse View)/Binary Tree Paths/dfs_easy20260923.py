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
            if path:
                path+='->' # python字符串是不可变对象，因此每次path+=都会生成一个新的字符串，所以左右子树不会互相污染
            path+=str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
                return 
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res