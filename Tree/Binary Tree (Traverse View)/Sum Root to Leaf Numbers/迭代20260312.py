# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root, root.val)] # 当前节点和到达该节点的时候的路径
        while stack: 
            node, current_sum = stack.pop()
            if node.left is None and node.right is None: # 终止条件
                res+=current_sum
            # 开始进行right和left的遍历
            if node.right:
                stack.append((node.right, current_sum*10+node.right.val))
            if node.left:
                stack.append((node.left, current_sum*10+node.left.val))
        return res


        