# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 题目类型：自底向上（后序遍历）
# 2. 递归三部曲
#（1）递归函数返回值及参数：当前子树中找到的p、q或者LCA
# - 返回None：当前子树没有找到p或者q
# - 返回p：当前子树找到了p，并向上传递
# - 返回q：当前子树找到了q，并向上传递
# - 返回LCA：当前子树找到了p和q的LCA
#（2）终止条件：遇到空节点则返回空，或者root已经是p或者q时也直接返回root
#（3）单层递归的逻辑
# - 递归左子树，返回左子树中找到的目标节点或者最近公共祖先
# - 递归右子树，返回右子树中找到的目标节点或者最近公共祖先
# - 根据左右子树的返回值判断
#   如果left is None and right is None，则左右子树均为找到目标节点
#   如果left is not None and right is None，返回left，表示目标节点或者LCA位于左子树
#   如果left is None and right is not None，返回right
#   如果left is not None and right is not None，返回当前节点

# 时间复杂度：O(n) 需要遍历所有的节点
# 空间复杂度：O(h)，递归栈的深度
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            if cur is None:
                return None
            if cur is p or cur is q:
                return cur
            l = dfs(cur.left)
            r = dfs(cur.right)
            if l is None and r is not None:
                return r
            elif l is not None and r is None:
                return l
            elif l is not None and r is not None:
                return cur
        return dfs(root)
