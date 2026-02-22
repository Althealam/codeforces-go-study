# 1. iterate all the node with value 0 in the grid, and identify whether can we put a stamp on the point (i, j) (let the point (i, j) be the left and top point of the stamp)
# left top: (i, j)
# right top: (i+stampWidth-1, j)
# left bottom: (i, j+stampHeight-1)
# right bottom: (i+stampWidth-1, j+stampHeight-1)
# Check whether the values in this grid are all 0 ==> if true, then we can put a stamp here
# 2. after get all the available points, we can identify whether all points with value 0 have beed fulfilled with stamp. If yes then return true

class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        available_points = []
        for i in range(m):
            for j in range(n):
                if self.check_availability(grid, i, j, stampHeight, stampWidth):
                    available_points.append((i, j)) 

        # 0 -> 0+4-1=3
        # 1 -> 1+3-1=3
        for point in available_points:
            # print(f'current point is {point}')
            x, y = point[0], point[1]
            for i in range(x, x+stampHeight):
                for j in range(y, y+stampWidth):
                    # print(f'iterate {i} {j}')
                    if grid[i][j]==0:
                        grid[i][j] = 1
            # print(f"current grid is {grid}")
        
        # print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    return False

        return True


    def check_availability(self, grid, x, y, stampHeight, stampWidth):
        if x+stampHeight-1>=len(grid) or y+stampWidth-1>=len(grid[0]):
            return False
        
        for i in range(x, x+stampHeight):
            for j in range(y, y+stampWidth):
                if grid[i][j]!=0:
                    return False
        return True
        

grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
stampHeight = 4
stampWidth = 3
sol = Solution()
res = sol.possibleToStamp(grid, stampHeight, stampWidth)
print(res)