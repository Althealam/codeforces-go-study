# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 在整棵树里面，找到一个严格大于root.val的最小值
# 1. 遇到比最小值大的节点，则当作候选
# 2. 遇到等于最小值的节点，则向下递归

# DFS三部曲：返回以node为根的子树的第二小候选值
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根节点的子树中，严格大于最小值node.val的最小节点值
#（3）终止条件
# - 如果当前节点为空，则返回-1（说明已经找完了整颗子树）
# - 如果node.val>root.val，说明已经找到了，则直接返回node.val
#（4）单层递归的逻辑
# 注意：node.val和root.val只有两种情况：node.val<root.val或者node.val=root.val
# 如果node.val==root.val，说明要去左右子树找
# - 调用递归获取左右子树的值 left和right
#   - 如果left==-1 and right!=-1: return right
#   - 如果left!=-1 and right==-1: return left
#   - 如果left!=-1 and right!=-1: return min(left, right)

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root)

    def dfs(self, node, parent):
        if not node:
            return -1
        if node.val>parent.val:
            return node.val
        if node.val==parent.val:
            left = self.dfs(node.left, node)
            right = self.dfs(node.right, node)
            if left==-1 and right!=-1:
                return right
            elif left!=-1 and right==-1:
                return left
            elif left!=-1 and right!=-1:
                return min(left, right)
            else:
                return -1