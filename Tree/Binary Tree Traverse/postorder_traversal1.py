class Solution:
    def postordertraversal(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # 先处理中节点
            res.append(node.val)
            # 左子节点入栈
            if node.left:
                stack.append(node.left)
            # 右子节点入栈
            if node.right:
                stack.append(node.right)
        return res[::-1]

# 后序遍历，左右中