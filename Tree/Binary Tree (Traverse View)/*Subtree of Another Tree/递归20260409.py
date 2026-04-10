# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自顶向下
# 本题需要遍历二叉树的所有节点，然后判断一下以当前节点为根节点的子树是否和subRoot相同
# 2. DFS三部曲（辅助递归）
#（1）返回值含义：以当前节点为根节点的子树是否和subRoot相同，bool
#（2）携带信息：当前root的节点，当前subRoot的节点
#（3）终止条件：
# - 如果root is None and subRoot is None: return True
# - 如果root is None or subRoot is None: return False
# - 如果root.val!=subRoot.val: return False
#（4）单层递归的逻辑：root.val==subRoot.val
# - 检查左边和右边
# return self.issame(root.left, subRoot.left) and self.issame(root.right, subRoot.right)
# 3. DFS三部曲（主递归）
#（1）返回值含义：以当前节点为根节点的子树中，是否能找到subTree
#（2）携带信息：root, subRoot
#（3）终止条件：如果root is None，说明整棵树都已经找了一遍还是没找到，则直接return False
#（4）单层递归逻辑
# - 接收结果
#   - check_self：使用辅助递归检查以root为根节点的子树
#   - check_left：调用主递归，检查以root.left为根节点的子树中有没有符合条件的子树
#   - check_right：调用主递归，检查以root.right为根节点的子树中有没有符合条件的子树

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.issame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def issame(self, node, subnode):
        if node is None and subnode is None:
            return True
        if node is None or subnode is None:
            return False
        if node.val!=subnode.val:
            return False
        return self.issame(node.left, subnode.left) and self.issame(node.right, subnode.right)
        