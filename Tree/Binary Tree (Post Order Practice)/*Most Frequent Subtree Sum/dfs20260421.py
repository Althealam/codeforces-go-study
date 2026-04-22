# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解类型）
# 2. DFS三部曲：以node为根节点的子树元素和
#（1）携带参数：node
#（2）返回值含义：以node为根节点的子树元素和
#（3）终止条件：遇到空节点的时候，返回0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的元素和
# - 获取当前子树的元素和，leftsum+rightsum+node.val
# - count哈希表更新元素和的出现次数

class Solution:
    def __init__(self):
        self.count = {}

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        maxfreq = max(self.count.values())
        res = []
        for sum_, freq in self.count.items():
            if freq==maxfreq:
                res.append(sum_)
        return res
    
    def dfs(self, node):
        if not node:
            return 0
        leftsum = self.dfs(node.left)
        rightsum = self.dfs(node.right)
        cursum = leftsum+rightsum+node.val
        self.count[cursum] = self.count.get(cursum, 0)+1
        return cursum