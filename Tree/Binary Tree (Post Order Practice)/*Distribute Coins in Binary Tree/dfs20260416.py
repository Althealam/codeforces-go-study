# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（叶子节点的状态是确定的）
# 2. DFS三部曲：统计每颗子树的硬币个数coins和节点个数nodes，硬币多就移出子树，硬币少就移入子树
# 这颗子树和其父亲节点的边的计数之为abs(coins-nodes)
# - coins = coinsleft+coinsright+node.val
# - nodes = nodesleft+nodesright+1
# - d = dleft+dright+node.val-1 (node.val-1是根节点的净值)
#（1）携带参数：当前节点
#（2）返回值含义：以node为根节点的子树的硬币个数和节点个树
#（3）终止条件：如果node为None，则返回0和0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的情况：coinleft, nodeleft and coinright, noderight
# - 以node为根节点的子树的硬币个数为coinleft+coinright+node.val
# - 以node为根节点的子树的节点个数为nodeleft+noderight+1
# 返回上述两个值

class Solution:
    def __init__(self):
        self.res = 0
    
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return (0, 0)
        
        # 获取左子树的硬币总数和节点总数
        coinleft, nodeleft = self.dfs(node.left)
        # 左子树的净盈余，表示有多少个硬币要从左子树的根节点与其父亲节点的边中流出
        dleft = abs(coinleft-nodeleft)

        # 获取右子树的硬币总数和节点总数
        coinright, noderight = self.dfs(node.right)
        # 右子树的净盈余，表示有多少个硬币要从右子树的根节点与其父亲节点的边中流出
        dright = abs(coinright-noderight)

        # 当前节点为根的子树的硬币总数和节点总数
        coins = coinleft+coinright+node.val
        nodes = nodeleft+noderight+1

        # 更新一下流动的次数
        self.res+=dleft+dright+node.val-1
        return (coins, nodes)
