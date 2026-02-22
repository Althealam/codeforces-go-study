# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, not_rob = self.steal(root)
        return max(rob, not_rob)
    
    def steal(self, root):
        if not root:
            return (0, 0)
        left_rob, left_not_rob = self.steal(root.left)
        right_rob, right_not_rob = self.steal(root.right)
        rob = root.val+left_not_rob+right_not_rob
        not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)
        return rob, not_rob