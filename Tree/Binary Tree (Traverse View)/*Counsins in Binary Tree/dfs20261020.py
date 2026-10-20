#
# @lc app=leetcode.cn id=993 lang=python3
# @lcpr version=30404
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 是堂兄弟节点的条件：
# depthA=depthB and parentA!=parentB

# 目标：dfs遍历二叉树，寻找x和y的节点
# 题目类型：自顶向下
# 递归三部曲
#（1）携带参数和返回值含义：当前遍历的节点node，当前节点的父节点parent，当前深度curdepth；返回值为空
#（2）终止条件：遇到空节点则直接返回true；
#（3）单层递归的逻辑
# 判断当前节点的值是否和x/y相等，如果是的话则更新x/y的info，不是的话则递归左右子树
# 更新当前节点的父亲节点和深度

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_info = {'depth': 0, 'parent': None}
        y_info = {'depth': 0, 'parent': None}
        def dfs(node, curdepth, parent):
            # 终止条件
            if not node:
                return 
            # 单层递归的逻辑
            if node.val==x:
                x_info['depth'] = curdepth
                x_info['parent'] = parent
            if node.val==y:
                y_info['depth'] = curdepth
                y_info['parent'] = parent
            # 递归左右子树
            dfs(node.left, curdepth+1, node)
            dfs(node.right, curdepth+1, node)
        dfs(root, 0, None)

        if x_info['depth']==y_info['depth'] and x_info['parent']!=y_info['parent']:
            return True
        return False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
sol = Solution()
res = sol.isCousins(root, 5, 4)
print(res)

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4,null,5]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4]\n2\n3\n
# @lcpr case=end

#

