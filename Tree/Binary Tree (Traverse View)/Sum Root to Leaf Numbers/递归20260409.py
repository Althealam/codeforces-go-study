# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 本题需要获取从根节点到子节点的所有路径的数值
# 2. DFS三部曲
#（1）携带信息：当前节点，当前的路径贡献值
#（2）返回值含义：无
#（3）终止条件：如果当前节点的左右子节点为空节点，说明到达了叶子节点，那么更新全局变量
#（4）单层递归的逻辑
# - 当前路径的贡献值：curpath = curpath*10+node.val
# - 继续递归左右子节点

class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, curpath):
        if not node:
            return 0
        curpath = curpath*10+node.val
        if node.left is None and node.right is None:
            self.res+=curpath
        self.dfs(node.left, curpath)
        self.dfs(node.right, curpath)