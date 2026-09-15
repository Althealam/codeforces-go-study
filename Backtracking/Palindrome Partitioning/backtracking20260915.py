class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, res, [], 0)
        return res
    
    def backtracking(self, s, res, path, startindex):
        if startindex==len(s):
            res.append(path[:])
            return 
        for i in range(startindex, len(s)): # 遍历切割的位置
            x = s[startindex:i+1] # 找到切割的位置
            if self.is_palindrome(x):
                path.append(x)
                self.backtracking(s, res, path, i+1)
                path.pop()
    
    def is_palindrome(self, x):
        if x==x[::-1]:
            return True
        return False