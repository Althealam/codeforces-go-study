# sliding window:
# [1, 2, 1, 2, 3]
# 1. l=r=0 subarray=[1]
# 2. l=0, r=1 subarray=[1, 2]: count+=1
# 3. l=0, r=2 subarray=[1, 2, 1]: count+=1
# 4. l=0, r=3 subarray=[1, 2, 1, 2]: count+=1
# 5. l=0, r=4 subarray=[1, 2, 1, 2, 3]
# if use sliding window, we will pass the [2, 1] subarray

# use two pointers:
# 1. l=r=0 subarray=[1]
# 2. l=0, r=1 subarray=[1, 2]: count+=1
# 3. l=0, r=2 subarray=[1, 2, 1]: we could get the [1, 2, 1] and [2, 1] both satisfy the requirement count+=2
# 4. l=0, r=3 subarray=[1, 2, 1, 2]: we could get the [1, 2], [2, 1, 2] and [1, 2, 1, 2] all satisfy count+=3
# 5. l=0, r=4 subarray=[1, 2, 1, 2, 3]
# 6. l=1, r=4 subarray=[2, 1, 2, 3]
# 7. l=2, r=4 subarray=[1, 2, 3]
# 8. l=3, r=4 subarray=[2, 3] count+=1

# [1, 2, 1, 3, 4] k =3
# 1. l=r=0 subarray=[1]
# 2. l=0 r=1 subarray=[1, 2]
# 3. l=0 r=2 subarray=[1,2,1]
# 4. l=0 r=3 subarray=[1,2,1,3] count+=2 which means that [1,2,1,3] and [2,1,3] both satisfy
# right-left=3 k=3 
# 5. l=0 r=4 subarray=[1,2,1,3,4] 
# 6. l=1 r=4 subarray=[2,1,3,4] 
# 7. l=2 r=4 subarray=[1,3,4] count+=1
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k):
            left = 0
            res = 0 
            counter = defaultdict(int)
            for right in range(len(nums)):
                counter[nums[right]]+=1
                while len(counter)>k:
                    counter[nums[left]]-=1
                    if counter[nums[left]]==0:
                        del counter[nums[left]]
                    left+=1
                res+=right-left+1
            return res
        return atMost(k)-atMost(k-1)


nums = [2, 2, 1, 2, 2, 2, 1, 1]
k = 2
sol = Solution()
print(sol.subarraysWithKDistinct(nums, k))