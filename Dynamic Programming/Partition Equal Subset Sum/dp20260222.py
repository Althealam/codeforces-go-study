# target = sum(nums)//2
# analysis: whether can we find a package which satisfy that its package could fullfill target=sum(nums)//2
# 1. definition: dp[j] is the maximal value we can put into the package when the package volume is j
# we just need to check dp[target]==target
# 2. formula:
# (1) don't use i: dp[j]
# (2) use i: dp[j-nums[i]]+nums[i]
# dp[i] = max(dp[j], dp[j-nums[i]]+nums[i])
# 3. initialization: dp[i]=0
# 4. traversal order: left -> right
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp = [0]*(target+1)
        for i in range(len(nums)): # iterate element
            for j in range(target, -1, -1): # iterate package volume
                if j>=nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        if dp[target]==target:
            return True

        return False