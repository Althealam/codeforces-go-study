# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）返回值含义：插入了新行后的节点
#（2）携带参数：当前深度，当前节点
#（3）终止条件：
# - 当当前深度等于depth的时候，则开始创建新的节点
# - 当前节点为空节点，直接return
#（4）单层递归的逻辑
# - 继续递归处理左右子树

class Solution:
    def __init__(self):
        self.depth = 0
        self.val = 0
        
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth, self.val = depth, val
        if self.depth==1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        return self.dfs(root, 1)
    
    def dfs(self, node, curdepth):
        if not node:
            return 
        if curdepth==self.depth-1:
            ori_left = node.left
            ori_right = node.right
            node.left = TreeNode(self.val)
            node.right = TreeNode(self.val)
            node.left.left = ori_left
            node.right.right = ori_right
            return node
        node.left = self.dfs(node.left, curdepth+1)
        node.right = self.dfs(node.right, curdepth+1)
        return node
        
        