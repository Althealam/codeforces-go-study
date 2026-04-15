# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 注意：路径探索是自顶向下的（带着祖先的信息去探路），结果汇总是自底向上的（把下面发现的最大差值汇报上来）
# 2. DFS三部曲：
#（1）携带参数：self.max_val记录遍历过程中发现的最大差值，当前节点node，cur_max，cur_min
#（2）返回值含义：从根节点到当前节点的祖先和子节点的最大差值
#（3）终止条件：如果node为空，则说明已经遍历完了，则更新curmax-curmin
#（4）单层递归的逻辑
# - 更新答案，更新curmin和curmax
# - 递归左右子树


class Solution:
    def __init__(self):
        self.max_val = float('-inf')

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, float('-inf'), float('inf'))
        return self.max_val
    
    def dfs(self, node, curmax, curmin):
        if not node:
            self.max_val = max(self.max_val, curmax-curmin)
            return 
        curmax = max(curmax, node.val)
        curmin = min(curmin, node.val)
        self.dfs(node.left, curmax, curmin)
        self.dfs(node.right, curmax, curmin)