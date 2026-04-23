# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）携带参数：preorder，upperbound，同时定义一个全局变量idx用来记录现在遍历到preorder的哪个元素了
#（2）返回值含义：按照preorder处理好的二叉树
#（3）终止条件：
# - 如果self.idx==len(preorder)则返回None
# - 如果当前节点的值大于upperbound，说明当前节点是不属于这个子树的，则返回None
#（4）单层递归的逻辑
# - 获取根节点，为preorder的第一个元素，记录一个upperbound
# - 递归左右子树
#   - 左子树的upperbound是rootval
#   - 右子树的upperbound是由父亲节点传承下来的

class Solution:
    def __init__(self):
        self.idx = 0 # 当前遍历到的数组的下标
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, float('inf'))
    
    def dfs(self, preorder, upperbound):
        if self.idx==len(preorder):
            return None
        if preorder[self.idx]>upperbound: # 当前元素并不属于这个子树
            return None
        root = TreeNode(preorder[self.idx])
        self.idx+=1 
        root.left = self.dfs(preorder, root.val)
        root.right = self.dfs(preorder, upperbound) # 记录一下父亲子树传递下来的upperbound
        return root