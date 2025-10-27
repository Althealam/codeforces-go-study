class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        nums.sort() # -1, 1, 1, 2, 3 寻找对于-1合法的下标对
        count = 0
        while left<right:
            while left<right and nums[left]+nums[right]>=target:
                right-=1 # 移动right直到nums[left]+nums[right]已经小于target
            count+=right-left # left=0, right=3 (-1, 1), (-1, 1), (-1, 2)
            left+=1 # 继续判断下一个值的情况
        return count

        