class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms) # the number of rooms
        grid = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in rooms[i]:
                grid[i][j] = True
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if grid[i][j] is True and j not in visited:
                    dfs(j)
        dfs(0)
        if len(visited)==n:
            return True
        return False

rooms = [[1,3],[3,0,1],[2],[0]]
solution = Solution()
print(solution.canVisitAllRooms(rooms))