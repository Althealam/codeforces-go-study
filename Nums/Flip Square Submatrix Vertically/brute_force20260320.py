class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # top left: (x, y)
        # top right: (x+k, y)
        # bottom left: (x+k, y)
        # bottom right: (x+k, y+k)

        # flip: (x, y)->(x+k, y) <=> (x+k, y)->(x+k, y+k)
        m, n = len(grid), len(grid[0])
        top, bottom = x, x+k-1
        while top<bottom:
            for j in range(k):
                grid[top][y+j], grid[bottom][y+j] = grid[bottom][y+j], grid[top][y+j]
            top+=1
            bottom-=1
        return grid
