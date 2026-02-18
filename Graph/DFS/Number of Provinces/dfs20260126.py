class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for neighbour in range(cities):
                if isConnected[city][neighbour]==1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces+=1

        return provinces  
