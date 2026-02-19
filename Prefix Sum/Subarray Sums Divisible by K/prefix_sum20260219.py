# prej-prei=num ==> num%k==0 ==> prej%k=prei%k
# find the number of subarray [i..j]
# iterate i, and find the j with same mod (pre%k)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = 0
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for i in range(len(nums)): # iterate the right side j
            pre+=nums[i]
            mod = pre%k
            ans+=cnt[mod]
            cnt[mod]+=1
        return ans


