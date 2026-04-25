# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# (3, 2, 1) ==> (3, 2) first=3, second=2 ==> (2, 1) first=3, second=1
# (1, 3, 2, 4) ==> (3, 2) first=3, second=2
# (1, 5, 2, 4, 6, 9) ==> (5, 2) first=5, second=2
# (1, 10, 3, 4, 7, 2, 12) ==> (10, 3) first=10, second=3 ==> (7, 2) first=10, second=2

# 1. 题目类型：中序遍历
# 2. DFS三部曲：用来寻找错误的两个节点
#（1）携带参数：当前节点node，node的前面一个节点pre
#（2）返回值含义：全局变量（错误的两个节点）
#（3）终止条件：如果遇到空节点则返回
#（4）单层递归的逻辑
# - 先调用DFS遍历左子树
# - 判断一下当前节点node和前面一个节点pre的关系：如果pre.val>node.val，说明找到了错误的节点，更新全局变量first和second
# - 调用DFS遍历右子树
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
    
    def dfs(self, cur):
        if not cur:
            return 
        self.dfs(cur.left)
        if self.pre and cur.val<self.pre.val:
            if self.first==None:
                self.first = self.pre
            self.second = cur
        self.pre = cur
        self.dfs(cur.right)