# 1. dp数组的定义：dp[j]是当背包最大容量为j时，我们可以放进去的最大价值
# 2. 递归公式
#（1）不使用当前物品i：dp[j]
#（2）使用当前物品i：dp[j-nums[i]]+nums[i]
# dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
# 3. 初始化：dp[i]=0
# 4. 顺序：物品从前往后遍历，容量从大到小遍历 -> 容量倒序是为了保证每个数字只能用一次
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp = [0]*(target+1)
        for i in range(len(nums)): # 遍历物品
            for j in range(target, -1, -1): # 遍历背包
                if j>=nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        if dp[target]==target:
            return True
        return False
        