directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(grid, visited, x, y):
    cur_area = 1 # 刚开始遍历这个部分
    for i, j in directions:
        next_x, next_y = x+i, y+j
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if not visitd[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y] = True
            cur_area+=dfs(grid, visited, next_x, next_y, cur_area)
    return cur_area

        
def main():
    max_area = 0
    m, n = map(int, input().split())
    visited = [[False]*n for _ in range(m)]
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j]==1:
                visited[i][j] = True
                cur_area = dfs(grid, visited, i, j)
                max_area = max(max_area, cur_area)
    print(max_area)

main()