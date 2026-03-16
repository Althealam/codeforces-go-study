# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 记录从根节点到startValue和destValue的路径startPath和destPath
# 2. 去除startPath和destPath的公共前缀
# 3. 将startPath全部变成U，将startPath和destPath拼接在一起，就是题目要求的路径
class Solution:
    def __init__(self):
        self.path = ''
        self.startPath = ''
        self.destPath = ''
        self.startValue = 0
        self.destValue = 0

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startValue = startValue
        self.destValue = destValue

        # 1. 寻找走到startValue和destValue的方向路径
        self.traversal(root)
        
        # 2. 去除两个方向路径的公共前缀
        p = 0
        while p<len(self.startPath) and p<len(self.destPath) and self.startPath[p]==self.destPath[p]:
            p+=1
        self.startPath = self.startPath[p:]
        self.destPath = self.destPath[p:]

        # 3. 将走向startValue的方向路径全部变成U
        self.startPath = 'U'*len(self.startPath)
        # 组合startPath和destPath
        return self.startPath+self.destPath
    
    def traversal(self, root):
        """从root出发寻找startValue和destValue"""
        if root is None:
            return 
        if root.val==self.startValue:
            self.startPath = self.path
        elif root.val==self.destValue:
            self.destPath = self.path
        
        # 二叉树遍历框架
        self.path+='L'
        self.traversal(root.left)
        self.path = self.path[:-1]

        self.path+='R'
        self.traversal(root.right)
        self.path = self.path[:-1]