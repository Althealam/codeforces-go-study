#
# @lc app=leetcode.cn id=129 lang=python3
# @lcpr version=30403
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. 递归三部曲
#（1）携带参数和返回值含义：当前遍历的节点node，当前路径之和sum_，返回值为当前路径之和
#（2）终止条件：遇到空节点则直接返回；遇到叶子节点则更新答案值，即所有路径之和，同时清空当前路径之和
#（3）单层递归的逻辑
# - 处理单层节点：sum_ = sum_*10+node.val，并递归处理左右子节点
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node, sum_):
            nonlocal res
            if not node:
                return 
            sum_ = sum_*10+node.val
            if node.left is None and node.right is None:
                res+=sum_
                sum_ = 0
            else:
                dfs(node.left, sum_)
                dfs(node.right, sum_)
        
        dfs(root, 0)
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
sol = Solution()
res = sol.sumNumbers(root)
print(res)
# @lc code=end

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#

 我的这段代码有什么问题吗