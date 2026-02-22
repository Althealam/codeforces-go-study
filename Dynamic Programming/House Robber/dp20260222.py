# 1. definition: dp[i] is the maximal amount of money you can rob tonight when you iterate the house 0..i
# 2. recurrence relation: dp[i] = max(dp[i-1], dp[i-2]+nums[i])
# 3. initialization: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
# 4. traversal order: left to right

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums)==1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]