# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1. 题目类型：自底向上
# 2. DFS三部曲：用于获取以node为根节点的子树的字符串的表示
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根节点的子树的字符串的表示
#（3）终止条件：遇到空节点，则直接返回
#（4）单层递归的逻辑
# 获取左右子树的递归情况
# 将当前节点的值加入到当前字符串中
# 判断一下leftstr和rightstr的情况
# - 如果leftstr为""，以及rightstr为""，说明该节点应该是叶子节点，则加入""
# - 如果leftstr不为""，以及rightstr为""，则加入"("+leftstr+")"
# - 如果leftstr不为""，以及rightstr不为""，则加入"("+left+")"和"("+right+")"
# - 如果leftstr为""，以及rightstr为""，则什么都不加入

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return ""
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        cur = str(node.val)

        if left is "" and right is "":
            return cur
        elif left is not "" and right is "":
            return str(node.val)+"("+left+")"
        elif left is "" and right is not "":
            return str(node.val)+"()"+"("+right+")"
        else:
            return str(node.val)+"("+left+")"+"("+right+")"