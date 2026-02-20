class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, res, [])
        return res
    
    def backtracking(self, nums, res, path):
        if len(path[:])==len(nums):
            res.append(path[:])
            return 
        for i in range(len(nums)):
            if nums[i] in path[:]:
                continue
            path.append(nums[i])
            self.backtracking(nums, res, path)
            path.pop()