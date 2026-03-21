# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root (TreeNode), startValue (int), destValue (int)
# output: shortest path (string)

# 1. 找到从root到startValue和destValue的路径
# 2. 去除两个路径的公共前缀，并且要转化为L/R/U
# 5-1-3：L-L
# 5-2-6：R-L
# 3. 将到startValue的路径全部转化为U，并且将两个路径拼接在一起


class Solution:
    def __init__(self):
        self.start_path = ""
        self.dest_path = ""
        self.path = ""
        self.startValue = None
        self.destValue = None

    def getDirections(self, root, startValue: int, destValue: int) -> str:
        self.startValue, self.destValue = startValue, destValue

        # 1. 获取从root到startValue和destValue的路径
        self.traversal(root)

        # 2. 获取公共前缀
        # "RLL"和"RLR" ==> "LL"和"LR"
        index = 0
        while index<len(self.start_path) and index<len(self.dest_path) and self.start_path[index]==self.dest_path[index]:
            index+=1
        
        # 3. 转换为一下从root到startvalue
        self.start_path = 'U'*len(self.start_path)

        # 4. 将start_path和dest_path拼接在一起
        res = self.start_path+self.dest_path
        
        return res

    def traversal(self, root):
        """
        获取从root到startValue和destValue的路径
        1. 是否要遍历所有节点：是的
        2. 是否依赖子节点的返回值：否
        3. 什么时候操作，以及做什么：
        self.root.val==startValue or self.root.val==destValue：更新一下start_path和dest_path
        """
        if root is None:
            return # 由于我们不需要递归有啥返回值，所以直接写个return就好，相当于是return None
        if root.val==self.startValue:
            self.start_path = self.path[:]
        if root.val==self.destValue:
            self.dest_path = self.path[:]
        
        # 二叉树遍历
        self.path+='L'
        self.traversal(root.left)
        self.path=self.path[:-1]

        self.path+='R'
        self.traversal(root.right)
        self.path=self.path[:-1]
