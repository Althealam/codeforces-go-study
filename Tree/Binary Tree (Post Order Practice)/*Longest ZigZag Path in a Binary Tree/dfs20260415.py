# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1. 题目类型：自顶向下
# 2. DFS三部曲：获取从node出发的最长的zigzag path的长度
#（1）携带参数：当前节点node，上一个边是left还是right，当前的zigzag path的长度，全局变量maxval
#（2）返回值含义：以当前节点开始的最长zigzag path的长度
#（3）终止条件：到达空节点的时候，则直接返回
#（4）单层递归的逻辑
# - 如果上一个边是left
#   - 递归到node.right，并且curval+=1
#   - 递归到node.left，并且curval=1
# - 如果上一个边是right
#   - 递归到node.left，并且curval+=1
#   - 递归到node.right，并且curval=1
# - 更新maxval

class Solution:
    def __init__(self):
        self.maxval = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, True)
        self.dfs(root, 0, False)
        return self.maxval
    
    def dfs(self, node, curval, is_left):
        if not node:
            return 
        if is_left==True:
            self.dfs(node.right, curval+1, False)
            self.dfs(node.left, 1, True)
        else:
            self.dfs(node.left, curval+1, True)
            self.dfs(node.right, 1, False)
        self.maxval = max(self.maxval, curval)