# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历+前驱节点
# dfs三部曲：
# 1. 返回参数及含义：只负责遍历，并更新全局变量
# 2. 携带参数：当前节点，前驱节点
# 3. 终止条件：当前节点为空时则停止
# 4. 单层递归逻辑
# - 递归左子树
# - 处理当前节点：更新ans，同时更新prev
# - 递归右子树
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        prev = None
        def dfs(node):
            nonlocal res, prev
            if node is None:
                return 
            dfs(node.left)
            if prev is not None:
                res = min(res, node.val-prev)
            prev = node.val
            dfs(node.right)
        dfs(root)
        return res