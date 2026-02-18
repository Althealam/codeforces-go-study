class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_cover = 0
        for i in range(len(nums)):
            max_cover = max(i+nums[i], max_cover)
            if max_cover>=len(nums)-1:
                return True
            if i==max_cover:
                return False
        return False