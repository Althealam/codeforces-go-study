class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.min_heap = [x for x in self.nums]
        heapify(self.min_heap)

        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap, val)
        
        elif val>self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        
        return self.min_heap[0]