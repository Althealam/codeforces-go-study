class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, res, [], 1)
        return res
    
    def backtracking(self, n, k, res, path, startIndex):
        if len(path[:])==k:
            res.append(path[:])
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.backtracking(n, k, res, path, i+1)
            path.pop()