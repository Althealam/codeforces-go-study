# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1. 将树转换为无向图
# - 利用层序遍历，每次遍历到节点的时候，则获取其子节点，并且构建子节点到父亲节点的映射
# 2. 利用BFS，从target开始（因为target是一个treenode）一层层遍历，当到达第k层的时候则收集结果
# 注意：bfs_queue中存储的就是某一层的节点，所以不需要另外创建数组来存储，只要返回队列即可
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        graph = {}
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    graph[node.left] = node
                if node.right:
                    queue.append(node.right)
                    graph[node.right] = node
        
        bfs_queue = collections.deque([target])
        depth = 0
        visited = {target} # 一定要记录，否则会导致超出时间限制，重复访问节点
        # 比如当我到达5的父亲节点3的时候，我将父亲节点加入到bfs_queue中，并且继续访问父亲节点的左右孩子节点，导致了重复访问
        while bfs_queue:
            if depth==k:
                return [node.val for node in bfs_queue]
            for _ in range(len(bfs_queue)):
                node = bfs_queue.popleft()
                for neighbor in [node.left, node.right, graph.get(node)]:
                    if neighbor and neighbor not in visited:
                        bfs_queue.append(neighbor)
                        visited.add(neighbor)
            depth+=1
        return []