# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1. 题目类型：自底向上
# 2. DFS三部曲：当前节点经过处理后的节点（node，None）
#（1）携带参数：当前节点node，当前路径总和cursum
#（2）返回值含义：当前节点经过处理后的节点
#（3）终止条件
# - 如果当前节点为空节点，则返回None
# - 如果当前节点是叶子节点，并且cursum+node.val<limit，return None
#（4）单层递归的逻辑
# - 获取左右子树的返回值
#   - left=None and right=None：return None
#   - left!=None or right!=None: return node

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
        node.left = self.dfs(node.left, cursum+node.val, limit)
        node.right = self.dfs(node.right, cursum+node.val, limit)
        if node.left is None and node.right is None:
            return None
        return node
