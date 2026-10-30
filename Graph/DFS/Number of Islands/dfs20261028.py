direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(grid, visited, x, y):
    """
    对一块陆地进行dfs并且标记
    """
    for i, j in direction:
        next_x = x+i
        next_y = y+j
        # 下标越界
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        # 未访问的陆地则标记后用dfs
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y] = True
            dfs(grid, visited, next_x, next_y)

if __name__=='__main__':
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    visited = [[False]*m for _ in range(n)]

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and not visited[i][j]:
                res+=1
                visited[i][j] = True
                dfs(grid, visited, i, j)
    
    print(res)