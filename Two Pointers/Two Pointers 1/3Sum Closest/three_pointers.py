class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0 # answer
        diff = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                sum_ = nums[i]+nums[left]+nums[right]
                if sum_==target:
                    return sum_
                # 更新答案值
                if abs(sum_-target)<diff:
                    diff = abs(sum_-target)
                    res = sum_
                if sum_>target:
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                if sum_<target:
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res

                