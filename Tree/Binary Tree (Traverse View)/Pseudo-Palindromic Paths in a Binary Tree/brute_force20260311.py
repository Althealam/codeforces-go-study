# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = []
        self.traversal(res, [], root)
        return len(res)
    
    def traversal(self, res, path, root):
        if root is None:
            return 
        path.append(root.val)
        if root.left is None and root.right is None:
            if self.check_pseudo_palindromic(path[:]):
                res.append(path[:])
        if root.left:
            self.traversal(res, path, root.left)
            path.pop()
        if root.right:
            self.traversal(res, path, root.right)
            path.pop()

    
    def check_pseudo_palindromic(self, arr):
        frequency = {}
        odd = 0 # frequency=1
        for num in arr:
            frequency[num] = frequency.get(num, 0)+1
        
        for num, freq in frequency.items():
            if freq%2==1:
                odd+=1
                if odd>1:
                    return False
        return True
        
            
