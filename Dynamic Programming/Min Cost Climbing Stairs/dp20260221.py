# 1. definition: dp[i] denotes the minimal cost when climbs to i th step
# 2. recurrence relation: 
# (1) climb one: dp[i-1]+cost[i-1]
# (2) climb two: dp[i-2]+cost[i-2]
# dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
# 3. initialization: 
# dp[0] = 0
# dp[1] = 0
# because you can either start from the step with index 0 or the step with index 1 ==> dp[0]=dp[1]=0
# 4. traversal order: left to right
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]