class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.backtracking(s, res, [], 0)
        return res
    
    def backtracking(self, s, res, path, split_index):
        if split_index==len(s) and len(path[:])==4:
            res.append('.'.join(path[:]))
            return 
        for i in range(split_index, len(s)):
            x = s[split_index:i+1]
            if self.is_valid(x[:]):
                path.append(x[:])
                self.backtracking(s, res, path, i+1)
                path.pop()
    
    def is_valid(self, x):
        if int(x)>255 or int(x)<0:
            return False
        if len(x)!=1 and int(x[0])==0:
            return False
        return True
