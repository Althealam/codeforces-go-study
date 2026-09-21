# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向上
# 2. DFS三部曲
#（1）递归函数的参数：当前节点node
#（2）返回值：以当前节点为根的子树的最小深度
#（3）终止条件：节点为空时返回0
#（4）单层递归的逻辑：递归求左右子树的最小深度（不可以直接min(left_depth, right_depth)+1，因为如果左子树为空的情况下，会直接取最小值得到1）
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        return self.dfs(root)
        
    def dfs(self, node):
        if node is None:
            return 0
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)

        if node.left is None:
            return right_depth+1
        if node.right is None:
            return left_depth+1
        return min(left_depth, right_depth)+1
        
        