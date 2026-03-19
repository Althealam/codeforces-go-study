# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分解问题：要获取一个节点数为n的满二叉树的数量，可以分别假设左右子树的节点数，并且获取左右子树为满二叉树时的组合数
# 满二叉树的性质：
# 1. 节点数量一定为奇数
# 2. 左右子树叶一定是满二叉树
# 3. 每个节点的子节点为0个或者2个

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        full_binary_trees = []
        if n%2==0:
            return full_binary_trees
        if n==1:
            full_binary_trees.append(TreeNode(0))
            return full_binary_trees
        for i in range(1, n, 2): # 遍历左子树的节点数量，并且一定要确保满二叉树的节点总数为奇数
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(n-1-i)
            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(0, left_subtree, right_subtree)
                    full_binary_trees.append(root)
        return full_binary_trees
