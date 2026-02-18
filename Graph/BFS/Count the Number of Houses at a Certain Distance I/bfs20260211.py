# 统计house1和house2之间最短距离为k的pairs
from collections import defaultdict, deque
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        graph = defaultdict(list)
        for i in range(1, n):
            graph[i].append(i+1)
            graph[i+1].append(i)
        if x!=y:
            graph[x].append(y)
            graph[y].append(x)
        
        def bfs(node):
            dist = [-1]*n # the minimal distance starting from node 
            dist[node-1] = 0 
            q = deque()
            q.append(node)
            while q:
                cur_node = q.popleft()
                for neighbor_node in graph[cur_node]:
                    if dist[neighbor_node-1]==-1: # we haven't visited this node currently
                        dist[neighbor_node-1] = dist[cur_node-1]+1
                        q.append(neighbor_node)
            return dist

        ans = [0]*n
        for i in range(1, n+1): # iterate all nodes
            dist = bfs(i) # get the distance array of node i
            for j in range(1, n+1): # iterate the mindistance from node i to node j
                if i!=j:
                    ans[dist[j-1]-1]+=1
        return ans

n = 3
x = 1
y = 3
solution = Solution()
res = solution.countOfPairs(n, x, y)
print(res)