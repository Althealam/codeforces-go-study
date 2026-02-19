# 1. 遇到偶数则变成0，奇数变成1
# 2. 通过前缀和寻找sum为k的连续子数组的数量
# prej-prei=k ==> prei=prej-k
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        pre = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for i in range(len(nums)):
            pre+=nums[i]
            ans+=cnt[pre-k]
            cnt[pre]+=1
        return ans
        