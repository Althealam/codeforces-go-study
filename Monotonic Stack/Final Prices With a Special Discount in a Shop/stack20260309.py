
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        next_smaller = [len(prices)]*len(prices)
        stack = []
        for i in range(len(prices)):
            while len(stack)!=0 and prices[i]<=prices[stack[-1]]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        ans = [0]*len(prices)
        for i in range(len(prices)):
            if next_smaller[i]!=len(prices):
                ans[i] = prices[i]-prices[next_smaller[i]]
            else:
                ans[i] = prices[i]
        return ans
                
        