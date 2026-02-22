# suppose target=a-b, sum_=a+b, then a=(target+sum_)//2
# our job is to find the number of expressions when the volume of the package is a
# 1. definition: dp[j] is the number of methods we can put to make the value of package is j
# 2. recurrence relation:
# use num: dp[j]+=dp[j-num] dp[0] = 1
# when the package volume is 0, then its number of methods should be 1
# 3. initialization: dp=[0]*(target_sum+1)
# 4. traversal order: left to right
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_ = sum(nums)
        target_sum = (target+sum_)//2
        if abs(target)>sum_:
            return 0
        if (target+sum_)%2!=0:
            return 0
        dp = [0]*(target_sum+1)
        dp[0] = 1
        for i in range(len(nums)): # iterate the num in nums
            for j in range(target_sum, -1, -1):
                if j>=nums[i]: 
                    dp[j]+=dp[j-nums[i]]
        return dp[-1]
        