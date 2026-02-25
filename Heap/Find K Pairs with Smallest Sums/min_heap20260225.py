# 1. nums1[0]+nums2[0] is the pair with the smallest sums
# 2. nums1[i]+nums2[0] and nums1[0]+nums2[j] should be the next pair with the smallest sums
# suppose nums1[i]+nums2[j] is the pair with the smallest sums, then the next pair should be nums1[i+1]+nums2[j] or nums1[i]+nums2[j+1]

# example: nums1=[1, 7, 11] num2=[2, 4, 6]
# [1+2, 7+2, 11+2] start with nums2[0]
# [1+4, 7+4, 11+6] start with nums2[1]
# [1+6, 7+6, 11+6] start with nums2[2]
# [3, 9, 13]
# [5, 11, 17]
# [7, 13, 17]

# time: O(klog(min(n, k)))
# space: O(min(n, k))

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        min_heap = []

        # initialize the min heap O(min(n, k)*log(min(n, k)))
        for i in range(min(len(nums1), k)): # time: O(min(n, k))
            current_sum = nums1[i]+nums2[0]
            heapq.heappush(min_heap, (current_sum, i, 0)) # time: O(log(min(n, k)))
        
        # put the minimal sum into res 
        # total time: O(klog(min(n, k)))
        while min_heap and len(res)<k: # time: O(k)
            current_sum, i, j = heapq.heappop(min_heap) # get the minimal from the heap 
            # time: O(log(min(n, k)))
            res.append([nums1[i], nums2[j]])

            # put the other into min_heap
            # 对于(nums1[i], nums2[j])，下一个最小和的pair只会出现在(nums1[i], nums2[j+1])和(nums1[i+1], nums2[j])
            if j+1<len(nums2):
                # time: O(log(min(n, k)))
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
        
        return res
        