# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：右中左
# 递归三部曲
#（1）递归函数参数及返回值：参数为当前处理的节点，没有返回值
#（2）终止条件：如果当前节点为空则直接返回None
#（3）单层递归的逻辑
# 更新当前节点的值
# 更新前一个节点的值

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre = 0
        self.dfs(root)
        return root
    
    def dfs(self, node):
        if not node:
            return None
        self.dfs(node.right)
        node.val+=self.pre
        self.pre = node.val
        self.dfs(node.left)