from collections import defaultdict
def dfs(grid, visited, x):
    for neighbor in grid[x]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(grid, visited, neighbor)

def main():
    N, K = map(int, input().split())
    grid = defaultdict(list)
    for _ in range(K):
        s, t = map(int, input().split())
        grid[s].append(t)
    visited = [False]*(N+1)
    visited[1] = True
    dfs(grid, visited, 1)
    for i in range(1, N+1):
        if not visited[i]:
            return -1
    return 1

print(main())