# coung(max<=right)-count(max<left)

from collections import deque
class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        return self.count(nums, right)-self.count(nums, left-1)

    def count(self, nums, bound):
        ans = 0
        cur = 0
        for x in nums:
            if x<=bound:
                cur+=1 # window length: it identifies the number of subarray which satisfies that the maximal value<=bound
                # cur=2: [2, 5] [5] and [2, 5] both satisfies
            else:
                cur = 0
            ans+=cur
        return ans

nums = [2, 9, 2, 5, 6]
left = 2
right = 8
sol = Solution()
print(sol.numSubarrayBoundedMax(nums, left, right))