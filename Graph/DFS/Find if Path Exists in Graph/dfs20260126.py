class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # NOTE: 这里不要使用grid=[[]*n for _ in range(n)]，当n过大的时候会导致超时
        grid = defaultdict(list)
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)
        
        visited = set()

        def dfs(i):
            visited.add(i) # NOTE：一定要先添加i，否则source==destination的时候会返回False
            if i==destination:
                return True
            # NOTE：这里使用for j in grid[i] 而不是 for j in range(n)，当n过大的时候会超市
            for j in grid[i]: # itearte the neighbour of i
                if j not in visited:
                    visited.add(j)
                    dfs(j)
        
        dfs(source)
        if destination in visited:
            return True
        return False