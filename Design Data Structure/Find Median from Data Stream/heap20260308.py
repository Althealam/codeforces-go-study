# self.nums = []
# self.heap1 = [](max_heap), self.heap2 = [](min_heap)
# 1. arr = [2, 3, 4] ==> self.heap1 = [2], self.heap2 = [3, 4]
# 2. arr = [2, 3] ==> self.heap1 = [2], self.heap2 = [3]

# - len(nums)%2==0: 
# - return -first = heapq.heappop(self.heap1), heapq.heappush(first)
# - second = heapq.heappop(self.heap2), heapq.heappush(second)
# - len(nums)%2!=0: return heapq.heappop(self.heap2)

# 1. addNum
# object: abs(len(self.heap1)-len(self.heap2))<=1
# example:
# self.heap1=[2], self.heap2=[3], num=4 ==> self.heap1=[-3, -2], self.heap2=[4]
# - if len(self.heap1)==0 and len(self.heap2)==0: heapq.heappush(self.heap1, -num)

# 2. findMedian: get the element from heap1 and heap2 by len(nums)
class MedianFinder:

    def __init__(self):
        self.large = [] # 小顶堆，保存较大的一半
        self.small = [] # 大顶堆，保存较小的一半
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large)>len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # 元素不一样多，多的那个堆的堆顶就是中位数
        if len(self.large)<len(self.small):
            return -self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (self.large[0]-self.small[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()