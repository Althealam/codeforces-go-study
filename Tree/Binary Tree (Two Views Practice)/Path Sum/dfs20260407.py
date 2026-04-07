# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 使用dfs获取从root到所有leaf的路径总和
#（1）是否依赖子节点的返回值：否
#（2）是否需要访问所有的节点：是的
#（3）需不需要记录路径：不需要？只要记录路径总和值即可
#（4）操作发生在哪：当到达叶子节点的时候开始进行判断
# 2. 判断一下当前路径总和是否等于targetSum，如果是的话则直接返回True，否则的话则continue

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, path_sum, targetSum):
        if not root:
            return False
        path_sum+=root.val
        if root.left is None and root.right is None:
            return path_sum==targetSum
        return self.dfs(root.left, path_sum, targetSum) or self.dfs(root.right, path_sum, targetSum)

        