class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        gain = [0]*(len(prices)-1)
        for i in range(len(prices)-1):
            gain[i] = prices[i+1]-prices[i]
        return sum(x for x in gain if x>0)