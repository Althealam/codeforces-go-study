# BFS常用于最短路径问题
from collections import defaultdict, deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i+1)
    
        ans = []
        
        def bfs():
            dist = [-1]*n # dist存储的是从0到i节点的最短路径
            q = deque()
            dist[0] = 0
            q.append(0)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v]==-1:
                        dist[v] = dist[u]+1
                        q.append(v)
            return dist[n-1]

        for u, v in queries:
            graph[u].append(v) # 增加新的路径到graph中
            ans.append(bfs()) # 寻找最短的路径
        return ans

n = 5
queries = [[2,4],[0,2],[0,4]]
solution = Solution()
res = solution.shortestDistanceAfterQueries(n, queries)
print(res)
