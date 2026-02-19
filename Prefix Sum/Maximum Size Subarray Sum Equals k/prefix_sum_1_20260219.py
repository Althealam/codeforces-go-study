# 由于nums中有负数，因此不可以使用滑动窗口
# 滑动窗口的使用情况是窗口内的指标是单调变化的，比如全部都是正数或者全部都是负数
# 如果遇到需要求解连续子数组，并且数组内有负数的，考虑使用前缀和

# prefix_j-prefix_i==k ==> prefix_i = prefix_j-k ==> j-i is max
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix_sum[i]=nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1]+nums[i]
        
        ans = 0
        cnt = defaultdict() # store the initial index for prefix_sum
        cnt[0] = -1
        for i in range(len(prefix_sum)):
            current_prefix = prefix_sum[i]
            target_prefix = current_prefix-k
            if target_prefix in cnt:
                ans = max(ans, i-cnt[target_prefix])
            if current_prefix not in cnt:
                cnt[current_prefix] = i
        return ans

        

        