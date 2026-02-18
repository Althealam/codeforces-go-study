# [2, 1, 4, 3, 5]
# 1. 以2为右边界：left=0, right =0, 合法区间为[2]
# 2. 以1为右边界：left=0, right =1, 合法区间为[1], [2, 1] 数量为2
# 3. 以4为右边界：left=0, right =2，此时区间不合法，因此缩小left，拿到left=1, right=2, 合法区间为[1, 4], [4]
# 寻找以right为右边界的合法子区间的数量：right-left+1
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum_ = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            sum_+=nums[right] # update the sum of the subarray
            while sum_*(right-left+1)>=k: # remove left to find the maximum index for the subarray
                sum_-=nums[left]
                left+=1
            ans+=right-left+1
        return ans
