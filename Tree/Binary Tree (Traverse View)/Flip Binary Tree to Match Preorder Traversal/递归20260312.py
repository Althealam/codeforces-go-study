# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 先序遍历+递归
# 1. 如果root.val!=voyage[index]: return False （无论如何反转都不能成功）
# 2. 判断是否要进行反转
# (1) root.left.val==voyage[index+1]：不需要反转
#    - 先遍历左子树
#    - 后遍历右子树
# (2) root.left.val!=voyage[index+1]：需要反转
#    - 先遍历右子树
#    - 后遍历左子树

class Solution:
    def __init__(self):
        self.index = 0 # 记录当前遍历voyage的索引
        self.flipped = [] # 记录反转的节点

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if not self.traversal(root, voyage):
            return [-1]
        return self.flipped
    
    def traversal(self, root, voyage):
        if not root:
            return True
        if root.val!=voyage[self.index]: # root和当前索引不匹配，直接返回False
            return False
        # 匹配的情况下，跳转到下一个元素
        self.index+=1

        # 判断左孩子的情况
        if root.left is not None and root.left.val!=voyage[self.index]:
            self.flipped.append(root.val)
            return self.traversal(root.right, voyage) and self.traversal(root.left, voyage)
        
        return self.traversal(root.left, voyage) and self.traversal(root.right, voyage)



