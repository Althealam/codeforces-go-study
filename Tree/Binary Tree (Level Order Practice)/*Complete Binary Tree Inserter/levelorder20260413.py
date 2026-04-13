# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 定义一个队列，该队列用来存储倒数第二层中，缺少孩子节点的父亲节点（用层序遍历实现），这个部分在init中实现
# 2. insert函数主要是对队列中的第一个元素做处理（队列的第一个元素是第一个缺少孩子节点的元素）

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        queue = collections.deque([root])
        self.res_queue = collections.deque([])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left or not node.right:
                    self.res_queue.append(node)

    def insert(self, val: int) -> int:
        parent = self.res_queue[0]
        new_node = TreeNode(val)
        if parent.left is None:
            parent.left = new_node
        else:
            # 该parent已经被填充完毕了，则直接弹出去
            parent.right = new_node
            self.res_queue.popleft()
        self.res_queue.append(new_node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()