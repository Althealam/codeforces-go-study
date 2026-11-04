import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num]+=1
        
        min_heap = [] # 小顶堆
        for num, freq in hash_table.items():  # O(m)
            if len(min_heap)<k: # O(logk)
                heapq.heappush(min_heap, (freq, num))
            elif freq>min_heap[0][0]: # 当前遍历的元素的出现频率大于当前的堆顶元素
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))
        
        return [num for freq, num in min_heap]
# 时间复杂度：O(mlogk) 
# 空间复杂度：
# - hash_table: O(m)
# - min_heap: O(k)
# - return: O(k) 