# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 判断堂兄弟必须要同时满足两个指标
# - 深度相同（depth_x==depth_y）
# - 父亲不同（parent_x==parent_y）
# 2. DFS三部曲：DFS用来获取x和y的父亲节点和深度
#（1）返回值含义：没有
#（2）携带信息：当前节点信息, parent_val, depth（当前节点的父亲和当前节点处于第几层）
#（3）终止条件：
# - 空节点直接返回
# - 如果node.val==x或者node.val==y，则记录一下x或者y的parent_val和depth
#（4）单层递归
# 递归左右子树

class Solution:
    def __init__(self):
        self.depthx = 0
        self.depthy = 0
        self.parentx = 0
        self.parenty = 0
        self.x, self.y = 0, 0
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x, self.y = x, y
        self.dfs(None, 0, root)
        if self.depthx==self.depthy and self.parentx!=self.parenty:
            return True
        return False
    
    def dfs(self, parent_val, depth, node):
        if not node:
            return 
        if node.val==self.x:
            self.depthx = depth
            self.parentx = parent_val
        if node.val==self.y:
            self.depthy = depth
            self.parenty = parent_val
        self.dfs(node.val, depth+1, node.left)
        self.dfs(node.val, depth+1, node.right)
        