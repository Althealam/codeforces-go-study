# 1. defintion: dp[i] is the length of the longest continuous increasing subsequence using element dp[0]..dp[i-1] end with dp[i-1]
# 2. recurrence relation: if nums[i]>nums[i-1]: dp[i] = dp[i-1]+1
# 3. initialization: dp=[1]*len(nums) dp[0] = 1
# 4. traversal order: left to right 0->len(nums)-1
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)

        