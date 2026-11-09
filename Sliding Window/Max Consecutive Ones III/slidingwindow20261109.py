# 思路：找到最长的连续子数组，其中0的数量小于等于K，剩下的则全部为1 
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        count_zero = 0
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right]==0:
                count_zero+=1
            while count_zero>k:
                if nums[left]==0:
                    count_zero-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len
        