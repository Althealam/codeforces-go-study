class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        history = {}
        has_cycle = False

        for day in range(n): # 现在的问题在于n可能很大
            state_key = tuple(cells)
            if state_key in history: # 遇到了循环
                has_cycle = True
                prev_day = history[state_key] # 遇到相同状态的上一个天数
                cycle_len = day-prev_day # the length of cycle
                remaining_day = (n-day)%cycle_len  # [1, 2, 3, 1, 2, 3] n=5 day=3 cycle=3-0=3 (5-3)%3=2 have 2 days left
                return self.prisonAfterNDays(cells, remaining_day)
            
            # 没遇到循环
            history[state_key] = day
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