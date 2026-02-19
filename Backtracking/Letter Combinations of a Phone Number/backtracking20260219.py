class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        self.backtracking(digits, res, [], 0, letter_map)
        return res
    
    def backtracking(self, digits, res, path, startIndex, letter_map):
        if len(path[:])==len(digits):
            res.append(''.join(path[:]))
            return 
        letters = letter_map[digits[startIndex]]
        for letter in letters:
            path.append(letter)
            self.backtracking(digits, res, path, startIndex+1, letter_map)
            path.pop()