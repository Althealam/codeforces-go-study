# 时间复杂度：O(n)，因为每个节点只会被访问一次
# 空间复杂度：O(h)，h是树的高度，递归调用栈的深度为h，如果树退化为链表的话h=n
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preordertraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return 
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res