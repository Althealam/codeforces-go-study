"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# 1. 是否需要访问所有节点：是
# 2. 当前节点答案是否依赖子树：是的，因为需要用返回值递归获取深度
# 3. 需不需要记录路径/父节点：不需要
# 4. 操作发生在哪：当到达叶子节点的时候，则开始比较max_depth = max(max_depth, current_depth)

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return self.max_depth 
        else:
            self.traversal(root, 1) # 包含当前节点，深度为1
            return self.max_depth
        
    def traversal(self, root, current_depth):
        if not root:
            return 
        if not root.children:
            self.max_depth = max(self.max_depth, current_depth)
        for child in root.children:
            self.traversal(child, current_depth+1)
         
        