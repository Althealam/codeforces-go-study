# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        ans = 0
        def dfs(cur, parent, grandparent):
            nonlocal ans
            if not cur:
                return 
            if grandparent is not None and grandparent.val%2==0:
                ans+=cur.val
            dfs(cur.left, cur, parent)
            dfs(cur.right, cur, parent)
        dfs(root, None, None)
        return ans