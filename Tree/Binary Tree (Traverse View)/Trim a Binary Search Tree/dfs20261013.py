# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（通过递归返回值，连接修剪后的左右子树）
# 2. 递归三部曲
#（1）递归函数的参数和返回值：参数就是root（当前需要修剪的子树的根节点）和low（允许保留的最小值）和high（允许保留的最大值），返回值就是经过修剪后的子树的根节点
#（2）终止条件：遇到空节点则直接返回None（当前子树不存在）
#（3）单层递归的逻辑
# - root.val<low: 递归右子树，返回右子树符合条件的头节点（当前子树的左子树一定都小于low，不满足要求）
# - root.val>high: 递归左子树，返回左子树符合条件的头节点（当前子树的右子树一定都大于high，不满足要求）
# - low<=root.val<=high: 当前节点符合要求，需要保留，因此递归修剪其左右子树

# 时间复杂度：O(n) 
# 本题可能需要递归左右两个子树，因此最坏情况下需要访问整棵子树
# 空间复杂度：O(h) 
# 空间复杂度来自递归调用栈，顺序递归左右子树，不是同时递归左右子树，因此其空间复杂度仍为O(h)，而不是O(n)
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        if root is None:
            return None
        if root.val<low:
            return self.trimBST(root.right, low, high)
        if root.val>high:
            return self.trimBST(root.left, low, high)
        if low<=root.val<=high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root