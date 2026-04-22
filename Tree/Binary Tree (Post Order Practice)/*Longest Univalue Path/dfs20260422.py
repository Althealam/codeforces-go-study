# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 2. DFS三部曲：以当前节点为起点，向其子树延伸的符合条件的路径的长度
#（1）携带参数：当前节点node
#（2）返回值含义：以node为起点，和node.val的值相同的节点组合路径最长的长度
#（3）终止条件：如果node为空节点，则返回0
#（4）单层递归的逻辑
# - 调用DFS，获取左右子树的返回值
# - 判断当前节点和左右子节点的值是否相同
#   - node.val==node.left.val: left = leftlen+1
#   - node.val==node.right.val: right = rightlen+1
# - 当前可以找到的最长路径是left+right，将这个值和maxval对比来更新全局最大值
# - 以node为起点找到的符合条件的最长路径长度为max(left, right)，只可以返回单边的值，不可以返回left+right

class Solution:
    def __init__(self):
        self.maxval = float('-inf')

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxval if self.maxval!=float('-inf') else 0
    
    def dfs(self, node):
        if node is None:
            return 0
        leftlen = self.dfs(node.left)
        rightlen = self.dfs(node.right)
        leftval = 0
        rightval = 0
        if node.left and node.val==node.left.val:
            leftval = leftlen+1
        if node.right and node.val==node.right.val:
            rightval = rightlen+1
        self.maxval = max(self.maxval, leftval+rightval)
        return max(leftval, rightval)