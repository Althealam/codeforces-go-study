# 1. definition: dp[i][j] is the number of the subset when there are at most i o and j 1
# 2. recurrence relation
# (1) use new str: dp[i-zeroNum][j-oneNum]+1
# (2) don't use new str: dp[i][j]
# dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. initialization: dp=[[0]*(n+1) for _ in range(m+1)]

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs: # iterate the element in the package
            oneNum = s.count('1')
            zeroNum = s.count('0')
            for j in range(n, -1, -1): # iterate the package
                for i in range(m, -1, -1):
                    if i>=zeroNum and j>=oneNum:
                        dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
        return dp[-1][-1]