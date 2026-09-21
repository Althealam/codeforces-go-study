# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）携带信息：当前节点
#（2）返回值含义：当前节点的最大深度
#（3）终止条件：如果该节点为空，则返回0
#（4）单层递归的逻辑
# - 最大深度=左子树最大深度+右子树最大深度+1
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right))+1
        