# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下（双重递归）
# 2. DFS三部曲（主递归：用于遍历所有节点，确保所有节点都会被作为起点）
#（1）返回值含义： 以当前节点为起点，以及其子孙节点为起点的所有符合条件的路径总数
#（2）携带信息：root, targetSum
#（3）单层递归的逻辑
# - 接收结果
#   - res_from_root：调用辅助递归，以当前节点开头的所有符合条件的路径总数
#   - res_left：调用主递归，从左子树中找符合条件的路径总数
#   - res_right：调用主递归，从右子树中找符合条件的路径总数
# - 汇总
# return res_from_root+res_left+res_right
# 3. DFS三部曲（辅助递归：从固定起点向下搜寻）
#（1）返回值含义：以当前节点为起点，符合条件的路径总数
#（2）携带参数：当前节点，当前路径总和
#（3）终止条件：如果当前节点为空节点，则返回0
#（4）单层递归的逻辑
# - 如果current_path=targetSum：找到了一条符合要求的路径，增加路径总数
# - 继续去左边找剩下的和
# - 继续去右边找剩下的和

class Solution:
    def __init__(self):
        self.targetSum = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.targetSum = targetSum
        return self.dfs(root, 0)+self.pathSum(root.left,targetSum)+self.pathSum(root.right, targetSum)
        
    
    def dfs(self, node, curpathsum):
        if not node:
            return 0 
        curpathsum+=node.val
        if curpathsum==self.targetSum:
            # 无论是否命中，都需要继续向下，因为有可能会有负数出现
            return 1+self.dfs(node.left, curpathsum)+self.dfs(node.right, curpathsum)
        else:
            return self.dfs(node.left, curpathsum)+self.dfs(node.right, curpathsum)


        