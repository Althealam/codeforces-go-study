from collections import defaultdict


class Solution:
    def getAncestors(self, n: int, edges):
        grid = defaultdict(list)
        for i, j in edges: # i->j
            grid[i].append(j)
        # print("Grid:", grid)

        def dfs(i, visited):
            for j in grid[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j, visited)
        
        parent_son = defaultdict(list)
        for i in range(n): # iterate all nodes and find whether this node is the ancestor of other node
            # print("Current node is:", i)
            visited = set() # this is the visited set for node i, which means starting with the node i, you can reach the node in the visited set
            dfs(i, visited)
            # print("Visited:", visited)
            parent_son[i]=list(visited)

        # print("parent_son:", parent_son)
        ans = [[] for _ in range(n)] # 注意：这里不可以是ans = [[]*n] 只会生成一个空列表
        for parent, sons in parent_son.items():
            for son in sons:
                ans[son].append(parent)
        print(ans)
        return ans

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
solution = Solution()
ans = solution.getAncestors(n, edgeList)
