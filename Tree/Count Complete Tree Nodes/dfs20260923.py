# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：利用完全二叉树的性质，避免访问所有的节点

# 完全二叉树的性质：
# 1. 除了最后一层外，前面的层全部填满
# 2. 最后一层的节点一定从左到右排列

# 满二叉树的性质：观察最左边和最右边，如果这棵树是一个完全二叉树，那么如果leftheight==rightheight，可以知道这棵树是一个满二叉树
# 满二叉树的节点个数为2^0+2^1+2^2+...+2^(h-1)
# 根据等比求和公式，可以知道上述之和为2^h-1
# 当节点数为n的时候，可以知道树高为h=logn

# 如果这棵树不是一个满二叉树，那么就1+count(root.left)+count(root.right)

# 时间复杂度：O(logn**2)
# 空间复杂度：O(logn)，递归深度为logn
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        # 最左高度==最右高度，说明该二叉树是满二叉树
        # 求树高的时间复杂度为O(logn)
        left_height = self.leftHeight(root)
        right_height = self.rightHeight(root)

        # 利用满二叉树的性质来求和
        if left_height==right_height:
            return 2**left_height-1
        # 继续递归左右子树
        return (self.countNodes(root.left)+self.countNodes(root.right)+1)

    # 不可以是左右子树的高度，而是最左节点和最右节点的高度
    def leftHeight(self, node):
        height = 0
        while node:
            height+=1
            node = node.left
        return height
    
    def rightHeight(self, node):
        height = 0
        while node:
            height+=1
            node = node.right
        return height
