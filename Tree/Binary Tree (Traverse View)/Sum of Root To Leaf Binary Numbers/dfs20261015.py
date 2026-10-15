#
# @lc app=leetcode.cn id=1022 lang=python3
# @lcpr version=30403
#
# [1022] 从根到叶的二进制数之和
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
#（1）携带参数和返回值含义：参数为当前的节点值以及当前路径，无返回值
#（2）终止条件：遇到空节点则直接返回，遇到叶子节点则获取当前路径的十进制数，并且更新一下答案值
#（3）单层递归的逻辑
# 如果当前节点不是叶子节点，则将当前节点更新到当前路径中，并且递归左右子树
# 回溯

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, curpath):
            nonlocal res
            if not node:
                return 
            curpath*=2
            curpath+=node.val
            if node.left is None and node.right is None:
                # 获取当前路径的十进制数
                # 4 = 1*2^2+0*2^1+0*2^0
                # 0
                # 1*2^0
                # 1*2^1+0*2^0
                # 1*2^2+0*2^1+0*2^0
                res+=curpath
                return
            else:
                dfs(node.left, curpath)
                dfs(node.right, curpath)

            # 回溯
            curpath-=node.val
            curpath/=2
        dfs(root, 0)
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
sol = Solution()
res = sol.sumRootToLeaf(root)
print(res)
                
# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

