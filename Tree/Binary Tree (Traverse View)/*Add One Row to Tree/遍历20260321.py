# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            self.traversal(1, depth, root, val) ## 注意：根节点的深度为1，而不是0！
            return root
    
    def traversal(self, cur_depth, depth, node, val):
        """
        找到深度为depth-1的节点
        1. 是否需要遍历所有节点：是的
        2. 是否需要子节点的返回值：不需要
        3. 什么时候操作，以及做啥：
        if cur_depth==depth-1: 创建两个new_node，并且记录一下原本的左右子节点，将原本的左右子节点放在new_node的左/右孩子节点上
        """
        if node is None:
            return 
        if cur_depth==depth-1: # 找到了深度为depth-1的节点node
            old_left = node.left
            old_right = node.right

            # 创建左边的子节点
            new_left = TreeNode(val)
            node.left = new_left
            node.left.left = old_left

            # 创建右边的子节点
            new_right = TreeNode(val)
            node.right = new_right
            node.right.right = old_right
        else:
            self.traversal(cur_depth+1, depth, node.left, val)
            self.traversal(cur_depth+1, depth, node.right, val)

