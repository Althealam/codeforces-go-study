# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# n是binary tree的节点数
# h是树的高度
# L是叶子节点的数量

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = [] # space: O(h)
        return self.traversal(root, "~", path) # time: O(n+Lh) space: O(h)
    
    def traversal(self, root, res, path):
        if root is None:
            return 
        path.append(chr(ord('a')+root.val)) 
        if root.left is None and root.right is None:
            s = "".join(reversed(path[:])) # time: O(h) (cause path[:] and reversed function)
            res = min(res, s)
        if root.left:
            res = self.traversal(root.left, res, path)
            path.pop()
        if root.right:
            res = self.traversal(root.right, res, path)
            path.pop()
        return res