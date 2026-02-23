# 1. definition: dp[i][j] means hte maximum number of connecting lines with nums1[0..i] and nums2[0..j]
# 2. recurrence relation
# if nums1[i-1]==nums2[j-1]: dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])
# 3. initialization:
# dp = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
# 4. traversal order: left to right
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])
                res = max(res, dp[i][j])
        return res
        