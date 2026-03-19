# 1. 使用DFS，将四个边界相邻的岛屿给沉没
# 2. 遍历grid，统计还没有被沉没的子点的数量

class Solution:
    def __init__(self):
        self.grid = None
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if self.grid[i][0]==1:
                self.dfs(i, 0)
            if self.grid[i][n-1]==1:
                self.dfs(i, n-1)
        for j in range(n):
            if self.grid[0][j]==1:
                self.dfs(0, j)
            if self.grid[m-1][j]==1:
                self.dfs(m-1, j)

        count = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j]==1:
                    count+=1
        return count
            
    def dfs(self, i, j):
        self.grid[i][j] = 0
        for dx, dy in self.directions:
            nxt_x, nxt_y = i+dx, j+dy
            if nxt_x<0 or nxt_y<0 or nxt_x>=len(self.grid) or nxt_y>=len(self.grid[0]):
                continue
            if self.grid[nxt_x][nxt_y]==1:
                self.dfs(nxt_x, nxt_y)
        
        