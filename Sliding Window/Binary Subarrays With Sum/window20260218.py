# number of subarrays with a sum goal = number of subarray satisfying its sum<=goal - number of subarray satisfying its sum<=goal-1
# [0, 0, 0, 0, 0]
# 1. left=right=0: [0]
# 2. left=0, right=1: [0, 0], [0]
# 3. left=0, right=2: [0, 0, 0], [0, 0], [0]
# 4. left=0, right=3: [0, 0, 0, 0], [0, 0, 0], [0, 0], [0]
# 5. left=0, right=4: [0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0], [0, 0], [0]
# 6. 
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # print(self.sum_at_most(nums, goal))
        # print(self.sum_at_most(nums, goal-1))
        return self.sum_at_most(nums, goal)-self.sum_at_most(nums, goal-1)
    
    def sum_at_most(self, nums, goal):
        left = 0
        count = 0
        sum_ = 0
        for right in range(len(nums)):
            sum_+=nums[right]
            # print(f'current_sum is {sum_}')
            while sum_>goal and left<=right:
                sum_-=nums[left]
                left+=1
                # print(f'current left is {left}')
                # print(f'update sum is {sum_}')
            # print(f'current left is {left}, current right is {right}')
            count+=right-left+1
        return count

nums = [0,0,0,0,0]
goal = 0
sol = Solution()
res = sol.numSubarraysWithSum(nums, goal)
print(res)