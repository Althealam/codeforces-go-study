# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下传递信息，自底向上做决策
# 2. DFS三部曲：获取以node为根节点的子树的和
#（1）携带参数：当前节点
#（2）返回值含义：以node为根节点的子树的和
#（3）终止条件：当前节点为None，返回0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的leftsum, rightsum
# - part1=leftsum+rightsum+node.val，part2=sum(nodes)-part1
# - 更新maxproduct = max(maxproduct, part1*part2)
# - 返回：leftsum+rightsum+node.val

class Solution:
    def __init__(self):
        self.maxproduct = 0
        self.sum_ = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.getsum(root)
        self.dfs(root)
        x = 10**9+7
        return self.maxproduct%x
    
    def getsum(self, root):
        if not root:
            return 0
        self.sum_+=root.val
        self.getsum(root.left)
        self.getsum(root.right)
        
    def dfs(self, node):
        if not node:
            return 0
        leftsum = self.dfs(node.left)
        rightsum = self.dfs(node.right)
        partone = leftsum+rightsum+node.val
        parttwo = self.sum_-partone
        self.maxproduct = max(self.maxproduct, partone*parttwo)
        return partone
