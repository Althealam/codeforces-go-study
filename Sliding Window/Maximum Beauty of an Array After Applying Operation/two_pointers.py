# 找到一个整数x，使得数组中有最多的元素能通过修改变成x==>找到若干闭区间，这些闭区间的交集不为空
# [4, 6, 1, 2] 
# [1, 2, 4, 6]
# [-1, 3], [0, 4], [2, 6], [4, 8]
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        nums.sort()
        for right in range(len(nums)): # [nums[left]-k, nums[left]+k], [nums[right]-k, nums[right]+k]
            # nums[right]-k<=nums[left]+k==>nums[right]-nums[left]<=2*k
            while nums[right]-nums[left]>2*k:
                left+=1
            ans = max(ans, right-left+1)
        return ans

