class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*(n-k+1) for _ in range(m-k+1)]

        for i in range(m-k+1): # 遍历矩阵的每一行
            for j in range(n-k+1): # 遍历矩阵的每一列
                vals = []
                # 获取k*x的小矩阵vals
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        vals.append(grid[x][y])
                
                # 对小矩阵进行排序
                vals.sort()
                min_diff = float('inf')
                # 遍历小矩阵中的元素值，获取差值
                for t in range(1, len(vals)):
                    if vals[t]==vals[t-1]:
                        continue
                    min_diff = min(min_diff, vals[t]-vals[t-1])
                
                if min_diff!=float('inf'):
                    ans[i][j] = min_diff
        return ans