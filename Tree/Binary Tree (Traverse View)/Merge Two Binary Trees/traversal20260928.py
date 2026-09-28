# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs三部曲：
# 1. 返回值含义：返回root1和root2合并后的根节点
# 2. 终止条件：
# - root1为空：返回root2
# - root2为空：返回root1
# 3. 单层递归逻辑
# - root1.val+=root2.val
# - root1.left=合并两棵树的左子树
# - root1.right=合并两棵树的右子树
# - 返回root1

# DFS遍历树，如果每个节点只处理一次，而且单个节点的处理是O(1)，通常时间复杂度为O(n)
# 时间复杂度：时间复杂度取决于两棵树结构中需要递归比较的位置数量，因此为O(k)
# 空间复杂度：O(h)，递归dfs，没有创建新的树，并且直接修改root1，因此额外空间来自递归调用栈，此时的递归深度为h，最坏情况下为n
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None
        elif root1 is None and root2 is not None:
            return root2
        elif root1 is not None and root2 is None:
            return root1
        else:
            root1.val+=root2.val
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1