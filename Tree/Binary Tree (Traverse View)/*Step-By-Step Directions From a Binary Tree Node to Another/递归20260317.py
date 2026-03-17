# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. record the path from root to startValue and destValue
# 2. delete the prefix for both start_path and dest_path
# 3. change the start_path into 'U'
# 4. combine the start_path and dest_path

class Solution:
    def __init__(self):
        self.start_path = ""
        self.dest_path = ""
        self.path = ""
        self.startValue = 0
        self.destValue = 0

    def getDirections(self, root, startValue: int, destValue: int) -> str:
        self.startValue = startValue
        self.destValue = destValue

        # 1. get the path from root to startValue and destValue
        self.traversal(root)
        
        # 2. remove the prefix
        index = 0
        while index<len(self.start_path) and index<len(self.dest_path) and self.start_path[index]==self.dest_path[index]:
            index+=1
        self.start_path = self.start_path[index:]
        self.dest_path = self.dest_path[index:]

        # 3. change the start_path into 'U'
        self.start_path = 'U'*len(self.start_path)

        # 4. combine start_path and dest_path
        return self.start_path+self.dest_path
    
    def traversal(self, root):
        if root is None:
            return 
        if root.val==self.startValue:
            self.start_path = self.path
        if root.val==self.destValue:
            self.dest_path = self.path
        
        self.path+='L'
        self.traversal(root.left)
        self.path = self.path[:-1]

        self.path+='R'
        self.traversal(root.right)
        self.path = self.path[:-1]
        
        
        
        