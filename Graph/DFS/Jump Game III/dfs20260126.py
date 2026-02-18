class Solution:
    def canReach(self, arr, start: int) -> bool:
        n = len(arr)
        visited = set()
        def dfs(i):
            if i<0 or i>=n or i in visited:
                return False
            if arr[i]==0:
                return True
            visited.add(i)
            step = arr[i]
            # 注意本题是可以跳跃到i+step或者是i-step，而不是i+step到i-step的范围内的点都可以跳到
            return dfs(i+step) or dfs(i-step)
        return dfs(start)

        

arr = [3,0,2,1,2]
start = 2
solution = Solution()
print(solution.canReach(arr, start))