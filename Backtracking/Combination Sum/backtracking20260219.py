class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(candidates, target, res, [], 0)
        return res
    
    def backtracking(self, candidates, target, res, path, startIndex):
        if sum(path[:])==target:
            res.append(path[:])
            return 
        if sum(path[:])>target:
            return
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target, res, path, i)
            path.pop()