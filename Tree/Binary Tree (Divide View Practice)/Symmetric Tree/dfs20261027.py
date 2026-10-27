#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30404
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自顶向下（先序遍历）
# 递归三部曲
#（1）携带参数和返回值含义
# - 携带参数：当前遍历的节点1和节点2
# - 返回值含义：当前节点1和节点2是否为轴对称的
#（2）终止条件：
# 如果当前节点为空，则返回True
# 如果当前节点的左右子节点为空，则返回True
# 如果当前节点的左节点为空/右节点为空，则返回False
#（3）单层递归的逻辑
# 如果当前节点的左右子节点不为空，并且节点值相同，则递归dfs(cur.left.left, cur.right.right) and dfs(cur.left.right, cur.right.left)
# 如果当前节点的左右子节点不为空，并且节点值不同，则直接返回False
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val!=right.val:
                return False
            if left.val==right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            return False
        return dfs(root.left, root.right)
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

