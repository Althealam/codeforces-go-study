class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        s = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i+1][j]+s[i][j+1]-s[i][j]+x
                if s[i+1][j+1]<=k:
                    ans+=1
        return ans