class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap
        max_heap = [] 
        # 不断的优化大顶堆，直到大顶堆中存储的是前面K个最小元素
        for x, y in points: 
            dist = -(x**2+y**2)
            if len(max_heap)<k:
                heapq.heappush(max_heap, (dist, [x, y])) 
            elif dist>max_heap[0][0]: # dist>max_heap[0][0]==> dist<-max_heap[0][0] 也就是当前元素比堆顶元素要小
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (dist, [x, y]))
        
        # 不断的弹出大顶堆的元素即可
        return [y for x, y in max_heap]
        