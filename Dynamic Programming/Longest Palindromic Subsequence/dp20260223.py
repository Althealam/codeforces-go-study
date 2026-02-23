# 1. definition: dp[i][j] denotes the length of the longest subsequence with s[i..j] (start with s[i] and ends with s[j])
# 2. recurrence relation: 
# (1) s[i]==s[j]: dp[i][j] = dp[i+1][j-1]+2
# (2) s[i]!=s[j]: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# 3. initialization: 
# dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
# dp[i][i] = 1
# 4. traversal order: i+1->i j-1->j 
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        res = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
