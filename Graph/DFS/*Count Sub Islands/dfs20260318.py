# 思路：把grid2中不是子岛的给淹掉，剩下的岛屿数量就是子岛的数量。注意，要删除的是非法子岛，而不是非法的子点
# 什么情况下不是子岛：在grid1中是海水，但是在grid2中是岛屿；在grid2中本来就是海水

# 使用dfs找到grid2中非子岛的岛屿
class Solution:
    def __init__(self):
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.grid1 = None
        self.grid2 = None

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.grid1 = grid1
        self.grid2 = grid2
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid1[i][j]==0 and grid2[i][j]==1:
                    self.dfs(i, j)
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]==1:
                    count+=1
                    # dfs
                    self.dfs(i, j)       
        return count
    
    def dfs(self, i, j):
        self.grid2[i][j] = 0
        for dx, dy in self.directions:
            next_x, next_y = i+dx, j+dy
            if next_x<0 or next_y<0 or next_x>=len(self.grid2) or next_y>=len(self.grid2[0]):
                continue
            if self.grid2[next_x][next_y]==1: 
                self.dfs(next_x, next_y)
