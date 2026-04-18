# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：以node为根节点的子树，按照题目要求构造出的字符串
#（1）携带参数：当前节点
#（2）返回值含义：以node为根节点的子树，构造出的字符串
#（3）终止条件：如果当前节点为空节点，则返回空字符串
#（4）单层递归的逻辑
# - 获取左右子树的字符串
# - 将当前节点值变成字符串cur = str(node.val)
# - 如果左右孩子都没有，则直接返回cur
# - 如果只有左孩子，则返回str(node.val)+"("+left+")"
# - 如果只有右孩子，则返回str(node.val)+"()"+"("+right+")"
# - 如果左右孩子都有，则返回str(node.val)+"("+left+")"+"("+right+")"

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return ""
        leftstr = self.dfs(node.left)
        rightstr = self.dfs(node.right)
        cur = str(node.val)
        if leftstr is "" and rightstr is "":
            return cur
        elif leftstr is not "" and rightstr is "":
            return str(node.val)+"("+leftstr+")"
        elif leftstr is "" and rightstr is not "":
            return str(node.val)+"()"+"("+rightstr+")"
        else:
            return str(node.val)+"("+leftstr+")"+"("+rightstr+")"