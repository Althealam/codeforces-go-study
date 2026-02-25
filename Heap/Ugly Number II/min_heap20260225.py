class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # [1, 1*2, 2*2, 3*2, ..., n*2]
        # [1, 1*3, 2*3, 3*3, ..., n*3]
        # [1, 1*5, 2*5, 3*5, ..., n*5]
        res = [1]
        min_heap = []
        factors = [2, 3, 5]
        
        for i in range(len(factors)):
            heapq.heappush(min_heap, (factors[i]*res[0], i, 0))
        
        while len(res)<n:
            val, i, j = heapq.heappop(min_heap)
            if val>res[-1]: # 用于去重
                res.append(val)
            heapq.heappush(min_heap, (factors[i]*res[j+1], i, j+1))
        return res[-1]