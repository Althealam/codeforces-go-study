# 1. definition: dp[i][j] is the length of their longest common subsequence with text1[0...i] and text2[0..j]
# 2. recurrence relation
# if text1[i-1]==text2[j-1]:
# dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])
# 3. initialization:
# dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
# 4. traversal order: left to right
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        res = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=max(dp[i-1][j-1]+1, dp[i][j])
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1], dp[i][j])
                res = max(res, dp[i][j])
        return res


text1 = 'abcde'
text2 = 'ace'
sol = Solution()
res = sol.longestCommonSubsequence(text1, text2)
print(res)