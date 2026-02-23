# 1. definition: dp[i] means the largest sum with nums[0..i]
# 2. recurrence relation:
# if dp[i-1]+nums[i]<0: dp[i] = nums[i]
# (1) dp[i-1]+nums[i]
# (2) nums[i]
# dp[i] = max(dp[i-1]+nums[i], dp[i-1])
# 3. initialization: dp = [0]*len(nums)
# dp[0] = nums[0]
# 4. traversal order: left to right
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        res = nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
            print(f'current dp[i] is {dp[i]} and current nums[i] is {nums[i]}')
        return res

nums = [-1, -2]
sol = Solution()
res = sol.maxSubArray(nums)
print(res)