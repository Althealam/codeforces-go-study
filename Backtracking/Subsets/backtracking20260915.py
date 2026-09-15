class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, res, [], 0)
        return res
    
    def backtracking(self, nums, res, path, startIndex):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, res, path, i+1)
            path.pop()