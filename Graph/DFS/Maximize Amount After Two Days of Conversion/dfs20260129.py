from typing import Any


from collections import defaultdict
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1, rates1, pairs2, rates2) -> float:
        grid1 = defaultdict(list)
        grid2 = defaultdict(list)

        for (country1, country2), rate in zip(pairs1, rates1):
            grid1[country1].append((country2, rate))
            grid1[country2].append((country1, 1/rate))
        
        for (country1, country2), rate in zip(pairs2, rates2):
            grid2[country1].append((country2, rate))
            grid2[country2].append((country1, 1/rate))

        def dfs(i, current_amount, amount_day, grid):
            amount_day[i] = current_amount
            for next_country, rate in grid[i]:
                if next_country not in amount_day:
                    # print("The next country:", next_country)
                    dfs(next_country, current_amount*rate, amount_day, grid)

        # 1. 获得从initial_currency出发时可以得到的最多货币值
        # print("====day1====")
        amount_day1 = {}
        current_amount = 1
        dfs(initialCurrency, current_amount, amount_day1, grid1)
        # print("amount_day_1:", amount_day1)
        # 2. 获得从amount_day1中的不同国家出发时回到initialCurrency的最大金额
        # print('====day2====')
        max_amount = 1
        for i in amount_day1.keys(): # 遍历从amount_day1出发的各个国家
            # print("Current country:", i)
            amount_day2 = {}
            dfs(i, amount_day1[i], amount_day2, grid2)
            # print("The max amount:", amount_day2)
            if initialCurrency in amount_day2.keys():
                max_amount = max(max_amount, amount_day2[initialCurrency])
        return max_amount

initialCurrency = "USD"
pairs1 = [["USD","EUR"]]
rates1 = [1.0]
pairs2 = [["EUR","JPY"]]
rates2 = [10.0]


solution = Solution()
ans = solution.maxAmount(initialCurrency, pairs1, rates1, pairs2, rates2)
print(ans)