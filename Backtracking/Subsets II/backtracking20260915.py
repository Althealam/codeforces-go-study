class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backtracking(nums, res, [], 0)
        return res
    
    def backtracking(self, nums, res, path, startindex):
        res.append(path[:])
        for i in range(startindex, len(nums)):
            if i>startindex and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, res, path, i+1)
            path.pop()
