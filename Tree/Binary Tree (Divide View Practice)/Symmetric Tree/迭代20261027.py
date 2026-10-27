
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def compare(left, right):
            stack = [(left, right)]
            while stack:
                x, y = stack.pop()
                if x is None and y is None:
                    continue
                if x is None or y is None:
                    return False
                if x.val!=y.val:
                    return False
                stack.append((x.left, y.right))
                stack.append((x.right, y.left))
            return True
        return compare(root.left, root.right)