# 前缀和+哈希表
# 思路：将0转换为-1，寻找0和1数量相等的最长子数组，即寻找和为0的连续子数组
# prefix_j-prefix_i = 0 ==> prefix_j == prefix_i and j-i is maximal 
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
        max_length = 0
        for i in range(len(nums)):
            current_prefix = prefix_sum[i]
            target_prefix = current_prefix
            if target_prefix in cnt:
                max_length = max(max_length, i-cnt[target_prefix])
            if current_prefix not in cnt:
                cnt[current_prefix] = i
        return max_length
        
