# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS三部曲：
# 1. 返回值含义：如果找到了该节点，则返回节点值
# 2. 终止条件：如果当前节点为空节点，则返回空
# 3. 单层递归的逻辑
# - 如果当前节点值比val要小，那么找右子树
# - 如果当前节点值比val要大，那么找左子树
# - 如果当前节点值和val一样，则返回当前节点

# 时间复杂度：一般情况下时间复杂度为O(h)，平衡BST为O(logn)，最坏退化BST为O(n)
# 空间复杂度：一般情况下为O(h)，平衡BST为O(logn)，退化BST为O(n)
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None
        if root.val>val:
            return self.searchBST(root.left, val)
        elif root.val<val:
            return self.searchBST(root.right, val)
        elif root.val==val:
            return root
        return None