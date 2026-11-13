# 1. change all the zeros into negative ones
# 2. find the contiguous subarray with sum equals to zero and with maximal length
# pre[j] - pre[i] == 0 -> pre[j] = pre[i]

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = -1
        
        pre = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1]+nums[i]
        # pre = [0, 1] -> pre=[-1, 0]
        max_len = 0
        hash = {}
        hash[0] = -1
        for i in range(len(pre)):
            if pre[i] not in hash:
                hash[pre[i]] = i
            else:
                max_len = max(max_len, i-hash[pre[i]])
        
        return max_len
        