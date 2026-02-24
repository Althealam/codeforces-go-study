class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {} # space: O(m)
        for word in words: # time: O(n)
            count[word] = count.get(word, 0)+1
        
        # time: O(m)
        # space: O(m)
        heap = [(-freq, word) for word, freq in count.items()] 
        # the more the frequence (freq large, -freq small), then its rank will be smaller
        # the smaller the character is, then its rank should be smaller 
        heapq.heapify(heap) # time: O(logm)

        res = [] # space: O(k)
        for _ in range(k): # time: O(k)
            freq, word = heapq.heappop(heap) # time: O(logm)
            res.append(word) 
        return res

# total time: O(n+m+logm+klogm)=(n+m+klogm)
# total space: O(m+m+k)=O(m)
# k<=m<=n

            