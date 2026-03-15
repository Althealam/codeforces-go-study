# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：用BFS去判断两个节点是否堂兄弟
# BFS按照层扩展，同一轮从队列里取出来的节点一定在同一层，因此只需要在这一层里面找x和y，并且记录他们的父亲节点，根据是否在同一层和父亲节点是否相同来下结论，判断是否是堂兄弟

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([(root, None)]) # (node, parent)
        while queue:
            size = len(queue)
            parent_x = None
            parent_y = None

            for _ in range(size):
                node, parent = queue.popleft()
                if node.val==x:
                    parent_x = parent
                if node.val==y:
                    parent_y = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            if parent_x and parent_y:
                return parent_x!=parent_y
            if parent_x or parent_y:
                return False
        return False