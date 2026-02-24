class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap
        heap = []
        for x, y in points:
            distance = x**2+y**2
            # push the tuple into heap, like (distance, [x, y])
            heapq.heappush(heap, (distance, [x, y]))
        
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res