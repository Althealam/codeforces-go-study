# 时间复杂度：每个回溯的时间复杂度为O(2^n)，并且总共会执行n次，同时前面有排序的逻辑，因此时间复杂度为O(nlogn+n2^n)
# 空间复杂度：递归最深最多选择n个元素，path最长也是n，因此为O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.backtracking(candidates, target, res, [], 0)
        return res
    
    def backtracking(self, candidates, target, res, path, startindex):
        if sum(path[:])==target:
            res.append(path[:])
            return 
        if sum(path[:])>target:
            return 
        for i in range(startindex, len(candidates)): # 递归搜索树的分支
            if i>startindex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, target, res, path, i+1)
            path.pop()