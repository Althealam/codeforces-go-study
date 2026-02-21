# 1. definition: dp[i][j] denotes the number of possible unique paths that robot can move to the point(i, j)
# 2. recurrence relation: dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. initialization: dp[i][0],dp[0][j],dp[0][0]
# if obstacleGrid[i][j]==1: dp[i][j]=0
# dp[i][0]=1 dp[0][j]=1 
# dp[0][0]=1
# 4. traversal order: left to right and top to bottom
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]!=1:
                dp[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]!=1:
                dp[0][j]=1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        