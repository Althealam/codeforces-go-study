class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target_sum = sum(nums)-x
        if target_sum<0:
            return -1
        if target_sum==0:
            return len(nums)
        cur_sum = 0
        left = 0
        ans = float('inf')
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while cur_sum>target_sum:
                cur_sum-=nums[left]
                left+=1
            if cur_sum==target_sum:
                cur_length = right-left+1
                ans = min(ans, len(nums)-cur_length)
        return -1 if ans==float('inf') else ans