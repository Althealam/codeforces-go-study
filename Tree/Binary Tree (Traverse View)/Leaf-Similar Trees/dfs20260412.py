# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上，并且是中序遍历（左、右、中）
# 2. DFS三部曲
#（1）携带信息：当前节点
#（2）返回值类型：无
#（3）终止条件：如果当前节点为叶子节点，则将叶子节点加入到结果集合中
#（4）单层遍历的逻辑：先递归左边，再递归右边
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getrootleaves(root1)
        leaves2 = self.getrootleaves(root2)
        return leaves1==leaves2
    
    def getrootleaves(self, root):
        leaves = []
        def dfs(node):
            if not node:
                return 
            if node.left is None and node.right is None:
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return leaves
                
        