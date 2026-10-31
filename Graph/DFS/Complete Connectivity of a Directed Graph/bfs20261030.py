import collections
from collections import defaultdict
def bfs(grid, visited, x):
    queue = collections.deque([])
    queue.append(x)
    while queue:
        cur = queue.popleft()
        for neighbor in grid[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def main():
    N, K = map(int, input().split())
    grid = defaultdict(list)
    for _ in range(K):
        s, t = map(int, input().split())
        grid[s].append(t)
    visited = [False]*(N+1)
    visited[1] = True
    bfs(grid, visited, 1)
    for i in range(1, N+1):
        if not visited[i]:
            return -1
    return 1

print(main())