# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型
# - 自顶向下：传递相对深度，每次递归深入一层，就在结果上加1（这个部分是在回溯计算的）
# - 自底向上：根据子节点的情况，来决定父亲节点是不是拥有最深节点的子树的根
# 2. DFS三部曲：获取node最大深度，以及以node为根节点的子树的候选答案
#（1）携带参数：当前节点
#（2）返回值含义：在当前节点为根的子树中，能达到的最大深度；这颗子树中，包含其下方所有最深节点的最小子树的根
#（3）终止条件：如果当前节点为None，则返回0以及None
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的深度leftdepth, rightdepth
# - leftdepth==rightdepth: 当前节点是目前发现的包含所有最深节点的最小子树候选者
# - leftdepth>rightdepth：包含最深节点的子树的根节点在左子树中
# - leftdepth<rightdepth：包含最深节点的子树的根节点在右子树中


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth, node = self.dfs(root)
        return node
    
    def dfs(self, node):
        if not node:
            return (0, None)
        # 获取左右子树的深度
        leftdepth, leftnode = self.dfs(node.left)
        rightdepth, rightnode = self.dfs(node.right)
        if leftdepth==rightdepth:
            return (leftdepth+1, node)
        elif leftdepth>rightdepth:
            return (leftdepth+1, leftnode)
        else:
            return (rightdepth+1, rightnode)