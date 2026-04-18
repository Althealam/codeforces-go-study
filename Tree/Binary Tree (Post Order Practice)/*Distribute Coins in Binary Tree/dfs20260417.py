# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 2. DFS三部曲：获取以node为根的子树的净流量（每条边上的流量就是移动次数）
# 净流量=abs(当前子树的节点个数-当前子树的金币个数)
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根的子树的净流量
#（3）终止条件：遇到空节点则返回0
#（4）单层递归的逻辑：
# - 调用DFS获取左右子树的净流量left和right，因此左右子树和当前节点的移动次数为abs(left)+abs(right)（因为这个数值是还缺/多的金币数量，因此一定会移动这么多次）
# - 左右子树的净值为leftbalance, rightbalance
# - 返回：leftbalance+rightbalance+node.val-1（leftbalance是左子树的净值，rightbalance是右子树的经值，node.val-1是根节点的净值）

class Solution:
    def __init__(self):
        self.res = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node:
            return 0
        # 获取左右子树的净流量
        leftbalance = self.dfs(node.left)
        rightbalance = self.dfs(node.right)
        self.res+=abs(leftbalance)+abs(rightbalance) # 更新一下移动次数
        return leftbalance+rightbalance+node.val-1