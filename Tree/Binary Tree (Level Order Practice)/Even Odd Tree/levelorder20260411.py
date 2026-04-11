# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        depth = 0
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if depth%2==0: # 当前是偶数层，需要判断是不是递增的，以及节点是不是都是奇数
                    if prev and node.val<=prev.val:
                        return False
                    if node.val%2==0:
                        return False
                if depth%2!=0: # 当前是奇数层，需要判断是不是递减的
                    if prev and node.val>=prev.val:
                        return False
                    if node.val%2!=0:
                        return False
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return True
        