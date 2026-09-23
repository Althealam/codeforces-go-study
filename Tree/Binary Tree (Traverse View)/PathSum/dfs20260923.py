# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS三部曲：
#（1）携带参数：当前节点，当前的路径和，目标和
#（2）返回值及含义：true/false，表示是否找到了一条从根节点到叶子节点的路径，并且路径和为targetsum
#（3）终止条件：如果当前的节点为叶子节点，则开始判断当前路径和是否等于目标和
#（4）单层递归的逻辑
# 递归左右子节点
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)
    
    def dfs(self, node, targetSum, pathsum):
        if not node:
            return False
        pathsum+=node.val
        if node.left is None and node.right is None:
            return pathsum==targetSum
        return self.dfs(node.left, targetSum, pathsum) or self.dfs(node.right, targetSum, pathsum)
        