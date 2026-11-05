class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        hash_table = {}
        for word in words:
            if word not in hash_table:
                hash_table[word]=1
            else:
                hash_table[word]+=1
        min_heap = []
        for word, freq in hash_table.items():
            key = tuple(-ord(c) for c in word) # 转换为负的字符编码元组，实现逆字典序比较
            heapq.heappush(min_heap, (freq, key, word))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[2])
        return res[::-1]

        