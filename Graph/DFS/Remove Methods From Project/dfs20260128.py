from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations):
        grid = defaultdict(list)
        for i, j in invocations:
            grid[i].append(j)

        suspicious = set()
        def dfs(i):
            suspicious.add(i)
            for j in grid[i]:
                if j not in suspicious:
                    dfs(j)
        dfs(k)
        print("Current suspicious nodes set:", suspicious)

        ans = set()
        for i in range(n): # add all nodes which are not suspicious
            if i not in suspicious:
                ans.add(i)

        # 如果有node指向suspicious，则不能删除任何节点
        for i, j in invocations:
            if j in suspicious and i not in suspicious:
                return list(range(n))
        return list(ans)

n = 3
k = 2
invocations =[[1,0],[2,0]]






solution = Solution()
res = solution.remainingMethods(n, k, invocations)
print(res)