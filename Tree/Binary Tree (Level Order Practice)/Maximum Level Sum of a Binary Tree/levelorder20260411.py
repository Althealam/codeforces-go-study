# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        queue = collections.deque([root])
        max_depth = 0
        max_sum = float('-inf')
        cur_depth = 1
        while queue:
            cur_sum = 0
            # 统计这一层的节点和
            for _ in range(len(queue)):
                node = queue.popleft()
                cur_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cur_sum>max_sum:
                max_sum = cur_sum
                max_depth = cur_depth
            cur_depth+=1
        return max_depth