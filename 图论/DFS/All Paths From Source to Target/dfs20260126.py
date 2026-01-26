class Solution:
    def allPathsSourceTarget(self, graph):
        # graph已经是一个有向图了，可以从中访问其节点
        n = len(graph) # the number of nodes

        ans = []

        def dfs(i, path, ans):
            if i==n-1: # already reach the target node
                ans.append(path[:])
                return
            for j in graph[i]: # iterate the neighbor nodes of i
                path.append(j)
                dfs(j, path, ans)
                path.pop()
        
        dfs(0, [0], ans)
        return ans

graph = [[1,2],[3],[3],[]]
solution = Solution()
print(solution.allPathsSourceTarget(graph))