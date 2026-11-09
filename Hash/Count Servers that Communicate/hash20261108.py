# 思路：
# 第一次遍历，如果grid[i][j]等于1，说明(i, j)有一台服务器 -> 更新row和col的i和j分别加1
# 第二次遍历，根据row和col来判断每一台服务器是否能和至少其他一台服务通信，如果grid[i][j]=1并且row[i]和col[j]中至少一个严格大于1，说明(i, j)的服务器能和同一行或者同一列的另外一台服务器通信，答案加1
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row = {}
        col = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if i in row:
                        row[i]+=1
                    else:
                        row[i] = 1
                    if j in col:
                        col[j]+=1
                    else:
                        col[j]=1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (row.get(i,0) >1 or col.get(j, 0)>1):
                    ans+=1
        return ans