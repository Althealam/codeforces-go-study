class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf') # the minimal length of the subarray
        left, right = 0, 0
        sum_= 0 # the cumulative sum in the subarray
        while right<len(nums):
            sum_+=nums[right]
            while sum_>=target:
                ans = min(ans, right-left+1)
                sum_-=nums[left]
                left+=1
            right+=1
        return ans if ans!=float('inf') else 0
