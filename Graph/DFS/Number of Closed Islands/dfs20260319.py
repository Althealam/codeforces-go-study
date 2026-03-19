# 1. 先将四个边界的岛屿变成海水
# 2. 遍历grid，找到岛屿的数量
class Solution:
    def __init__(self):
        self.directions = [[1,0],[0,1],[-1,0],[0,-1]]
        self.grid = None
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if self.grid[i][0]==0:
                self.dfs(i, 0)
            if self.grid[i][n-1]==0:
                self.dfs(i, n-1)
        for j in range(n):
            if self.grid[0][j]==0:
                self.dfs(0, j)
            if self.grid[m-1][j]==0:
                self.dfs(m-1, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j]==0:
                    ans+=1
                    self.dfs(i, j)
        return ans

    def dfs(self, i, j):
        self.grid[i][j] = 1
        for dx, dy in self.directions:
            nxt_x, nxt_y = i+dx, j+dy
            if nxt_x<0 or nxt_y<0 or nxt_x>=len(self.grid) or nxt_y>=len(self.grid[0]):
                continue
            if self.grid[nxt_x][nxt_y]==0:
                self.dfs(nxt_x, nxt_y)


        