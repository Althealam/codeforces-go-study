# Definition for a binary tree node.

# [1, 0, 0] ==> 1*(2^2)+0*(2^1)+0*(2^0) = 4
# [1, 0, 1] ==> 1*(2^2)+0*(2^0)+1*(2^0) = 5

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_ = 0

    def sumRootToLeaf(self, root) -> int:
        self.traversal(root, []) # 时间复杂度：O(nh)，其中n是节点的总数，h是树木的高度
        # 空间复杂度：O(h)，最坏为O(n)，深度优先遍历，栈的层数等于当前路径的长度，因此O(h)，当为单链的时候为O(n)
        return self.sum_
    
    def traversal(self, root, path):
        """给定root，获取所有到叶子节点的路径"""
        if root is None:
            return 
        path.append(root.val)
        if root.left is None and root.right is None:
            self.sum_+=self.return_num(path[:])
            print(f"current path is {path[:]}")
            print(f"current num is {self.return_num(path[:])}")
        self.traversal(root.left, path)
        self.traversal(root.right, path)
        path.pop()
    
    def return_num(self, path):
        """给定路径，还原对应的二进制数"""
        res = 0
        for i in range(len(path)):
            res+=path[i]*(2**(len(path)-i-1))
        return res
        
root = TreeNode(val = 1)
root.left = TreeNode(val=0)
root.right = TreeNode(val=1)
root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=1)
root.right.left = TreeNode(val=0)
root.right.right = TreeNode(val=1)
sol = Solution()
res  = sol.sumRootToLeaf(root)
print(res)