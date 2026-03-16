# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# subRoot可能的出现位置是root, root.left, root.right, root.left.left, root.right.right...
# subRoot可能出现在root的每一个根节点上，因此需要对root的每一个根节点判断是否和subRoot相同

# 1. 如果root==None: 检查subRoot是否也是None
# 2. 如果same(root, subRoot): return True（其中same除了判断root.val和subRoot.val，还会判断root.left, root.right, subRoot.left, subRoot.right）
# 3. 去root.left找
# 4. 去root.right找
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
