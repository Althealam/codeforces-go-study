# 1. definition: dp[i] denotes the number of structurally unique BST when has i nodes of unique values from 1 to i ==> dp=[0]*(n+1)
# 2. recurrence relation: 
# suppose f(i, n) denotes the number of BST when given n nodes and its root is node i
# dp[n]=f(1, n)+f(2, n)+...+f(n, n)
# Now we can analyze f(i, n): f(i, n) = dp[i-1]*dp[n-i] left tree have i-1 nodes and right tree have n-i nodes
# dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+...+dp[n-1]*dp[0]
# 3. initialization: dp[1] = 1
# 4. order: i first then j
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1 # Null Tree
        dp[1] = 1
        for i in range(2, n+1): # the number of nodes in the tree (node: 1...i)
            for j in range(1, i+1): # iterate its head
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[-1]
