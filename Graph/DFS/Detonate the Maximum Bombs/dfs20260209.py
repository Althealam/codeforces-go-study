# 从有向图的某个点出发，最多可以涉及到多少个点
from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n): # iterate all nodes in bombs
            x1, y1, r1 = bombs[i]
            for j in range(n): # iterate all nodes which (x1, y1) can bomb
                if i==j:
                    continue
                x2, y2, r2 = bombs[j]
                dx = x1-x2
                dy = y1-y2
                if dx*dx+dy*dy<=r1*r1: # node i could bomb j
                    graph[i].append(j)
        
        def dfs(node):
            effect_nodes = 1
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    effect_nodes+=dfs(neighbor)
            return effect_nodes
        ans = 0
        for i in range(n): 
            visited = set()
            # dfs(i)获得从(x[i], y[i])出发时可以炸到的最多节点数
            ans = max(ans, dfs(i))
        return ans
        

bombs = [[1, 1, 5], [10, 10, 5]]
solution = Solution()
res = solution.maximumDetonation(bombs)
print(res)