# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 2. DFS三部曲：获取以node为根节点的子树能够到达的最大深度
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根节点的子树能够到达的最大深度，当前找到的最小子树的根节点
#（3）终止条件：如果node为空节点的话，则返回(0, None)
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的最大深度leftdepth, rightdepth
# - if leftdepth==rightdepth: 说明最深的节点均匀的分布在左右子树中，因此这是最小的公共祖先，返回(leftdepth+1, node)
# - if leftdepth>rightdepth: 说明最深的节点在左子树中，返回(leftdepth+1, node.left)
# - if leftdepth<rightdepth: 说明最深的节点在右子树中，返回(rightdepth+1, node.right)

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth, node = self.dfs(root)
        return node
    
    def dfs(self, node):
        if not node:
            return (0, None)
        leftdepth, leftnode = self.dfs(node.left)
        rightdepth, rightnode = self.dfs(node.right)
        if leftdepth==rightdepth:
            return (leftdepth+1, node)
        elif leftdepth>rightdepth:
            return (leftdepth+1, leftnode)
        else:
            return (rightdepth+1, rightnode)