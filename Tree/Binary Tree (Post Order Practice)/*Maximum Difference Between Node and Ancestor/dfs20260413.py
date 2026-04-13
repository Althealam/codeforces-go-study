# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）携带参数：当前节点，当前路径上的最小值，当前路径上的最大值
#（2）返回值：当前子树可以产生的最大差值
#（3）终止条件：如果当前节点为空节点，说明这条路径已经走完了，那么最大差值就是cur_max-cur_min
#（4）单层递归的条件
# - 每次到达一个新节点，先用当前节点的值更新路径上的cur_min和cur_max
# - 向下传递，将更新后的cur_min和cur_max传递给左右子树
# - 获取左右子树的最大差值，并且返回max(left_diff, right_diff)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)
    
    def dfs(self, node, curmin, curmax):
        if not node:
            return curmax-curmin
        curmin = min(node.val, curmin)
        curmax = max(node.val, curmax)
        left_diff = self.dfs(node.left, curmin, curmax)
        right_diff = self.dfs(node.right, curmin, curmax)
        return max(left_diff, right_diff)

        