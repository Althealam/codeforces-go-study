directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(grid, visited, x, y):
    visited[x][y] = True
    grid[x][y] = 0
    for i, j in directions:
        next_x, next_y = x+i, y+j
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            dfs(grid, visited, next_x, next_y)

def main():
    m, n = map(int, input().split())
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))
    visited = [[False]*n for _ in range(m)]
    for i in range(m):
        if not visited[i][0] and grid[i][0]==1:
            visited[i][0] = True
            dfs(grid, visited, i, 0)
        if not visited[i][n-1] and grid[i][n-1]==1:
            visited[i][n-1] = True
            dfs(grid, visited, i, n-1)
    for j in range(n):
        if not visited[0][j] and grid[0][j]==1:
            visited[0][j] = True
            dfs(grid, visited, 0, j)
        if not visited[m-1][j] and grid[m-1][j]==1:
            visited[m-1][j] = True
            dfs(grid, visited, m-1, j)
    
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                res+=1
    return res