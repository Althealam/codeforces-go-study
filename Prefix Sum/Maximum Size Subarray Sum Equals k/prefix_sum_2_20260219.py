# 由于nums中有负数，因此不可以使用滑动窗口
# 滑动窗口的使用情况是窗口内的指标是单调变化的，比如全部都是正数或者全部都是负数
# 如果遇到需要求解连续子数组，并且数组内有负数的，考虑使用前缀和

# prefix_j-prefix_i==k ==> prefix_i = prefix_j-k ==> j-i is max
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre = 0
        cnt = {}
        cnt[0] = -1
        ans = 0
        for i in range(len(nums)):
            pre+=nums[i]
            target = pre-k
            if target in cnt:
                ans = max(ans, i-cnt[target])
            if pre not in cnt:
                cnt[pre] = i
        return ans

