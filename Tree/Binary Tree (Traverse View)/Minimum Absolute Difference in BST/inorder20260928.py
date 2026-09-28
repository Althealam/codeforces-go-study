# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        self.inorder(root, res)
        ans = float('inf')
        for i in range(len(res)):
            if i>0 and abs(res[i]-res[i-1])<ans:
                ans = abs(res[i]-res[i-1])
        return ans
    
    def inorder(self, root, res):
        if not root:
            return None
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)