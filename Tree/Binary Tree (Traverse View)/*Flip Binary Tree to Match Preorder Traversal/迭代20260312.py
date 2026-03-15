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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        i = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node is None:
                continue

            if node.val!=voyage[i]:
                return [-1]
            
            i+=1

            if node.left is not None and node.left.val!=voyage[i]:
                flipped.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            else:
                stack.append(node.right)
                stack.append(node.left)
        
        return flipped