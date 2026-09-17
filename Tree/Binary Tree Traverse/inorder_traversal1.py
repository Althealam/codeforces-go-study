class Solution:
    def inordertraversal(self, root):
        if not root:
            return []
        stack = []
        res = []
        cur = root
        while cur or stack:
            # 先访问最底层的左子树节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左节点后再处理栈顶节点
            else:
                cur = stack.pop()
                res.append(cur.val)
                # 取右边的节点
                cur = cur.right
        return res
            