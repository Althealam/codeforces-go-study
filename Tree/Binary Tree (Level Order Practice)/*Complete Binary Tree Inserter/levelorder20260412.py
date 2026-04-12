# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 完全二叉树：
# 1. 一棵深度为k的完全二叉树，除了第k层（最后一层）以外，第1到第k-1层的节点数都必须达到最大值
# 2. 并且在最后一层中，所有的节点都必须在左侧
# 思路：
# 1. 使用层序遍历，寻找缺少左子节点/右子节点的父亲节点，并且放入队列中
# 2. 由于完全二叉树要求所有的节点都必须在左侧，所以获取队列中的第一个元素，这个元素就是我们需要插入的父亲节点
# 3. 判断一下插入该节点到父亲节点的左子节点还是右子节点中
# 时间复杂度：

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = collections.deque([]) # 用来存储缺少部分孩子节点的父亲节点
        # space: O(n)
        queue = collections.deque([root])
        while queue: # time: O(n)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left or not node.right:
                    self.deque.append(node)

    def insert(self, val: int) -> int:
        # 队列的最左侧就是当前最靠左边，并且缺少孩子节点的父亲节点
        father = self.deque[0]
        new_node = TreeNode(val)

        # time: O(1)
        # 开始插入节点
        if father.left is None:
            father.left = new_node
        else:
            father.right = new_node
            # 如果当前的father的右边也已经填满了，说明不可以再填充该节点，则弹出该节点
            self.deque.popleft()
        
        self.deque.append(new_node) # 需要加入该节点
        return father.val

    def get_root(self) -> Optional[TreeNode]:
        # time: O(1)
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()