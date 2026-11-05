class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k
        self.min_heap = [x for x in self.nums] # time: O(n)
        heapq.heapify(self.min_heap)  # time: O(n)
        while len(self.min_heap)>k: # time: O(n-k)
            heapq.heappop(self.min_heap)  # time: O(logn)

    def add(self, val: int) -> int:    
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap, val) # O(logk)

        elif val>self.min_heap[0]:
            # time: O(logk)
            heapq.heappop(self.min_heap) # 弹出堆顶元素，此时的堆顶元素不属于前k个最大元素
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]  

# time: O(n+(n-k)logn) + O(logk)
