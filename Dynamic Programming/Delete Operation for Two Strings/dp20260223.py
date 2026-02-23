# 1. definition: dp[i][j] denotes the minimum number of steps required to make word1[0..i] and word2[0..j] the same
# 2. recurrence relation
# (1) word1[i-1]==word2[j-1]: dp[i-1][j-1]
# (2) word1[i-1]!=word2[j-1]: 
# (2.1) drop word1[i-1]: dp[i-1][j]+1
# (2.2) drop word2[j-1]: dp[i][j-1]+1
# dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
# 3. initialization:
# dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
# dp[i][0] = i dp[0][j] = j
# 4. traversal order: word1 first then word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
        