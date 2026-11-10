# 二维前缀和：
# 1. 需要多次查询矩阵中某个矩形区域的元素之和
# 2. 矩阵初始化方法不会改变，并且每次查询必须是O(1)
# 前缀和矩阵
# pre[i][j] = pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+matrix[i-1][j-1]
# 计算矩阵区域和
# sumRegion = pre[row2+1][col2+1]-pre[row1][col2+1]-pre[row2+1][col1]+pre[row1][col1]
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0]*n for _ in range(m)] # 表示从(i-1, j-1)到(0, 0)的区域面积
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    self.pre[0][0] = matrix[0][0]
                elif i==0:
                    self.pre[0][j] = self.pre[0][j-1]+matrix[0][j]
                elif j==0:
                    self.pre[i][0] = self.pre[i-1][0]+matrix[i][0]
                else:
                    self.pre[i][j] = self.pre[i-1][j]+self.pre[i][j-1]-self.pre[i-1][j-1]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.pre[row2][col2]
        if row1>0:
            res-=self.pre[row1-1][col2]
        if col1>0:
            res-=self.pre[row2][col1-1]
        if row1>0 and col1>0:
            res+=self.pre[row1-1][col1-1]
        return res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)