#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30404
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自顶向下
# 全局变量：节点值之和等于targetSum的路径的数量ans

# dfs1: 用来找从固定起点开始的路径
# 递归三部曲
#（1）携带参数和返回值含义：当前节点cur，当前路径总和pathsum
#（2）终止条件：如果当前节点为空，则直接返回
#（3）单层递归的逻辑
# - 更新当前路径总和
# - 判断当前路径总和是否满足条件，如果是的话则更新答案值
# - 递归左右子节点

# dfs2：用来遍历整棵树，找到所有可行的起点
# 递归三部曲
#（1）携带参数和返回值含义：当前节点cur
#（2）终止条件：如果当前节点为空则直接返回
#（3）单层递归的逻辑
# - 用dfs1获取以当前节点为起点的所有路径的情况
# - 用dfs2递归左右子树
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        def dfs(cur, pathsum):
            nonlocal ans
            if not cur:
                return
            pathsum+=cur.val
            if pathsum==targetSum:
                ans+=1
            dfs(cur.left, pathsum)
            dfs(cur.right, pathsum)

        def traversal(cur):
            if not cur:
                return 
            dfs(cur, 0)
            traversal(cur.left)
            traversal(cur.right)

        traversal(root)
        return ans

# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

