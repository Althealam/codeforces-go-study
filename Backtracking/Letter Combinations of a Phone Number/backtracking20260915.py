# 时间复杂度：O(n*4^n)，因为每个数字最多对应4个字母，因此搜索数的分支数最多为4，深度为n=len(digits)，时间复杂度为O(4^n)，同时总共有遍历n次，每次4^n的时间复杂度，因此是O(n*4^n)
# 空间复杂度：O(n)，递归深度最多为n，同时path最长也是n，因此空间复杂度为O(n)

class Solution:
    def __init__(self):
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.backtracking(digits, 0, [], res)
        return res
    
    def backtracking(self, digits, startIndex, path, res):
        if len(path[:])==len(digits):
            res.append("".join(path[:]))
            return 
        letters = self.mapping[digits[startIndex]] # 用来定位子搜索树的
        for letter in letters: # 用来遍历搜索树的分支的
            path.append(letter)
            self.backtracking(digits, startIndex+1, path, res)
            path.pop()

