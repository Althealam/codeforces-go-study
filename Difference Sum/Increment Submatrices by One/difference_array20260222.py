# grid[i][j]-grid[i][j-1]=diff[i][j]
# grid[i][j]=(grid[i][j]-grid[i][j-1])+(grid[i][j-1]-grid[i][j-2]+...) 
# =diff[i][j]+diff[i][j-1]+...+diff[i][0]

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0]*(n+1) for _ in range(n+1)]

        # 差分数组打标记
        for query in queries:
            row1, col1, row2, col2 = query[0], query[1], query[2], query[3]
            # (row1, col1), (row1, col2), (row2, col1), (row2, col2)
            diff[row1][col1]+=1
            if col2+1<n:
                diff[row1][col2+1]-=1
            if row2+1<n:
                diff[row2+1][col1]-=1
            if col2+1<n and row2+1<n:
                diff[row2+1][col2+1]+=1
        
        # 还原数组
        array = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 上方的值
                up = array[i-1][j] if i>0 else 0
                # 左边的值
                left = array[i][j-1] if j>0 else 0
                # 斜上方的值
                up_left = array[i-1][j-1] if (i>0 and j>0) else 0
                # 递推公式
                array[i][j] = up+left-up_left+diff[i][j]

        return array