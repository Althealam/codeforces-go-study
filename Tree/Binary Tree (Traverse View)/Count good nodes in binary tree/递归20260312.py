# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        self.traversal(root, root.val)
        return self.res
    
    def traversal(self, node, path_max):
        if not node:
            return 
        if path_max<=node.val:
            self.res+=1
        path_max = max(path_max, node.val)
        self.traversal(node.left, path_max)
        self.traversal(node.right, path_max)
        