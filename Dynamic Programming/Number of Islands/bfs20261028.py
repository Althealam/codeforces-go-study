directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
from collections import deque
def bfs(grid, visited, x, y):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        for i, j in directions:
            next_x, next_y = cur_x+i, cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            queue.append([next_x, next_y])

def main():
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
                bfs(grid, visited, i, j)
    return res