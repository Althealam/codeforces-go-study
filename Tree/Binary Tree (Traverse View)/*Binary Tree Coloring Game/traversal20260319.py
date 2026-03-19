# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 找到x的节点所在的位置
# 2. 获取x.left和x.right的节点数量，以及x的父亲节点的子树的数量
# 3. 判断一下最大值是否超过n//2，如果超过的话可以赢

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        x_node = self.traversal(root, x)
        left_count = self.count(x_node.left)
        right_count = self.count(x_node.right)
        other_count = n-1-left_count-right_count
        max_count = max(max(left_count, right_count), other_count)
        return max_count>n//2
    
    def traversal(self, root, x):
        """
        在root中寻找x的节点
        1. 是否要遍历所有节点：是的
        2. 什么时候进行操作：if root.val==x: return root
        3. 是否要记录子节点：否
        """
        if not root:
            return 
        if root.val==x:
            return root
        return self.traversal(root.left, x) or self.traversal(root.right, x)
    
    def count(self, node):
        if not node:
            return 0
        return 1+self.count(node.left)+self.count(node.right)
