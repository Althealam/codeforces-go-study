# 1. definition of dp: dp[i] denotes the number of methods when climbs to i level
# 2. recurrence relation: dp[i] = dp[i-2]+dp[i-1]
# 3. initialization: dp[0]=0 dp[1]=1 dp[2]=2
# 4. traversal order: left to right
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n==0:
            return 0
        if n==1:
            return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

        