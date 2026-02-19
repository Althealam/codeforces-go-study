class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 遇到会出现重复元素的情况，就排序数组
        candidates.sort()
        self.backtracking(candidates, target, [], res, 0)
        return res
    
    def backtracking(self, candidates, target, path, res, startIndex):
        if sum(path[:])==target:
            res.append(path[:])
            return 
        if sum(path[:])>target:
            return 
        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, target, path, res, i+1)
            path.pop()