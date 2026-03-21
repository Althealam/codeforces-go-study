# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 满二叉树的性质：
# 1. 节点数量一定为奇数
# 2. 左右子树也一定是满二叉树

# 注意：本题的要求返回值为list[TreeNode]，因为返回列表，并且列表中存储的是树节点
# 分解问题：定义一个子函数来获取给定节点数量时的满二叉树的可能组合，然后分别获取左右子树的可能组合

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = self.build(n)
        return res
    
    def build(self, n):
        res = []
        if n==0:
            return [None] # 返回空二叉树
        if n==1:
            return [TreeNode(0)]
        if n%2==0:
            return [] # 无法构建二叉树
        for i in range(n): # 遍历左子树的节点数量
            left = i # 左子树的节点数
            right = n-1-i # 右子树的节点数
            left_trees = self.build(left)
            right_trees = self.build(right)
            for left_tree in left_trees: # 递归左子树
                for right_tree in right_trees: # 递归右子树
                    root = TreeNode(0, left_tree, right_tree)
                    res.append(root)
        return res

        