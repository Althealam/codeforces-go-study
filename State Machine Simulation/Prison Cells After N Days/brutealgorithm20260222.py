class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        for day in range(n): # 现在的问题在于n可能很大
            new_cells = [0]*8
            for i in range(1, 7):
                if cells[i-1]==cells[i+1]:
                    new_cells[i] = 1
                else:
                    new_cells[i] = 0
            cells = new_cells
        
        return cells

cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 7
sol = Solution()
res = sol.prisonAfterNDays(cells, n)
print(res)