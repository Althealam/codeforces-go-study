# 时间复杂度：搜索树的深度最多为target/min(candidates)，分支的最多数量为m=len(candidates)
# 因此时间复杂度为O(m^(target/a))
# 空间复杂度：O(target/min(candidates))，因为递归树的深度最多为target/min(candidates)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(res, [], candidates, target, 0)
        return res
    
    def backtracking(self, res, path, candidates, target, startIndex):
        if sum(path[:])==target:
            res.append(path[:])
            return 
        if sum(path[:])>target:
            return 
        for i in range(startIndex, len(candidates)): # 遍历搜索树的分支
            path.append(candidates[i]) # 加入其中一个分支的值
            self.backtracking(res, path, candidates, target, i) # 回溯，继续找下一个位置
            path.pop() # 弹出该分支的值
        