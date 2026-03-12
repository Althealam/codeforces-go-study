# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        res = self.build(1, n)
        return res
    
    def build(self, l, r):
        res = []
        if l>r:
            return [None]
        for i in range(l, r+1):
            # print(f"current root is {i}")
            left_trees = self.build(l, i-1)
            right_trees = self.build(i+1, r)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
                    print(f"current res is {res}")
        return res

        
sol = Solution()
n = 3
res = sol.generateTrees(n)
print(res)