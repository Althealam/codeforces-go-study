# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 2. DFS三部曲
#（1）返回值含义：经过反转后的当前节点
#（2）携带参数：当前节点
#（3）终止条件：如果当前节点为空节点，则直接返回None
#（4）单层递归的逻辑
# - 调用递归反转左子树
# - 调用递归反转右子树
# - 处理当前节点
#   - 反转左右子节点
#   - 返回当前节点

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
    
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.dfs(node.right)
        old_left = node.left
        old_right = node.right
        node.left = old_right
        node.right = old_left

        