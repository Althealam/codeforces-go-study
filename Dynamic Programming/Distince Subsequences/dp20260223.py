# 1. definition: dp[i][j] means the number of distinct subsequences of s[0..i]  ends with s[i-1] which equals t[0..j] ends with t[j-1]
# 2. recurrence relation
# s[i-1]==t[j-1]
# (1) use s[i-1] to match: dp[i-1][j]
# (2) don't use s[i-1] to match: dp[i-1][j-1]
# s[i-1]!=t[j-1]: dp[i-1][j]
# 3. initialization: dp[i][0] = 1 dp[0][j] = 1 dp[0][0] = 1
# 4. traversal order: s first then t
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        # match s to a None string: just drop all alphabets from the s ==> 1 way
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        