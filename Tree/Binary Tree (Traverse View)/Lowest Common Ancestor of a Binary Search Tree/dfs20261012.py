# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 性质：在BST中，两个节点的LCA的值一定是node.val<p and node.val>q or node.val<p or node.val>p
# LCA节点 => LCA的val和p/q的val的关系 是否可以反推？即值在p和q中间的节点，是否一定是p和q的LCA？
# 和二叉树的最近公共祖先不同，可以通过BST的性质进行剪枝

# 递归三部曲：
# 1. 递归函数返回值及参数：参数就是当前节点以及两个节点p和q，返回值是最近公共祖先
# 2. 终止条件：遇到空节点则返回
# 3. 单层递归的逻辑：寻找区间[p.val, q.val]
# 如果cur.val>p.val且cur.val>q.val，则向左遍历
# 如果cur.val<p.val且cur.val<q.val，则向右遍历
# 如果cur.val在p.val和p.val的中间，则返回cur

# 时间复杂度：O(h)，每次递归只需要进入一棵子树，而不是同时递归左右子树，每个节点只进行O(1)的比较操作，最多递归h层，其中h为树的高度
# 空间复杂度：O(h)，dfs递归调用栈
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            if cur is None:
                return None
            if cur.val>p.val and cur.val>q.val:
                return dfs(cur.left)
            elif cur.val<p.val and cur.val<q.val:
                return dfs(cur.right)
            else:
                return cur
        return dfs(root)
            
        