import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashtable = {} # space: O(m)
        for num in nums: # time: O(n)
            if num not in hashtable:
                hashtable[num]=1
            else:
                hashtable[num]+=1
        
        max_heap = [] # space: O(n)
        for num, freq in hashtable.items(): # time: O(m)
            heapq.heappush(max_heap, (-freq, num)) # time: O(logm)
        print(f"max heap is {max_heap}")

        res = [] # space: O(n)
        for _ in range(k): # time: O(k)
            neg_freq, num = heapq.heappop(max_heap) # time: O(logm)
            res.append(num)
        return res 

# total time: O(n+mlogm+klogm) k<=m<=n ==> O(n+mlogm)
# total space: O(m)
        
nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()
res = sol.topKFrequent(nums, k)
print(res)