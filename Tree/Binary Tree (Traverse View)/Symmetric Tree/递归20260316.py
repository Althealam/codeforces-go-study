class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        if self.same(root, subRoot):
            return True
        # 去左右子树中判断是否有和subRoot相同的子树
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def same(self, a, b):
        # 判断一对节点是否相同
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val!=b.val:
            return False
        # 判断其他节点是否相同
        return self.same(a.left, b.left) and self.same(a.right, b.right)