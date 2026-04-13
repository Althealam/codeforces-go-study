# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：以当前节点为起点，向其子树延伸的相同数值节点的最长单边路径长度
#（1）携带参数：node
#（2）返回值含义：以node为根节点的子树中，和node.val相同的最长路径的长度
#（3）终止条件：如果node为空节点，则直接返回0
#（4）单层递归的逻辑
# - 获取左右子树的情况：左右子树能够提供的最长单边同值路径长度
# - 判断当前节点与子节点是否相等
#   - 如果node.val==node.left.val: left = left_len+1
#   - 如果node.val==node.right.val: right = right_len+1
# - 更新全局最大值：以当前节点为拐点的同值路径的最大长度是left+right，同时更新max_path
# - 将这个值返回给父亲节点

# 注意：路径的含义是不可以有分叉
# 比如，如果你的父亲节点想要通过你构成一条更长的路径，那么这条路径必须是F->U->左子树/右子树
# 如果将left+right返回给父亲，会导致U出现分叉
class Solution:
    def __init__(self):
        self.max_val = float('-inf')

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.max_val

    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # left_len和right_len分别表示左右子树的贡献值
        # 也就是从子节点出发的相同数值节点的最长单边路径长度

        left_len = 0
        right_len = 0
        if node.left and node.val==node.left.val:
            left_len = left+1
        if node.right and node.val==node.right.val:
            right_len = right+1
        self.max_val = max(self.max_val, left_len+right_len)
        return max(left_len, right_len) # 返回单边的值