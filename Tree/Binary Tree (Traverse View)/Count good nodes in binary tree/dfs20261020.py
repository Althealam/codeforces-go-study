#
# @lc app=leetcode.cn id=1448 lang=python3
# @lcpr version=30404
#
# [1448] 统计二叉树中好节点的数目
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自顶向下
# 额外定义：全局变量ans，用来统计好节点的数量
# 递归三部曲
#（1）携带参数和返回值含义：当前节点cur，当前路径下的最大值maxval；返回值为空
#（2）终止条件：
# - 遇到空节点则直接返回
#（3）单层递归的逻辑
# - 更新当前路径下的最大值maxval
# - 如果当前节点的值超过了maxval，则更新maxval，并且更新ans
# - 如果当前节点的值没超过maxval，则后续还有可能有路径合法，继续递归左右子节点
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, maxval):
            nonlocal ans
            if not node:
                return 
            if node.val>=maxval:
                ans+=1
                maxval = node.val
            dfs(node.left, maxval)
            dfs(node.right, maxval)
        dfs(root, float('-inf'))
        return ans

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
sol = Solution()
res = sol.goodNodes(root)
print(res)

# @lc code=end



#
# @lcpr case=start
# [3,1,4,3,null,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,null,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

