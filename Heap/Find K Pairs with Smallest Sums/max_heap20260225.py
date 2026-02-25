class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(min(len(nums1), k)): # time: O(min(len(nums1), k)
            for j in range(min(len(nums2), k)): # time: O(min(len(nums2), k)
                current_sum = nums1[i]+nums2[j]

                if len(max_heap)<k: # time: O(logk)
                    heapq.heappush(max_heap, (-current_sum, [nums1[i], nums2[j]]))
                elif current_sum<-max_heap[0][0]:
                    heapq.heappop(max_heap) # time: O(logk)
                    heapq.heappush(max_heap, (-current_sum, [nums1[i], nums2[j]]))
                else:
                    break
        return [pair for val, pair in max_heap]