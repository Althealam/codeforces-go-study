from typing import Any
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges) -> int:
        grid = [[]*n for _ in range(n)]
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)

        # visited用来标识是否访问过这个点，如果访问过，则说明这个点在某一个连通块中
        visited = [False]*n
        def dfs(x):
            visited[x] = True
            size = 1
            for y in grid[x]:
                if not visited[y]:
                    size+=dfs(y)
            return size # 当前连通块的大小为size，那么当前连通块中的每个点，和之前连通块中的每个点都是无法相互到达的，因此总共有size*total个
        
        ans = total = 0
        # total是之前连通块中的点数，ans是当前连通块中的点数和之前连通块中点数的乘积
        for i in range(n): # 遍历所有点，如果当前点没有访问过，则找到了一个新的连通块
            if not visited[i]: # 未访问的点，说明找到了一个新的连通块
                size = dfs(i)
                ans+=size*total
                total+=size
        return ans
        

n = 5
edges = [[1,0],[3,1],[0,4],[2,1]]

solution = Solution()
print(solution.countPairs(n, edges))