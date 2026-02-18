from typing import Any

# 获取从0到x的最短颜色交替路径长度
from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))
        
        def bfs():
            dist = [[-1, -1] for _ in range(n)] 
            # dist[i][0] means the min distance from 0 to i and its last edge is red
            # dist[i][1] measn the min distance from 0 to i and its last edge is blue
            dist[0][0] = 0
            dist[0][1] = 0

            q = deque[Any]()
            # q store all the pairs
            q.append((0, 0))
            q.append((0, 1))

            while q:
                node, last_color = q.popleft()
                for neighbor_node, neighbor_color in graph[node]:
                    if neighbor_color!=last_color:
                        if dist[neighbor_node][neighbor_color] == -1: # haven't visited this pair
                            dist[neighbor_node][neighbor_color] = dist[node][last_color]+1
                            q.append((neighbor_node, neighbor_color))

            return dist

        dist = bfs()
            
        ans = []
        for i in range(n):
            red_dist = dist[i][0]
            blue_dist = dist[i][1]

            if red_dist==-1 and blue_dist==-1:
                ans.append(-1)
            elif red_dist==-1:
                ans.append(blue_dist)
            elif blue_dist==-1:
                ans.append(red_dist)
            else:
                ans.append(min(blue_dist, red_dist))
        return ans

        

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []
res = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
print(res)