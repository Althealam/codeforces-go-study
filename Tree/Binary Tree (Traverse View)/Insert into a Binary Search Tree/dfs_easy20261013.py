# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归函数有返回值版
# 1. 题目类型：自顶向下
# 2. 递归三部曲
#（1）递归函数参数以及返回值：根节点指针，要插入的元素，返回值为插入val后，这棵子树的根节点
#（2）终止条件：当遍历的节点为空的时候，就是要插入节点的位置，则返回插入的节点
#（3）单层递归的逻辑
# - 如果root.val>val：节点应该插入在左子树
# - 如果root.val<val：节点应该插入在右子树
# - 否则return root

# 时间复杂度：O(h)
# 我们每次只需要选择左子树或者右子树进行递归，不需要遍历整棵树
# 如果是平衡二叉搜索树，时间复杂度为O(logn)，此时的h=logn
# 如果是退化的二叉搜索树（退化为链表）那么时间复杂度为O(n)
# 空间复杂度：O(h)，每次递归调用都会占用一定的调用栈空间
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)
        if root.val>val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val<val:
            root.right = self.insertIntoBST(root.right, val)
        return root