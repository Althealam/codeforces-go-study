# 1. if num=0 then transform it into -1
# 2. prefix_j-prefix_i = 0 ==> prefix_j == prefix_i and j-i is maximal
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = -1
        
        prefix_sum = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix_sum[0] = nums[0]
            else:
                prefix_sum[i] = prefix_sum[i-1]+nums[i]
        
        cnt = {} # record the earlest index for prefix sum
        cnt[0] = -1
        ans = 0 # record the maximal length of the contiguous subarray
        for i in range(len(nums)):
            current_prefix = prefix_sum[i]
            target_prefix = current_prefix
            if target_prefix in cnt:
                ans = max(ans, i-cnt[target_prefix])
            if current_prefix not in cnt:
                cnt[current_prefix] = i
        return ans        
        