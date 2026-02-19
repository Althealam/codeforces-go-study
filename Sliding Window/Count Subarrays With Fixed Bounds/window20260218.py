# 对于每个right=i，子数组必须不包含非法元素，并且至少包含一个minK，以及包含一个maxK
# 因此最早的起点是last_invalid+1 最晚的起点是min(last_min, last_max)
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        last_invalid = -1 # 最近一个非法严肃
        last_min = -1 # 最近一个min出现的位置
        last_max = -1 # 最近一个max出现的位置

        ans = 0
        for i, num in enumerate(nums):
            if num<minK or num>maxK:
                last_invalid = i
            
            if num==minK:
                last_min=i
            if num==maxK:
                last_max=i

            valid_count = min(last_min, last_max)-last_invalid
            if valid_count>0:
                ans+=valid_count
        return ans