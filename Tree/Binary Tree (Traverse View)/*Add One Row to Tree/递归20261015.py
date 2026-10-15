#
# @lc app=leetcode.cn id=623 lang=python3
# @lcpr version=30403
#
# [623] 在二叉树中增加一行
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
#（1）携带参数和返回值含义：当前子树的根节点，整数val和深度depth，当前的深度
#（2）终止条件：如果当前节点为空节点，则直接返回；如果depth=1，那么直接新创建一个root即可
#（3）单层递归的逻辑
# 更新当前节点的深度
# 如果当前节点的深度达到了depth，那么开始创建子节点，并连接左右子树
# 如果当前节点的深度没有达到depth，那么继续递归左右子树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        def dfs(node, curdepth, val, depth):
            if not node:
                return 
            if curdepth==depth-1: # 已经到达了目标深度的上一个节点（即需要插入节点的父节点）
                # 记录旧节点
                old_left = node.left
                old_right = node.right
                # 插入新节点
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                # 连接原来的左右子树
                node.left.left = old_left
                node.right.right = old_right
                return 
            dfs(node.left, curdepth+1, val, depth)
            dfs(node.right, curdepth+1, val, depth)
        dfs(root, 1, val, depth)
        return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
sol = Solution()
res = sol.addOneRow(root, 1, 2)
print(res)            

# @lc code=end



#
# @lcpr case=start
# [4,2,6,3,1,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,null,3,1]\n1\n3\n
# @lcpr case=end

#

