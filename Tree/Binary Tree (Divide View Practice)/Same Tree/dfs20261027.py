#
# @lc app=leetcode.cn id=100 lang=python3
# @lcpr version=30404
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自底向上（后序遍历）
# DFS：判断以root1和root2为根节点的子树是否相同
# 递归三部曲
#（1）携带参数和返回值含义
# - 携带参数：两棵子树的根节点root1和root2
# - 返回值含义：两棵子树是否相同，相同为true，否则为false
#（2）终止条件
# - 如果root1 is None and root2 is None: return true
# - 如果root1 is None or root2 is None: return false
# - 如果root1.val!=root2.val: return false
#（3）单层递归的逻辑
# - 调用递归判断左右子树是否相同
# - 判断当前两棵子树的根节点
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def dfs(root1, root2):
            # 终止条件
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val!=root2.val:
                return False
            # 后序遍历
            left = dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)
            if left is False or right is False:
                return False
            if root1.val==root2.val and left and right:
                return True
            return False
        return dfs(p, q)
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1]\n[1,1,2]\n
# @lcpr case=end

#

