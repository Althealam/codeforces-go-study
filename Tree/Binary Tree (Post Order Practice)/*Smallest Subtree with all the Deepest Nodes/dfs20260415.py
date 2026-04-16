# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上（后序遍历）
# 2. DFS三部曲
#（1）携带参数：当前节点
#（2）返回值含义：以当前节点为根的子树能到达的最大深度，该子树中包含所有最深节点的最小公共祖先
#（3）终止条件：如果遇到空节点，则直接返回0，节点为None
#（4）单层递归的逻辑（后序遍历）
# - 递归左右子树，获取左右子树的最大深度和对应的祖先
# - 如果l_depth==r_depth，说明最深的节点均匀分布在左右子树中，那么当前节点就是最小的公共祖先
# - 如果l_depth>r_depth，说明最深的节点全部都在左边，因此我们要找的祖先一定在左子树返回的结果里，返回(l_depth+1, l_node)
# - 如果l_depth<r_depth，说明最深的节点全部都在右边，因此我们要找的祖先一定在右子树返回的结果里，返回(r_depth+1, r_node)

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth, node = self.dfs(root)
        return node
    
    def dfs(self, node):
        if not node:
            return (0, None)
        l_depth, l_node = self.dfs(node.left)
        r_depth, r_node = self.dfs(node.right)
        if l_depth==r_depth:
            # 左右一样深，当前节点是公共节点，深度是子树深度+1
            return (l_depth+1, node)
        if l_depth>r_depth: 
            # 左边深，返回左边的祖先（因为说明最深的节点在左子树），深度依然要加1
            return (l_depth+1, l_node)
        else:
            # 右边深，返回右边的祖先（说明最深的节点在右子树），深度依然要加1
            return (r_depth+1, r_node)

            