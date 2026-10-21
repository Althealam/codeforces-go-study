class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(cur, val):
            if not cur: 
                return TreeNode(val)
            if val>cur.val:
                new_root = TreeNode(val)
                new_root.left = cur
                return new_root
            cur.right = dfs(cur.right, val)
            return cur
        return dfs(root, val)