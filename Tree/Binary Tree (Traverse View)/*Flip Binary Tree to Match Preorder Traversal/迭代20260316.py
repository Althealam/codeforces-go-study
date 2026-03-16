# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 想要按层、一层层扩散则用queue；想要一路往下走的则用stack

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped = []
        index = 0 # 当前在voyage中遍历的索引
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None: # 当前弹出的节点为空，则继续弹出栈的节点
                continue
            if node.val!=voyage[index]: # 当前的节点无法对应上
                return [-1]
            else: # 当前的节点可以对应上
                index+=1 # 开始遍历下一个节点
                if node.left and node.left.val!=voyage[index]: # 左孩子对应不上
                    flipped.append(node.val) 
                    # 先右节点，再左节点（注意stack的顺序）
                    if node.left: # 避免将None压入栈中
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
        return flipped 

