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

# 在一个升序序列中，如果任意两个数a和b交换了位置，那么一定会产生逆序对
# 第一个异常点就是本该在后面的大数，它出现在第一次发生“前大后小”的地方
# 第二个异常点就是本该在前面的小数，它出现在最后一次发生“前大后小”的地方

# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：返回经过经过修复后以node为根节点的子树
#（1）携带参数：当前节点node，上一个看过的节点pre
#（2）返回值含义：经过修复后以node为根节点的子树
#（3）终止条件：遇到空节点则直接返回None
#（4）单层递归的逻辑：中序遍历（左中右）确保了二叉搜索树的遍历一定是递增的
# - 检查pre.val是否大于cur.val：如果pre.val>cur.val，说明找到了异常点
#   - 记录节点pre（这是跳到了前面的大数，比如图片中的3），同时记录cur
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.pre = None # 中序遍历的前面一个节点

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root, None)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        return root
    
    def dfs(self, node, pre):
        if not node:
            return 
        self.dfs(node.left, node)
        if self.pre and self.pre.val>node.val:
            if self.first is None:
                self.first = self.pre
                self.second = node
            else:
                self.second = node
        
        self.pre = node # 移动节点

        self.dfs(node.right, node)