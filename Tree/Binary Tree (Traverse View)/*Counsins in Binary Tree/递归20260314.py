# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# - 获取x和y的深度和父亲节点
# * 如果depth_x == depth_y and parent_x == parent_y: return True 
# * 使用traversal来寻找

class Solution:
    def __init__(self):
        self.depth_x = 0
        self.depth_y = 0
        self.parent_x = None
        self.parent_y = None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.traversal(root, 0, None, x, y)
        if self.depth_x==self.depth_y and self.parent_x!=self.parent_y:
            return True
        return False

    def traversal(self, root, depth, parent, x, y):
        if root is None:
            return 
        if root.val==x:
            self.parent_x = parent
            self.depth_x = depth
        if root.val==y:
            self.parent_y = parent
            self.depth_y = depth
        self.traversal(root.left, depth+1, root, x, y)
        self.traversal(root.right, depth+1, root, x, y)
        