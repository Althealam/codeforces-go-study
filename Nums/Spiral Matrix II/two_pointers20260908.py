# 时间复杂度：O(n^2) 每个for循环走n次，每个while循环也是最多n次
# 空间复杂度：O(n^2)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        left, right = 0, n-1 # left=0, right=2
        top, bottom = 0, n-1 # top=0, bottom=2
        num = 1
        while left<=right and top<=bottom:
            for j in range(left, right+1): # [0, 3), [1, 2)
                res[top][j] = num
                num+=1
            top+=1 # top=1, bottom=2
            for i in range(top, bottom+1): # [1, 3)
                res[i][right] = num
                num+=1
            right-=1 # left=0, right=1
            for j in range(right, left-1, -1): # [1, -1)
                res[bottom][j] = num
                num+=1
            bottom-=1 # top=1, bottom=1
            for i in range(bottom, top-1, -1): # [1, 1)
                res[i][left] = num
                num+=1
            left+=1 # left=1, right=1
        return res