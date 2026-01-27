# 思路：要让n个节点变成连通图，至少需要n-1条边
# 连通分量：图中一块已经完全连接的区域
# 目标：假设我们有k个连通分量，我们的目标是变成1个连通分量，那么至少要进行k-1次操作
# 每次操作最多让连通分量的数量减去1，比如1-2-3变成1-2和3，因此从k变成1需要至少k-1次操作
import collections
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 如果边的数量不够，那么无论如何都无法将这个图变成连通图
        if len(connections)<n-1:
            return -1
        
        # 创建邻接表
        grid = collections.defaultdict(list)
        for i, j in connections:
            grid[i].append(j)
            grid[j].append(i)
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in grid[i]:
                if j not in visited:
                    dfs(j)
        
        # 统计连通分量
        ans = 0 # 连通分量的数量
        for i in range(n):
            if i not in visited:
                dfs(i) # 通过dfs找到和i相互连通的节点
                ans+=1 # 连通分量的数量加1

        return ans-1