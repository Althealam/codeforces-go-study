# 分析：s1-s2 = target, s1+s2 = sum_ => 2s1=target+sum_ => s1=(target+sum_)/2
# 1. dp数组的定义：dp[j]表示让背包容量为j的方法数 最终目的是找到j=(target+sum_)/2时的方法数
# 2. 递推公式
# 使用当前的数字num：dp[j]+=dp[j-num]
# 3. 初始化
# dp[0] = 1 dp = [0]*(target_sum+1)
# 4. 遍历顺序：物品正序遍历，容量逆序遍历
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sum_ = sum(nums)
        target_sum =(target+sum_)//2
        if abs(target)>sum_:
            return 0
        if (target+sum_)%2!=0:
            return 0
        dp = [0]*(target_sum+1)
        dp[0] = 1
        for i in range(len(nums)): # 遍历物品
            for j in range(target_sum, -1, -1): # 遍历背包容量
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]
        return dp[-1]
        