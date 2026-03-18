# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 是否需要遍历所有节点：是
# 2. 操作发生在哪：当当前节点的深度为depth-1时，则创建值为val的两个节点，并且插入到当前节点的左右子节点中
# 3. 是否需要返回值：否

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot
        else:
            self.traversal(root, 1, depth,val)
            return root
    
    def traversal(self, root, curdepth, depth, val):
        if root is None:
            return 
        if curdepth==depth-1: # 找到了深度为depth-1的节点
            oldleft = root.left
            oldright = root.right
            newleft = TreeNode(val)
            newright = TreeNode(val)
            root.left = newleft
            root.left.left = oldleft
            root.right = newright
            root.right.right = oldright
        else: 
            self.traversal(root.left, curdepth+1, depth, val)
            self.traversal(root.right, curdepth+1, depth, val)
        
        