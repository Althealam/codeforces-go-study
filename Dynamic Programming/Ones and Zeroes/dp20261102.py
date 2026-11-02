# 1. dp数组的定义：dp[i][j]是拥有最多i个0和j个1的子集的数量
# 2. 递推公式
# - 使用新的num：dp[i-zeroNum][j-oneNum]+1
# - 不使用新的num：dp[i][j]
# dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：正序遍历物品，逆序遍历背包容量
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs: # 遍历物品
            oneNum = s.count("1")
            zeroNum = s.count("0")
            for j in range(n, -1, -1): # 逆序遍历背包
                for i in range(m, -1, -1): # 逆序遍历背包
                    if i>=zeroNum and j>=oneNum:
                        dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[-1][-1]