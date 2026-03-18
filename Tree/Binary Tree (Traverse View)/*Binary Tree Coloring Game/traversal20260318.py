# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 对方先选择一个节点之后，你的最优策略是紧贴着对方的那个节点进行选择，也就是说选择节点x的左右子节点或者父亲节点
# 如果想要赢，必须要占据超过n/2的节点，也就是说这三个蓝色区域中节点数最多的那个区域中的节点个数大于n/2你能赢，否则你就输

# 1. 在以root为根节点的二叉树中找到x的节点的位置
# 2. 计算x的左右子树的节点数量，以及父节点的子树的数量
# 3. 判断一下左右子树、父子树的节点数量是否超过n/2，如果是的话你可以赢，否则的话则赢不了
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        x_node = self.found(root, x)
        left_tree_count = self.count(x_node.left)
        right_tree_count = self.count(x_node.right)
        other_tree_count = n-1-left_tree_count-right_tree_count
        max_cnt = max(left_tree_count, max(right_tree_count, other_tree_count))
        return max_cnt>n//2

    def count(self, cur):
        if not cur:
            return 0
        return 1+self.count(cur.left)+self.count(cur.right)

    def found(self, node, x):
        """
        1. 是否要遍历整棵树：是的
        2. 什么时候操作，以及操作行为：if node.val==x: return node
        3. 是否要记录子节点的值：不需要
        """
        if not node:
            return False
        if node.val==x:
            return node
        else:
            return self.found(node.left, x) or self.found(node.right, x)
        