# pre[i] = nums[0]*nums[1]*...*nums[i-1] nums[i]左边所有元素的乘积
# -> pre[i] = pre[i-1] * nums[i-1]
# pre[0] = 1
# pre[1] = nums[0]
# pre[2] = nums[0] * nums[1]

# suf[i] = nums[n-1]*nums[n-2]*...*nums[i] nums[i]右边所有元素的乘积
# -> suf[i] = suf[i+1] * nums[i+1]
# suf[n-1] = 1
# suf[n-2] = nums[n-1]
# suf[n-3] = nums[n-1] * nums[n-2]

# answer[i] = pre[i]*suf[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        suf = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = pre[i]*suf[i]
        return ans
        