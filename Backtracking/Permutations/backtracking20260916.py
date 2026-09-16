class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.backtracking(nums, res, [])
        return res
    
    def backtracking(self, nums, res, path):
        if len(path[:])==len(nums): 
            res.append(path[:])
            return
        for i in range(len(nums)): # 全排列，不需要限制startindex，因为startindex是限制搜索树的分支顺序的
            if nums[i] in path[:]:
                continue
            path.append(nums[i])
            self.backtracking(nums, res, path)
            path.pop()