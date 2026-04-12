# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解类型）
# 2. DFS三部曲：获取以当前节点为根的子树的节点和
#（1）携带参数：当前节点，当前子树的和
#（2）返回参数：当前子树的节点和
#（3）终止条件：如果当前节点为空，则返回0
#（4）单层递归的逻辑
# - 处理当前节点：
#   - 获取左右子树的节点和
#   - 加上当前的节点和
# 3. DFS三部曲：获取以当前节点为根的子树的坡度
#（1）携带参数：当前节点
#（2）返回参数：当前子树的坡度
#（3）终止条件：如果当前节点为空，则返回0
#（4）单层递归的逻辑
# - 获取左右子树的节点和
# - 获取当前子树的坡度

class Solution:
    def __init__(self):
        self.res = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, node, cursum):
        if not node:
            return 0
        leftsum = self.dfs(node.left, 0)
        rightsum = self.dfs(node.right, 0)
        self.res+=abs(leftsum-rightsum)
        return leftsum+rightsum+node.val