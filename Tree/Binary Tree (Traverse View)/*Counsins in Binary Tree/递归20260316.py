# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 记录每个结点的父亲节点和深度
# 2. 递归遍历，判断一下当前的节点的值是否等于x，如果root.val=x则更新父亲节点和深度


class Solution:
    def __init__(self):
        self.depth_x = 0
        self.depth_y = 0
        self.father_x = None
        self.father_y = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.traversal(root, None, 0, x, y)
        if self.depth_x==self.depth_y and self.father_x!=self.father_y:
            return True
        return False

    def traversal(self, node, father, depth, x, y):
        if node is None:
            return 
        if node.val == x:
            self.depth_x = depth
            self.father_x = father
        if node.val == y:
            self.depth_y = depth
            self.father_y = father
        self.traversal(node.left, node, depth+1, x, y)
        self.traversal(node.right, node, depth+1, x, y)
        
        