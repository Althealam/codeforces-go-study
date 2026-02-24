class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {} # space: O(m)
        for num in nums: # time: O(n) 
            hashtable[num] = hashtable.get(num, 0)+1
        
        min_heap = [] # 小顶堆，存入前面K个高频元素的频率和元素值
        for num, freq in hashtable.items(): # time: O(m)
            if len(min_heap)<k:
                # time: O(logk)
                heapq.heappush(min_heap, (freq, num)) # 频率为正，小顶堆
            elif freq>min_heap[0][0]: # 当前遍历的元素的出现频率大于堆顶元素
                heapq.heappop(min_heap)
                # time: O(logk)
                heapq.heappush(min_heap, (freq, num))
        
        return [num for freq, num in min_heap]

# total time: O(n+mlogk)
# total space: O(m)