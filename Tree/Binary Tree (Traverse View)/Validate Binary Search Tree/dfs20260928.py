# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs三部曲：
# 1. 返回参数及含义：当前以node为根的子树，在(lower, upper)范围内是否是一颗合法的BST
# 2. 携带参数：
# node
# lower：当前节点允许的最小值
# upper：当前节点允许的最大值
# 3. 终止条件：
# node is None -> True
# node.val<=lower or node.val>=upper -> false
# 4. 单层递归的逻辑
# - 左子树：范围变成(lower, node.val)
# - 右子树：范围变成(node.val, upper)
# - 左右都合法才返回True

# 时间复杂度：O(n)，最坏情况下需要将整棵树的每个节点都检查一遍，并且对于每个节点只是执行常数操作
# 空间复杂度：递归调用栈，O(h)，其中h是树的高度
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        def dfs(node, lower, upper):
            if node is None:
                return True
            if node.val<=lower or node.val>=upper:
                return False
            return (
                dfs(node.left, lower, node.val)
                and
                dfs(node.right, node.val, upper)
            )
        return dfs(root, float('-inf'), float('inf'))