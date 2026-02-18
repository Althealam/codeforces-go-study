class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        current_end = 0
        max_end = 0
        for i in range(len(nums)-1):
            max_end = max(max_end, nums[i]+i)
            if i==current_end:
                step+=1
                current_end = max_end
        return step
            

