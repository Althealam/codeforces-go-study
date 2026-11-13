# (prefix_sum[j]-prefix_sum[i])%k==0
# prefix_sum[j]%k = prefix_sum[i]%k
# hash表中key存储的是pre[i]%k，而不是pre[i]
# hash表中value存储的是i
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix[i] = nums[0]
            else:
                prefix[i] = prefix[i-1]+nums[i]

        hash = {} 
        hash[0] = -1
        for i in range(len(prefix)):
            target = prefix[i]%k
            if target not in hash:
                hash[target] = i
            else:
                if i-hash[target]>=2:
                    return True
        return False
        