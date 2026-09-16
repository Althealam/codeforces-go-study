class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, res, [], 0)
        return res
    
    def backtracking(self, nums, res, path, startindex):
        if len(path[:])>=2 and path not in res:
            res.append(path[:]) # 如果这后面加上了一个return，则会导致长度一达到2就结束递归，不继续往下搜索
        for i in range(startindex, len(nums)):
            if len(path)!=0 and nums[i]<path[-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, res, path, i+1)
            path.pop()
