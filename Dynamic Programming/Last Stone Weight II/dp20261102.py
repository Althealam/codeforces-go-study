# 将石头分成终点尽量接近的两组，求两组重要差的最小值
# 假设重量为total，较轻的一组重量为s（s<total/2），那么(total-s)-s=total-2s是重量差值
# 1. dp数组的定义：dp[j]表示容量为j时，能装进去的最大石头重量
# 2. 递推公式
# 不使用当前的石头：dp[j]
# 使用当前的石头：dp[j-stone]+stone
# dp[j] = max(dp[j], dp[j-stone]+stone)
# 3. 初始化：dp = [0]*(30*300+1) 最多有30个石头，每个石头的重量最多为100
# 4. 顺序：由于石头只能被放进去一次，因此物品是顺序遍历，容量是倒序遍历

class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total_sum = sum(stones)
        target = total_sum//2
        dp = [0]*(target+1)
        for stone in stones: # 遍历物品
            for j in range(target, -1, -1): # 遍历背包容量
                if j>=stone:
                    dp[j] = max(dp[j], dp[j-stone]+stone)
        return total_sum-2*dp[target]
        