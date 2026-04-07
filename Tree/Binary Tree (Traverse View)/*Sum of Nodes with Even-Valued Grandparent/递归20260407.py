# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲: dfs(node, p_val, gp_val)
#（1）递归函数的返回值和含义：子节点需要告诉我其所有符合条件的节点值，因此返回值是累加和
#（2）递归函数需要携带的信息：parent, grandparent
#（3）终止条件：如果root为空，则直接返回0
#（4）单层递归的逻辑
# - 如果grandparent的值是偶数，那么当前节点的值就是我们要找的孙子，将其值累加和
# - 向下传承
#   - 对于该节点的儿子来说，该节点变成了parent，而该节点的父亲节点变成了grandparent
#   - 递归调用：left_sum = dfs(child, me, my_father)

class Solution:
    def __init__(self):
        self.res = 0

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0, 0)
        return self.res
    
    def dfs(self, node, p_val, gp_val):
        if node is None:
            return 0
        if gp_val!=0 and gp_val%2==0:
            self.res+=node.val
        self.dfs(node.left, node.val, p_val)
        self.dfs(node.right, node.val, p_val)

        