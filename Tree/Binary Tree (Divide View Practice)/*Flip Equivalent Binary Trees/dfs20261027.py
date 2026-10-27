#
# @lc app=leetcode.cn id=951 lang=python3
# @lcpr version=30404
#
# [951] 翻转等价二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自顶向下
# 递归三部曲
#（1）携带参数和返回值含义
# - 携带参数：当前遍历的节点cur1和cur2
# - 返回值含义：是否能通过翻转/不翻转操作保持一致，如果可以的话则返回true，不行的话则返回false
#（2）终止条件
# - 如果cur1和cur2为空，则返回true
# - 如果cur1或cur2为空，则返回false
# - 如果cur1.val!=cur2.val，则返回false
#（3）单层递归的逻辑
# 1. 不进行翻转
# cur1.left和cur2.left是否翻转等价
# cur1.right和cur2.right是否翻转等价
# 2. 进行翻转
# cur1.left和cur2.right是否翻转等价
# cur1.right和cur2.left是否翻转等价
# 上述两种情况其中一种成立则返回true

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(cur1, cur2):
            if cur1 is None and cur2 is None:
                return True
            if cur1 is None or cur2 is None:
                return False
            if cur1.val!=cur2.val:
                return False
            if dfs(cur1.left, cur2.left) and dfs(cur1.right, cur2.right):
                return True
            else:
                return dfs(cur1.left, cur2.right) and dfs(cur1.right, cur2.left)
        return dfs(root1, root2)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[1]\n
# @lcpr case=end

#

