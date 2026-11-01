class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_range = 0
        cur_range = 0
        for i in range(len(nums)):
            cur_range = i+nums[i]
            max_range = max(max_range, cur_range)
            if max_range>=len(nums)-1: # 到达最后一个下标就成功
                return True
            if i>=max_range:
                return False
        return False