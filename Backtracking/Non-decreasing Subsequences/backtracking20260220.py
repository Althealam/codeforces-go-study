class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backtracking(res, nums, [], 0)
        return res
    
    def backtracking(self, res, nums, path, startIndex):
        if len(path)>=2 and path[:] not in res:
            res.append(path[:])
        # print(f'current res is {res}')
        for i in range(startIndex, len(nums)):
            if len(path)!=0 and nums[i]<path[-1]:
                continue
            path.append(nums[i])
            self.backtracking(res, nums, path, i+1)
            path.pop()

nums = [4, 4, 3, 2, 1]
sol = Solution()
print(sol.findSubsequences(nums))