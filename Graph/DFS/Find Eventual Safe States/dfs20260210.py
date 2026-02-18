# 判断从该node出发的所有路径是否都可以走到terminal node，并且需要判断是否有环
from collections import defaultdict
from platform import node
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        state = [0]*n

        def dfs(u):
            if state[u]==1:
                return False  # 环
            
            if state[u]==2:
                return True
            
            state[u] = 1

            for v in graph[u]:
                if not dfs(v):
                    return False
            
            state[u] = 2
            return True

        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans

solution = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
res = solution.eventualSafeNodes(graph)
print(res)