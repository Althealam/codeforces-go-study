class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, [], res, 1)
        return res
    
    def backtracking(self, n, k, path, res, startIndex):
        if sum(path[:])==n and len(path[:])==k:
            res.append(path[:])
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.backtracking(n, k, path, res, i+1)
            path.pop()