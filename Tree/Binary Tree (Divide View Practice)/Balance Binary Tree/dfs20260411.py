# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 2. DFS三部曲
#（1）返回值含义：如果当前节点为根的子树是平衡的，则返回实际高度；否则返回-1
#（2）携带参数：当前节点
#（3）终止条件：遇到空节点的时候返回0
#（4）单层递归的逻辑：
# - 递归查询左子树，如果左子树已经是-1，则说明左边已经失衡，则直接返回-1
# - 递归查询右子树，如果右子树已经是-1，则说明右边已经失衡，则直接返回-1
# - 当前节点处理
#   - 获取左右子树的高度
#   - 计算差值：abs(leftheight-rightheight)
#   - 如果差值>1说明当前节点失衡，则返回-1；否则返回高度

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.dfs(root)==-1:
            return False
        return True
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left, right)+1
        