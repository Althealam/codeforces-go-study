class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, [], res, 0)
        return res
    
    def backtracking(self, s, path, res, startIndex):
        if startIndex==len(s):
            res.append(path[:])
            return 
        for i in range(startIndex, len(s)):
            x = s[startIndex:i+1]
            if self.is_palindrome(x[:]):
                path.append(x[:])
                self.backtracking(s, path, res, i+1)
                path.pop()
    
    def is_palindrome(self, s):
        if s==s[::-1]:
            return True
        return False