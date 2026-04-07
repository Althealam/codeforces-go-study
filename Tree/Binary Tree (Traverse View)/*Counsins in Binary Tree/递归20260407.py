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
#（2）携带信息：parent_val, depth（当前节点的父亲和当前节点处于第几层）
#（3）终止条件：
# - 空节点直接返回
#（4）单层递归
# 如果node.val==x或者node.val==y，则记录一下x或者y的parent_val和depth

class Solution:
    def __init__(self):
        self.parentx = 0
        self.parenty = 0
        self.depthx = 0
        self.depthy = 0
        self.x, self.y = 0, 0

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x, self.y = x, y
        self.dfs(root, 0, 0)
        if self.parentx!=self.parenty and self.depthx==self.depthy:
            return True
        return False
    
    def dfs(self, node, parent_val, depth):
        if not node:
            return 
        if node.val==self.x:
            self.parentx = parent_val
            self.depthx = depth
        if node.val==self.y:
            self.parenty = parent_val
            self.depthy = depth
        self.dfs(node.left, node.val, depth+1)
        self.dfs(node.right, node.val, depth+1)
        
        