# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST的性质
# 1. 左右子树也一定是BST

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        return self.build(1, n)
    
    def build(self, left, right):
        """给定区间left和right，返回在这区间内的BST的数量"""
        if left>right:
            return [None] # 一定要判断一下left和right，否则的话会无限递归
        res = []
        for i in range(left, right+1): # 遍历根节点
            lefttrees = self.build(left, i-1)
            righttrees = self.build(i+1, right)
            for l in lefttrees:
                for r in righttrees:
                    root = TreeNode(i, l, r)
                    res.append(root)
        return res


