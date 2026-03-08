# stack = [100] ==> len(stack)
# update stack:
# 1. price = 100, stack = [(100, 1)]
# 2. price = 80, stack = [(100, 1), (80, 1)]
# 3. price = 60, stack = [(100, 1), (80, 1), (60, 1)]
# 4. price = 70, stack = [(100, 1), (80, 1), (70, 2)] (1+1)
# 5. price = 60, stack = [(100, 1), (80, 1), (70, 2), (60, 1)]
# 6. price = 75, stack = [(100, 1), (80, 1), (75, 4)]
# 7. price = 85, stack = [(100, 1), (85, 6)]

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while len(self.stack)!=0 and price>=self.stack[-1][0]:
            prev_price, prev_days = self.stack.pop()
            count+=prev_days
        self.stack.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)