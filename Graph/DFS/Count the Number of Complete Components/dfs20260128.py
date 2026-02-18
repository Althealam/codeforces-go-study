# 注意：完全连通图中任意两个点之间都有边
# 完全图的边数为n*(n-1)//2
from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges) -> int:
        grid = defaultdict(list)
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)
        
        visited = [False]*n

        def dfs(i, comp):
            visited[i]=True
            comp.add(i)
            for j in grid[i]:
                if not visited[j]:
                    dfs(j, comp)
        
        ans = 0
        for i in range(n):
            if not visited[i]: # 找到了一个新的连通图
                comp = set()
                dfs(i, comp) # 

                k = len(comp) # 该连通图的节点数
                # 将该连通图中所有节点的度数加起来
                # 因为无向边会被计数两次，因此除以2
                # edge_cnt是该无向图中边的个数
                edge_cnt = sum(len(grid[u]) for u in comp)//2

                if edge_cnt==k*(k-1)//2:
                    ans+=1
        return ans

n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
solution = Solution()         
ans = solution.countCompleteComponents(n, edges)
print(ans)
