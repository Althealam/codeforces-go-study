class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float('inf')
        left = 0
        sum_ = 0
        for right in range(len(nums)):
            sum_+=nums[right]
            while sum_>=target:
                ans = min(ans, right-left+1)
                sum_-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0