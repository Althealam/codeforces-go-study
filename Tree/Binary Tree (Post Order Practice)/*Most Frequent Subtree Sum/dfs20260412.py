# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（分解类型）
# 2. DFS三部曲：获取以当前节点为根节点的子树的节点和（辅助）
#（1）携带信息：当前节点，以及当前节点为根节点的子树的和
#（2）返回值含义：以当前节点为根节点的子树的节点和
#（3）终止条件：遇到空节点，则返回0
#（4）单层递归的逻辑
# - 获取左右子树的节点和
# - 将左右子树的节点和加上当前节点的值
# 3. DFS三部曲：遍历所有的节点（主）
#（1）携带信息：当前节点
#（2）返回值含义：无
#（3）终止条件：遇到空节点，则直接返回
#（4）单层递归的逻辑
# - 获取当前节点的子树和，并且更新到哈希表中
# - 递归左右子树

class Solution:
    def __init__(self):
        self.hashmap = {}
        self.res = []

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.getsum(root)
        max_val = max(self.hashmap.values())
        for sum_, cnt in self.hashmap.items():
            if cnt==max_val:
                self.res.append(sum_)
        return self.res
     
    def dfs(self, node, cur_sum):
        """post order"""
        if not node:
            return 0
        left_sum = self.dfs(node.left, cur_sum)
        right_sum = self.dfs(node.right, cur_sum)
        return node.val+left_sum+right_sum
    
    def getsum(self, node):
        if not node:
            return 
        cursum = self.dfs(node, 0)
        if cursum not in self.hashmap:
            self.hashmap[cursum] = 1
        else:
            self.hashmap[cursum]+=1
        self.getsum(node.left)
        self.getsum(node.right)
        
        