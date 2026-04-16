# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上根据子节点的留存来决定父亲节点的留存
# 2. DFS三部曲
#（1）携带参数：当前节点，limit，从根节点到当前节点的路径和
#（2）返回值含义：如果经过当前节点的路径严格小于limit则返回None；如果经过当前节点的路径大于等于limit则返回node
#（3）终止条件：
# - 如果到达空节点，则直接返回空节点
# - 如果到达叶子节点，则要判断此时的路径和是否小于limit，如果小于limit，则一定要删除该叶子节点，则返回None
#（4）单层递归的逻辑：后序遍历（自底向上都是后序遍历）
# - 递归获取左右子树的情况
#   - 如果左右子树都为空，则说明说明经过该节点的路径小于limit，则删除该节点


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return self.dfs(root, limit, 0)
    
    def dfs(self, node, limit, cursum):
        if not node:
            return None
        # 到达叶子节点
        if node.left is None and node.right is None:
            if cursum+node.val<limit:
                return None
            else:
                return node
        cursum+=node.val
        # 递归处理左右子树，自底向上（后序遍历）
        node.left = self.dfs(node.left, limit, cursum)
        node.right = self.dfs(node.right, limit, cursum)
        if node.left is None and node.right is None: # 左右子节点都是空节点，说明经过该节点的所有路径和都小于limit
            return None
        return node