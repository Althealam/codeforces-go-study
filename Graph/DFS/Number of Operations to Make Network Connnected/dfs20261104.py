class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(x, y):
            visited[x][y] = True
            for i, j in directions:
                next_x, next_y = x+i, y+j
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]=='1':
                    dfs(next_x, next_y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=='1':
                    count+=1
                    dfs(i, j)
        return count
