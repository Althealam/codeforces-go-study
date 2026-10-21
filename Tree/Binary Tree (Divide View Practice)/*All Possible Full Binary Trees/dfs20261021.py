#
# @lc app=leetcode.cn id=894 lang=python3
# @lcpr version=30404
#
# [894] 所有可能的真二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# n=1+left+right
# 其中left和right是左右子树的节点数

# 题目类型：自顶向下
# 递归三部曲
#（1）携带参数和返回值的含义：
# - 参数：n表示当前需要构造的真二叉树包含多少个节点
# - 返回值：返回一个列表，其中包含所有由n个节点组成的真二叉树的根节点
#（2）终止条件
# - 如果n==1，那么只有一种真二叉树，则直接返回[TreeNode(0)]
# - 如果n%2==0，那么没有真二叉树，则直接返回[]
#（3）单层递归的逻辑
# - 枚举左子树的节点数量，由此得到右子树的节点数量
# - 递归调用dfs，得到左右子树可能的真二叉树的列表
# - 遍历左右子树的真二叉树列表，将其组合在一起，得到符合条件的真二叉树列表


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        def dfs(n):
            if n==1:
                return [TreeNode(0)]
            if n%2==0:
                return []
            ans = []
            # 枚举所有的左子树的节点数量
            for l in range(1, n, 2):
                r = n-1-l # 右子树的节点数量

                # 递归得到所有可能的左右子树
                left_trees = dfs(l)
                right_trees = dfs(r)

                # 枚举所有的左右子树的组合
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
        return dfs(n)
        
# @lc code=end



#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

