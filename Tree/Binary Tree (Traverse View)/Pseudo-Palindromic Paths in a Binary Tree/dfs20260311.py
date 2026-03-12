# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = [0]*10 # 当前路径下的频率统计
        self.res = 0

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.res
    
    def traversal(self, root):
        if root is None:
            return
        self.count[root.val]+=1
        if root.left is None and root.right is None:
            # 遇到叶子节点，判断是否是回文串
            odd = 0
            for n in self.count: #  遍历所有的数字，判断一下奇数出现的次数
                if n%2==1:
                    odd+=1
            if odd<=1:
                self.res+=1 # 更新回文串数量
        self.traversal(root.left)
        self.traversal(root.right)
        self.count[root.val]-=1
