# 1. when we confirm that (x+H-1, y+W-1) is available for the stamp, then we use the 2d difference array with diff[x][y]+=1 diff[x+H][y]-=1 diff[x][y+W]-=1 diff[x+H][y+W]+=1
# 2. Get the prefix sum from the difference array
# time: O(mn)

# 1. 如何确定某一块可不可以贴邮票（使用二维前缀和）：prefix_sum[i][j]表示从(0, 0)到(i, j)一共包含了多少个1
# 如果prefix_sum[i][j]==0，说明这块地全部是0，因此可以放邮票
# 2. 如何瞬间将某一块地都涂上颜色（使用二维差分）：如果我们需要在(x1, y1)和(x2, y2)之间贴一个邮票，那么就在这个矩形的四个角打上+1和-1的标签
# 3. 扫描一遍diff数组，计算每个格子的覆盖次数，如果原本是0的格子覆盖次数仍然为0，说明这块空地怎么也无法被贴到，因此失败

class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        ### Step1
        prefix_sum = [[0]*(n+1) for _ in range(m+1)] # padding 
        # prefix_sum[i][j] means the total sum from (0, 0) to (i, j)
        for i in range(m):
            for j in range(n):
                prefix_sum[i+1][j+1] = prefix_sum[i][j+1]+prefix_sum[i+1][j]-prefix_sum[i][j]+grid[i][j]

        def get_sum(x1, y1, x2, y2):
            # given the prefix_sum, get the sum from (x1, y1) to (x2, y2)
            # (x1, y1), (x1, y2), (x2, y1), (x2, y2)
            # get the sum of the area from these four points
            return prefix_sum[x2+1][y2+1]-prefix_sum[x1][y2+1]-prefix_sum[x2+1][y1]+prefix_sum[x1][y1]

        ### Step2 
        # difference array
        diff = [[0]*(n+2) for _ in range(m+2)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    # (i, j)是左上的点，(x2, y2)是右下的点
                    x2, y2 = i+stampHeight-1, j+stampWidth-1
                    if x2<m and y2<n and get_sum(i, j, x2, y2)==0: # 这块区域全部都是0，可以贴邮票
                        diff[i+1][j+1]+=1 # 从(i, j)开始往右下的所有格子，覆盖次数都+1
                        diff[i+1][y2+2]-=1 
                        diff[x2+2][j+1]-=1
                        diff[x2+2][y2+2]+=1 # 右下角外面的区域多执行了一次-1的操作
        
        cnt = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                cnt[i][j] = cnt[i-1][j]+cnt[i][j-1]-cnt[i-1][j-1]+diff[i][j]

                if grid[i-1][j-1]==0 and cnt[i][j]==0:
                    return False
        return True

        