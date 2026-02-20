class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False]*len(nums)
        self.backtracking(nums, res, path, visited)
        return res
    
    def backtracking(self, nums, res, path, visited):
        if len(path[:])==len(nums) and path[:] not in res:
            res.append(path[:])
            return 
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1] and visited[i]:
                continue
            if visited[i]:
                continue
            path.append(nums[i])
            visited[i] = True
            self.backtracking(nums, res, path, visited)
            path.pop()
            visited[i] = False