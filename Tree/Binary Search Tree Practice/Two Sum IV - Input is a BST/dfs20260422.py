# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dfs(root)
        i, j = 0, len(self.res)-1
        # 双指针遍历
        while i<j:
            sum_val = self.res[i]+self.res[j]
            if sum_val<k:
                i+=1
            elif sum_val>k:
                j-=1
            else:
                return True
        return False
    
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)
