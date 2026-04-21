# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 使用graph将树转换为无向图，graph存储的是node->parent
# 2. 使用BFS从target开始进行层序遍历
# - 定义queue
# - 每次遍历到一层的时候，就将其对应的孩子节点和父亲节点存入到队列中，并且计算一下当前的层树
# - 如果到达了对应的层数，则返回队列中的值

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 1. 构建无向图
        graph = {}
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    graph[cur.left] = cur
                    queue.append(cur.left)
                if cur.right:
                    graph[cur.right] = cur
                    queue.append(cur.right)
        

        # 2. 使用BFS遍历
        depth = 0
        bfsqueue = collections.deque([target])
        visited = [target]
        while bfsqueue:
            if depth==k:
                return [node.val for node in bfsqueue]
            for _ in range(len(bfsqueue)):
                node = bfsqueue.popleft()
                for child in [node.left, node.right, graph.get(node)]:
                    if child and child not in visited:
                        bfsqueue.append(child)
                        visited.append(child)
            depth+=1
        return []