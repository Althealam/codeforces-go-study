#
# @lc app=leetcode.cn id=971 lang=python3
# @lcpr version=30403
#
# [971] 翻转二叉树以匹配先序遍历
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
#（1）携带参数和返回值含义：参数为当前遍历的节点，以及当前遍历到voyage数组的第几个元素的index，需要反转的结果数组res，返回值为true/false，表示当前节点是否和当前ind的值匹配
#（2）终止条件：如果当前节点为空，则直接返回true
#（3）单层递归的逻辑
# - 判断当前节点值是否和voyage的节点对的上，对不上的话则直接返回false（因为翻转只能交换左右子树，对当前节点没帮助，所以可以直接返回[-1]）
# - 判断是否需要翻转当前节点的左右子树
#   - 如果node.left.val!=voyage[ind] -> 翻转左右子树 -> 记录当前节点的值到res数组中，更新ind -> 递归右子树和左子树
#   - 如果node.left.val==voyage[ind] -> 不需要翻转左右子树 -> 递归左子树和右子树
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        ind = 0
        def dfs(node):
            nonlocal res, ind
            if not node:
                return True
            if node.val!=voyage[ind]:
                return False
            ind+=1
            if node.left and ind<len(voyage) and node.left.val!=voyage[ind]:
                res.append(node.val)
                return dfs(node.right) and dfs(node.left)
            else:
                return dfs(node.left) and dfs(node.right)
        if dfs(root) and ind==len(voyage):
            return res
        return [-1]
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
sol = Solution()
voyage = [2, 1]
res = sol.flipMatchVoyage(root, voyage)
print(res)
# @lc code=end



#
# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

#

