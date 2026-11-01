# nums = [2, 3, 1, 1, 4]
# max_range = [2, 4, 2, 2, 5]


class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0 # 跳跃次数
        cur_end = 0 # 当前的边界
        max_range = 0 # 能到达的最远范围
        for i in range(len(nums)-1):
            max_range = max(max_range, i+nums[i]) # 当前能覆盖的最远范围
            if i==cur_end: # 已经到达了目前的边界，则要跳一次
                jumps+=1
                cur_end = max_range
        return jumps 
