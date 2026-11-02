# 1. dp数组的定义：dp[i]表示将i拆分为多个整数时的最大乘积
# 2. 递推公式
# dp[i] = j*(i-j)
# dp[i] = j*dp[i-j]
# dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
# 3. 初始化：dp[0]=0, dp[1]=0, dp[2]=1
# 4. 先遍历i，再遍历j
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        if n<2:
            return dp[n]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[-1]