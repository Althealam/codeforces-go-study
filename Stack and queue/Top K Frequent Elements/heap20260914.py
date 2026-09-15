# 时间复杂度：O(n+mlogm+klogm)
# 空间复杂度：O(m+k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 定义哈希表，存储每个元素的出现次数
        hash_map = collections.defaultdict(int)
        for num in nums:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        max_cnt = max(hash_map.values()) # 最大的出现次数

        # 2. 使用最大堆
        max_heap = [] # 将m个不同元素推入堆中每次的时间复杂度为O(logm)，总共的时间复杂度为O(mlogm)
        for num, freq in hash_map.items():
            heapq.heappush(max_heap, (-freq, num))
        
        res = []
        for _ in range(k): # 弹出k次的时间复杂度为O(klogm)
            neg_freq, num = heapq.heappop(max_heap)
            res.append(num)
        return res