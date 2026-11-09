# 思路：题目要求统计所有乘积严格小于k的连续子数组 -> 滑动窗口
# nums中的元素都是正整数，因此当指针向右移动时，窗口乘积只会增大或者保持不变，左指针向右移动时，窗口乘积只会减小或者保持不变

# 需要累加right-left+1而不是+1
# 当[left, right]的乘积小于k时，[left+1, right], [left+2, right]...都是符合要求的
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        ans = 0
        cur = 1
        left = 0
        for right in range(len(nums)):
            cur*=nums[right]
            while cur>=k:
                cur//=nums[left]
                left+=1
            ans+=right-left+1
        return ans