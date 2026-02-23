# 1. definition: dp[i][j] denotes whether s[i..j] is a palindromic strings
# 2. recurrence relation
# if s[i]==s[j]:
# (1) i==j: True
# (2) j-i==1: True
# (3) j-i>1: dp[i][j] = dp[i+1][j-1]
# 3. initialization: dp = [[False]*(len(s)+1) for _ in range(len(s)+1)]
# dp[i][i] = True
# 4. traversal order:  i+1->i j-1->j i: right->left j: left->right
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][i] = True
        count = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if i==j or j-i==1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    count+=1
        return count