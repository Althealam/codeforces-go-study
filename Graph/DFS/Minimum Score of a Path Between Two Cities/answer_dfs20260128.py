from math import inf


class Solution:
    def minScore(self, n: int, roads):
        grid = [[] for _ in range(n)]
        for x, y, d in roads:
            grid[x-1].append((y-1, d))
            grid[y-1].append((x-1, d))
        ans = inf
        vis = [False]*n
        def dfs(x):
            nonlocal ans
            vis[x] = True
            for y, d in grid[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)
        dfs(0)
        return ans