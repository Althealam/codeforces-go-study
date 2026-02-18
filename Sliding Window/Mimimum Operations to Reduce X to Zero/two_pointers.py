# find a subarray with maximal length and its sum is sum(nums)-x (this subarray must be continuous)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target =sum(nums)-x # the sum of the subarray with maximal length is sum(nums)-x, and another subarray is x
        if target<0:
            return -1
        count = 0 # the sum of the subarray
        ans = float('-inf') # the maximal length of the valid subarray
        left, right = 0, 0 # two pointers
        while right<len(nums):
            count+=nums[right]
            while count>target:
                count-=nums[left]
                left+=1
            if count==target:
                ans = max(ans, right-left+1)
            right+=1
        return -1 if ans == float('-inf') else len(nums)-ans
