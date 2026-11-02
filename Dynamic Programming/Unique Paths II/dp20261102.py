# 1. dp数组的定义：dp[i][j]表示从(0, 0)到(i, j)的可能的唯一路径数
# 2. dp递推公式：
# dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. 初始化：
# dp[0][0] = 1 if obstacleGrid[0][0]!=1
# dp[i][0] = 1 if obstacleGrid[i][0]!=1 
# dp[0][j] = 1 if obstacleGrid[0][j]!=1
# 4. 遍历顺序：从左到右，从上到下
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                break
            else:
                dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

        