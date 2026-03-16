# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代法
# 1. 在queue中存储当前的节点，以及该结点的父亲
# 2. 每次迭代的时候，都从queue弹出队头节点，然后判断一下该结点的节点值和x或者y是否相同（在同一层弹出的两个节点的深度一定相同，因此只需要判断一下父亲节点是否相同即可）

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([(root, None)]) # 当前节点，以及当前节点的父亲
        while queue:
            parent_x = None
            parent_y = None
            size = len(queue)
            for _ in range(size): # 层序遍历
                cur_node, cur_father = queue.popleft()
                if cur_node.val==x:
                    parent_x = cur_father
                if cur_node.val==y:
                    parent_y = cur_father
                if cur_node.left:
                    queue.append((cur_node.left, cur_node))
                if cur_node.right:
                    queue.append((cur_node.right, cur_node))
            if parent_x and parent_y:
                return parent_x!=parent_y
            if parent_x or parent_y:
                return False
        return False        