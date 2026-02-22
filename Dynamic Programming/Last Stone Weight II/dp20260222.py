# suppose the weight of the first stones set is x, then the other one is sum(stones)-x
# hence, their left weight of stones is sum(stones)-2*x
# we need to let x be close to sum(stones)//2
# then we need to get the maximal volume when the volume of the package is target=sum(stones)//2

# 1. definition: dp[i] is the maximal value when the volume of the package is i
# 2. recurrence relation: 
# (1) use stone i: dp[j-stones[i]]+stones[i]
# (2) don't use stone i: dp[j]
# dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
# 3. initialization: dp = [0]*(30*100+1)
# 4. traversal order: left->right
# return sum(stones)-2*dp[target]
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum//2 
        dp = [0]*(target+1)
        for i in range(len(stones)): # iterate stone
            for j in range(target,-1,-1):
                if j>=stones[i]:
                    dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return total_sum-2*dp[target]

        