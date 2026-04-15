# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1. 题目类型：自底向上（分解问题）
# 2. DFS三部曲：获取以node为根节点的子树的和
#（1）携带参数：当前节点，当前遍历的子树和
#（2）返回值含义：以node为根节点的子树的和
#（3）终止条件：如果遇到空节点，则直接返回0
#（4）单层递归的逻辑
# - 递归获取左右子树的和
# - 更新当前遍历的子树和：cursum = left+right+node.val
# - 更新哈希表：hash[cursum] = hash.get(cursum)+1

class Solution:
    def __init__(self):
        self.hash = {}

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root, 0)
        res = []
        maxfreq = max(self.hash.values())
        for sum_, freq in self.hash.items():
            if freq==maxfreq:
                res.append(sum_)
        return res

    
    def dfs(self, node, cursum):
        if not node:
            return 0
        left = self.dfs(node.left, cursum)
        right = self.dfs(node.right, cursum)
        cursum = left+right+node.val
        if cursum not in self.hash:
            self.hash[cursum] = 1
        else:
            self.hash[cursum]+=1
        return cursum
        