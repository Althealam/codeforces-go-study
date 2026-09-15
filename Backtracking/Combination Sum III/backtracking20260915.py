# 时间复杂度：k* C(9, k)
# 空间复杂度：O(k)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking(res, n, k, [], 1)
        return res
    
    def backtracking(self, res, n, k, path, startIndex):
        if sum(path[:])==n and len(path[:])==k:
            res.append(path[:])
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.backtracking(res, n, k, path, i+1)
            path.pop()