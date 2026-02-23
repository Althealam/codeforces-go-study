class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val) # add a new test score into self.nums
        max_heap = [-x for x in self.nums]
        heapq.heapify(max_heap) # O(n)
        res = 0
        for _ in range(self.k):
            res = heapq.heappop(max_heap)
        return -res

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)