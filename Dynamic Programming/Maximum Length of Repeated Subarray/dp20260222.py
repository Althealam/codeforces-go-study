# 1. definition: dp[i][j] denotes the maximum length of a subarray that appears in both arrays when ends with nums1[i-1] in nums1, and ends with nums2[j-1] in nums2
# 2. recurrence relation: 
# if nums1[i-1]==nums2[j-1]: dp[i][j] = dp[i-1][j-1]+1
# 3. initialization: dp =[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
# 4. traversal order: left to right
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        res = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
                res = max(res, dp[i][j])
        return res