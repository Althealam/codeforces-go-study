from collections import defaultdict
from sys import prefix
# prei-prej=goal ==> prei=prej+goal
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1]+nums[i]
        
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1 # 这个一定要cnt[0] = 1，表示前缀和为0，否则所有从下标0开始的子数组都会被漏掉
        # 当子数组为[0..j]的时候，其前缀和为prefix_sum[j]，那么如果我们不记录cnt[0]=1的话，会导致求cnt[prefix_sum[j]-goal]的时候找不到cnt[0]
        # 比如如果是[1, 1] target=2 
        # prefix_sum[0..1]=2, cnt[prefix_sum[0..1]-target]=cnt[0]=1才可以
        for prefix in prefix_sum:
            ans+=cnt[prefix-goal]
            cnt[prefix]+=1
        return ans
        # pre = 0
        # ans = 0
        # cnt = defaultdict(int)
        # cnt[0]=1 # 存储一个前缀和为0的元素
        # for num in nums:
        #     print(f"Current num is {num}")
        #     pre+=num
        #     print(f"Update sum is {cnt[pre-goal]}")
        #     ans+=cnt[pre-goal]
        #     cnt[pre]+=1
        # return ans

nums = [1, 0, 1, 0, 1]
goal = 2
sol = Solution()
res = sol.numSubarraysWithSum(nums, goal)
print(res)