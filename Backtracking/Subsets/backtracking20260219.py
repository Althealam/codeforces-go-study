class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, 0, [], res)
        return res
    
    def backtracking(self, nums, startIndex, path, res):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i+1, path, res)
            path.pop()