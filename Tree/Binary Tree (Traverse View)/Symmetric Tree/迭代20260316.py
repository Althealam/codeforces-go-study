class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if self.same(node, subRoot): # 持续检查node和subRoot的形状是否相同
                return True
            if node.left: # 继续检查node.left和node.right是否和subRoot相同
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
        
    def same(self, a, b):
        stack = [(a, b)]
        while stack:
            x, y = stack.pop()
            if x is None and y is None:
                continue # 这里一定是continue，不可以return True，因为只是这个节点相同合法了，我们还要继续检查下一个节点
            if x is None or y is None:
                return False
            if x.val!=y.val:
                return False
            stack.append((x.left, y.left))
            stack.append((x.right, y.right))
        return True