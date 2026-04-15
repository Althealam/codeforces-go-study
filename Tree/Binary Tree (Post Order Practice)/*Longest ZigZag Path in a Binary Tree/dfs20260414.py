# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下传递信息，自底向上返回值
# 2. DFS三部曲
#（1）携带参数：全局变量maxpath，当前节点，当前zigzag路径长度，上一个路径是left还是right
#（2）返回值含义：从根节点到当前节点的最长zigzag路径长度（不需要返回）
#（3）终止条件：
# - 遇到空节点，则直接返回
#（4）单层递归的逻辑
# - 更新路径长度
# - 如果上一个节点是left，则递归dfs(node.right...)，同时开启一条新路（但是curpath=0）
# - 如果上一个节点是right，则递归dfs(node.left...)，同时开启一条新路（但是curpath=0）
# - 更新全局变量


# 自顶向下传递信息：父亲节点告诉子节点要向左还是向右
# 自底向上返回值：上报/全局更新，需要遍历完所有子树，才可以得到self.maxpath

class Solution:
    def __init__(self):
        self.maxpath = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, True)
        self.dfs(root, 0, False)
        return self.maxpath
    
    def dfs(self, node, curlen, left):
        if not node:
            return
        if left==True:
            self.dfs(node.right, curlen+1, False)
            # 去左边，之前的断了，所以新路径从这里跨向左边，边长一定是1
            self.dfs(node.left, 1, True)
        if left==False:
            self.dfs(node.left, curlen+1, True)
            self.dfs(node.right, 1, False)
        self.maxpath = max(self.maxpath, curlen)
        