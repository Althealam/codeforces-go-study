# 分析：找到和1在一起的连通块内，最小的路径权重
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads) -> int:
        grid = defaultdict(list)
        for i, j, distance in roads:
            grid[i].append((j, distance))
            grid[j].append((i, distance))
        # print(grid)
        # print(distances)
        min_distance = float('inf')
        visited = set()
        def dfs(i):
            # print("Current node is:", {i})
            nonlocal min_distance
            visited.add(i)
            # 找到当前连通图中的所有点
            for j, distance in grid[i]:
                min_distance = min(min_distance, distance) # 必须要遇到一个点的时候就更新min_distances，否则会跳过一些边
                # print("Current neighbor is:", {j})
                if j not in visited:
                    # nonlocal min_distance # 告诉Python使用的是外层函数的变量，而不是新的局部变量
                    # # 注意，这里不能用min_distance = min()，否则函数会认为min_distance是局部变量
                    # min_distance = min(min_distance, distances[i-1][j-1])
                    # print("Current min distance is:", min_distance)
                    dfs(j)
        dfs(1)
        return min_distance


n = 6
roads = [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]
solution = Solution()
ans = solution.minScore(n, roads)
print(ans)