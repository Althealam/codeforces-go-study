def dfs(grid, visited, node, destination):
    if node == destination:
        return True
    for i in range(1, len(grid)):
        if not visited[i] and grid[node][i]:
            visited[i] = True
            if dfs(grid, visited, i, destination):
                return True
    return False
    
def main():
    n, m = map(int, input().split())
    grid = [[False]*(m+1) for _ in range(n+1)]
    for i in range(m):
        s, t = map(int, input().split())
        grid[s][t] = True
        grid[t][s] = True
    source, destination = map(int, input().split())
    visited = [False]*(n+1)
    if dfs(grid, visited, source, destination):
        return 1
    return 0

print(main())