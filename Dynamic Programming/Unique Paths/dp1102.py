# 1. dp数组的定义：dp[i][j]表示从起点到(i, j)的可能路径数
# 2. dp递推公式：dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. 初始化：
# dp[i][0] = dp[i-1][0], dp[0][j] = dp[0][j-1], dp[0][0] = 1
# 4. 遍历顺序：从左到右，从上到下
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        