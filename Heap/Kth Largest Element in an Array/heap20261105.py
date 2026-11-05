class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] # space: O(k)
        heapq.heapify(min_heap) # time: O(k)  space: O(1)
        for i in range(k, len(nums)): # time: O(n-k)
            if nums[i]>min_heap[0]: # 当前的元素大于堆顶元素，则将堆顶元素推出去，说明这个元素肯定不属于前面K个最大的雨严肃
                heapq.heappop(min_heap) # time: O(logk)
                heapq.heappush(min_heap, nums[i]) # time: O(logk)
        return min_heap[0]

# time: O(k+(n-k)logk) = O(nlogk)
# space: O(k)