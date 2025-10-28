# 有效三角形：两边之和大于第三边
# 判断方法：对于nums中的每个值，找到符合nums[left]+nums[right]>val的[left, right]组合数即可
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0 # the answer
        for i in range(2, len(nums)):
            left = 0
            right = i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]: # [left, right] is a valid edge for nums[i]
                    count+=right-left
                    right-=1
                else: # [nums[left], nums[right], nums[i]] is not valid
                    left+=1 # remove the left to improve nums[left]+nums[right]
        return count

    