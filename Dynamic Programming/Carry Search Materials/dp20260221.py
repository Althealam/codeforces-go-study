# 1. dp数组的定义：dp[i][j]表示从下标[0, i]的物品里任选放到容量为j的背包里，价值总和最大为多少
# 2. 递推公式：
# (1) 不放入物品i：dp[i-1][j]
# (2) 放入物品i：dp[i-1][j-weight[i]]+value[i]
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
# 3. 初始化：dp[i][0]=0
# dp[0][j] = value[0] if j>=weight[0] else 0
# 4. 遍历顺序：先物品后背包 
# dp[i][j]是由dp[i-1][j]推导出来的
m, n = map(int, input().split())

weights = list(map(int, input().split()))
values = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(m)]

for j in range(n+1):
    if j<weights[0]:
        dp[0][j] = 0
    elif j>=weights[0]:
        dp[0][j] = values[0]

for i in range(1, m): # 遍历物品
    # 遍历背包
    for j in range(n+1):
        if j<weights[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+values[i])
print(dp[-1][-1])

