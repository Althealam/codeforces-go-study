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
        if not root:
            return self.res
        self.dfs(root, 0)
        max_freq = max(self.hashmap.values())
        return [s for s, freq in self.hashmap.items() if freq==max_freq]
     
    def dfs(self, node, cur_sum): 
        """获取当前子树的节点和，并且更新哈希表"""
        if not node:
            return 0
        left_sum = self.dfs(node.left, cur_sum)
        right_sum = self.dfs(node.right, cur_sum)
        total_sum = node.val+left_sum+right_sum
        self.hashmap[total_sum] = self.hashmap.get(total_sum, 0)+1
        return total_sum
