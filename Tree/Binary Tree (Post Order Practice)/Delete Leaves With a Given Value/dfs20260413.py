# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：处理以node为根节点的子树中的叶子节点
#（1）携带参数：node
#（2）返回值含义：处理好叶子节点的node
#（3）终止条件
# - 如果当前节点为空节点，则直接返回空
#（4）单层递归的逻辑
# - 获取左右子树的返回值，将左右子树的返回值拼接到原来的父亲节点的孩子节点上
# - 如果当前节点为叶子节点，并且该叶子节点的值为target，则直接返回空
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.dfs(root, target)
    
    def dfs(self, node, target):
        if not node:
            return None
        left = self.dfs(node.left, target)
        right = self.dfs(node.right, target)
        node.left = left
        node.right = right
        if node.left is None and node.right is None and node.val==target:
            return None
        return node
        