# 1. definition of dp: dp[i][j] denotes the number of possible unique paths which lead to the point (i, j)
# 2. recurrence relation: dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. initialization: dp[i][0] and dp[0][j]
# dp[i][0] = dp[i-1][0] dp[0][j] = dp[0][j-1] dp[0][0] = 1
# 4. traversal order: from left to right and from top to bottom
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
        