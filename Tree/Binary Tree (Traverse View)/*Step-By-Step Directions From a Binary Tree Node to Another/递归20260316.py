# Definition for a binary tree node.
from re import S


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. 记录从根节点到startValue和destValue的路径startPath和destPath
# 2. 去除startPath和destPath的公共前缀
# 3. 将startPath全部变成U，将startPath和destPath拼接在一起，就是题目要求的路径
class Solution:
    def __init__(self):
        self.startValue = 0
        self.destValue = 0
        self.startpath = ""
        self.destpath = ""
        self.path = ""

    def getDirections(self, root, startValue: int, destValue: int) -> str:
        self.startValue = startValue
        self.destValue = destValue

        # 1. 获取从root到startValue和destValue的路径
        self.traversal(root)
        # 2. 获取startpath和destpath的公共前缀
        index = 0
        while index<len(self.startpath) and index<len(self.destpath) and self.startpath[index]==self.destpath[index]:
            index+=1
        # 去除startpath和destpath的公共前缀
        self.startpath = self.startpath[index:]
        self.destpath = self.destpath[index:]
        # 3. 将startpath全部变成U
        self.startpath = 'U'*len(self.startpath)
        # 4. 将startpath和destpath拼接在一起
        return self.startpath+self.destpath
        
        

    def traversal(self, root):
        """找到从root到startValue和destValue的路径"""
        if root is None: # 边界条件
            return 
            
        if root.val==self.startValue:
            self.startpath = self.path
        elif root.val==self.destValue:
            self.destpath = self.path
        
        # 二叉树遍历框架
        self.path+='L'
        self.traversal(root.left)
        self.path = self.path[:-1]

        self.path+='R'
        self.traversal(root.right)
        self.path = self.path[:-1]

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)
sol = Solution()
print(sol.getDirections(root, 3, 6))