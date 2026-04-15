# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. 题目类型：自顶向下传递信息，自底向上做决策
# 2. DFS三部曲
#（1）参数含义：当前节点，从根节点到父亲节点路径上的累加和，limit
#（2）返回值：处理后的当前节点（如果这个节点需要被删除，则返回None）
#（3）终止条件
# - 当到达叶子节点时，开始做决定
#   - 如果此时cursum+node.val<limit，说明这条唯一的路径不及格，叶子节点需要删除
#   - 否则，返回node
#（4）单层递归的逻辑
# - 更新累加和：cursum+node.val
# - 递归处理左右子树：node.left, node.right
# - 判断这个节点是否该死：如果递归后，发现node.left和node.right都是None，说明经过我的节点全部都不及格，说明这条节点也要消失

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return self.dfs(root, 0, limit)
    
    def dfs(self, node, cursum, limit):
        if not node:
            return None
        if node.left is None and node.right is None:
            if cursum+node.val<limit: 
                return None
            else:
                return node
        cursum+=node.val
        node.left = self.dfs(node.left, cursum, limit)
        node.right = self.dfs(node.right, cursum, limit)
        if node.left is None and node.right is None:
            return None
        return node

        