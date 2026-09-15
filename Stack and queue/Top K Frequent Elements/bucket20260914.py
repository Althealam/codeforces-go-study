# 时间复杂度：O(n)
# 空间复杂度：O(n)
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

        # 2. 将出现次数相同的元素，放在同一个桶中
        buckets = [[] for _ in range(max_cnt+1)]
        for x, c in hash_map.items():
            buckets[c].append(x)
            # c是出现次数，x是元素值
        
        # 3. 倒序遍历buckets，将出现次数前面K大的元素加入答案
        ans = []
        for bucket in buckets[::-1]: # buckets[::-1]会复制一个新的表，因此空间复杂度为O(n)
            ans+=bucket
            if len(ans)==k:
                return ans