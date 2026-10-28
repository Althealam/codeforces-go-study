import collections
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def bfs(grid, visited, x, y):
    area = 1
    queue = collections.deque([])
    queue.append([x, y])
    while queue:
        cur_x, cur_y = queue.popleft()
        for i, j in directions:
            next_x, next_y = cur_x+i, cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])
                area+=1
    return area
        
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
                cur_area = bfs(grid, visited, i, j)
                max_area = max(max_area, cur_area)
    print(max_area)

main()