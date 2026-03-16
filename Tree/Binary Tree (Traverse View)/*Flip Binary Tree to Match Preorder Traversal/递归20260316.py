# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 如果root.val!=voyage[index]: return False（无论如何反转都不可能成功过）
# 2. 判断是否要进行反转
# - root.left.val==voyage[index+1]：不需要反转
# * 先遍历左子树
# * 后遍历右子树
# - root.left.val!=voyage[index+1]：需要反转
# * 先遍历右子树
# * 后遍历左子树

class Solution:
    def __init__(self):
        self.index = 0
        self.flipped = [] # 存储反转的节点值

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if self.traversal(root, voyage):
            return self.flipped
        return [-1]
    
    def traversal(self, root, voyage):
        if not root:
            return True
        if root.val!=voyage[self.index]: # 无法反转
            return False
        # 可以反转，则跳转到下一个节点
        self.index +=1
        # 如果左孩子存在，并且左孩子不是下一个应该访问的节点，则需要反转
        if root.left and self.index<len(voyage) and root.left.val!=voyage[self.index]: 
            self.flipped.append(root.val)
            return self.traversal(root.right, voyage) and self.traversal(root.left, voyage)
        return self.traversal(root.left, voyage) and self.traversal(root.right, voyage)
        