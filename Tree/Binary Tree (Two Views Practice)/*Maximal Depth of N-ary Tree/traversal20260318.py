"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# 1. 是否需要遍历所有节点：是
# 2. 操作发生在哪：children is None: update max_depth
# 3. 是否需要子节点的返回值：否


class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return self.max_depth
        self.traversal(root, 1) # 一定要从1开始
        return self.max_depth
    
    def traversal(self, root, curdepth):
        if not root:
            return None
        if not root.children: # 到达叶子节点 注意：不可以写if root.children is None，因为root.children一般是空列表，不是空值
            self.max_depth = max(self.max_depth, curdepth)
        for child in root.children:
            self.traversal(child, curdepth+1)
        
        