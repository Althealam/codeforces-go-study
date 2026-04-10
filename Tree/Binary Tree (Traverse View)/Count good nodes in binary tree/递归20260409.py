# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）携带信息：从根节点到当前节点的路径上的最大值，当前节点
#（2）返回值含义：以当前节点为根节点的子树中，包含的好节点的数量
#（3）终止条件
# 如果node为空节点，说明没节点了，返回0
#（4）单层递归的逻辑
# - 判断当前：
#   - if node.val>max_val：当前节点是好节点，计数；更新当前路径的最大值
#   - if node.val<max_val：当前节点不是好节点
# - 向下传承：获取以左右子节点为根节点的子树中，包含的好节点的数量
# - 汇总：isgood+leftcnt+rightcnt

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(float('-inf'), root)
    
    def dfs(self, maxval, node):
        if not node:
            return 0
        if node.val>=maxval:
            return 1+self.dfs(node.val, node.left)+self.dfs(node.val, node.right)
        else:
            return self.dfs(maxval, node.left)+self.dfs(maxval, node.right)

        