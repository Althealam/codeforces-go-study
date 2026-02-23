# 1. definition: dp[i][j] denotes the maximal length of duplicate subsequence for s[0..i] and t[0..j]
# 2. recurrence relation
# if s[i-1]==t[j-1]: dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])
# 3. initialization:
# dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
# 4. traversal order: left to right
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])

        if dp[-1][-1]==len(s):
            return True
        return False

s = "abc" 
t = "ahbgdc" 
sol = Solution()
res = sol.isSubsequence(s, t)
print(res)