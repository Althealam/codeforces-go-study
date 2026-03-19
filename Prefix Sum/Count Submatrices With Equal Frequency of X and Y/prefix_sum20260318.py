class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        pre_x = [[0]*(n+1) for _ in range(m+1)]
        pre_y = [[0]*(n+1) for _ in range(m+1)]
        count = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pre_x[i+1][j+1] = pre_x[i][j+1]+pre_x[i+1][j]-pre_x[i][j]+(x=='X')
                pre_y[i+1][j+1] = pre_y[i][j+1]+pre_y[i+1][j]-pre_y[i][j]+(x=='Y')
                if pre_x[i+1][j+1]==pre_y[i+1][j+1] and pre_x[i+1][j+1]>=1:
                    count+=1
        return count