class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sum = [[0]*n for _ in range(m)]
        for i in range(m):
            if i==0:
                prefix_sum[0][0] = grid[0][0]
            else:
                prefix_sum[i][0] = prefix_sum[i-1][0]+grid[i][0]
        for j in range(n):
            if j==0:
                prefix_sum[0][0] = grid[0][0]
            else:
                prefix_sum[0][j] = prefix_sum[0][j-1]+grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                prefix_sum[i][j] = prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+grid[i][j]
        count = 0
        for i in range(m):
            for j in range(n):
                if prefix_sum[i][j]<=k:
                    count+=1
        return count


        