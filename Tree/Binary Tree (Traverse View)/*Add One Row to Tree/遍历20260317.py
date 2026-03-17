# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 每个子节点的返回值依赖父节点的返回值，因此有返回值的递归
# 本题需要找到对应深度下的节点，所以需要遍历整个树

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1: # 深度为1的时候，直接创建一个新的节点，并且将原来的root变成新的root的左子树
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else: # 深度大于1的时候，则开始traversal整个树，找到树对应的深度
            self.traversal(root, 1, depth, val)
        return root


    def traversal(self, node, cur_depth, depth, val):
        if not node:
            return 
        if cur_depth==depth-1:
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = old_left
            node.right.right = old_right
        else:
            self.traversal(node.left, cur_depth+1, depth, val)
            self.traversal(node.right, cur_depth+1, depth, val)
        





        