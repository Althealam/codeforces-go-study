# 1. definition of dp: dp[i] is the length of the longest strictly increasing subsequence from nums[0] to nums[i-1] when end with nums[i-1]
# 2. recurrence formula:
# if nums[j]>nums[i]: dp[j]=max(dp[j], dp[i]+1)
# 3. initialization: dp=[1]*len(nums) dp[0] = 1
# 4. traversal order: left to right iterate j first, then iterate i
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        dp[0] = 1
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j]>nums[i]: # iterate all the subsequence in [0..j-1]
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp) # not dp[-1]
        