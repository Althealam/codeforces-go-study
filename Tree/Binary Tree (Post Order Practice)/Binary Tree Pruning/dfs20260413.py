# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：判断一下以node为根节点的子树是否包含1
#（1）携带参数：当前节点
#（2）返回值：node/None，如果为node表示以node为根节点的子树包含1，如果为None表示以node为根节点的子树不包含1
#（3）终止条件：遇到空节点则直接返回None
#（4）单层递归的逻辑
# - 获取左右子树的返回值：如果其中一个子树的返回值为None，说明该子树没有1，则将node拼接None
# - 如果左右子树的返回值都为None，并且node.val!=1，那么这个node的返回值也为None
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return None
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        node.left = left
        node.right = right
        if left is None and right is None and node.val!=1:
            return None
        return node