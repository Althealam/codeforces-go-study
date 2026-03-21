# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST的性质
# 1. 左右子树也一定是BST

# 思路：遍历根节点的值，然后递归构建左右子树，比如根节点的值为i，那么左子树的区间为1, i-1，右子树的区间为i+1, n

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return [None]
        res = self.build(1, n)
        return res
    
    def build(self, left, right) -> List[Optional[TreeNode]]:
        """
        给定区间[left, right]，递归构建左右子树
        return: list，其中list中存储的是treenode
        """
        if left>right:
            return [None] # 必须是列表的形式，并且[]表示没有树，而[None]表示里面是空树
        res = []
        for i in range(left, right+1):
            left_trees = self.build(left, i-1) 
            # 当i=left的时候，left_trees = self.build(left, left-1)，所以要判断一下left和right的情况
            right_trees = self.build(i+1, right)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    res.append(root)
        return res