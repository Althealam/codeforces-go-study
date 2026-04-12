# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：
# 1. 将二叉树转换为无向图
# 2. 层序遍历二叉树，向三个地方扩散，寻找距离为k的节点

class Solution:
    def __init__(self):
        self.root = None

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.root = root

        # 1. 构建父亲节点的映射（子->父）
        graph = {}
        queue = collections.deque([self.root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    graph[node.left] = node
                    queue.append(node.left)
                if node.right:
                    graph[node.right] = node
                    queue.append(node.right)
        
        # 2. 从target开始进行层序遍历，相当于BFS向三个地方扩散
        res_queue = collections.deque([target])
        visited = {target}
        distance = 0
        while res_queue:
            if distance==k: # 到达了距离为k的地方
                return [node.val for node in res_queue]
            for _ in range(len(res_queue)):
                cur = res_queue.popleft()
                for neighbor in [cur.left, cur.right, graph.get(cur)]:
                    if neighbor and neighbor not in visited:
                        res_queue.append(neighbor)
                        visited.add(neighbor)
            distance+=1
        return []

    
