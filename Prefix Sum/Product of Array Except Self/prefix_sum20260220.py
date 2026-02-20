# pre[i] = num[0]*nums[1]*...*nums[i-2]
# [1, 2, 3, 4] ==> [1, 1, 1*2, 1*2*3]
# suf[i] = nums[i+1]*...*nums[n-1]
# [1, 2, 3, 4] ==> [2*3*4, 3*4, 4, 1]

# ans[i] = nums[0]*nums[1]*...*nums[i-2]*nums[i]*..*nums[n-1]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        sur = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            # print('========')
            # print(f'current i is {i}')
            # print(f'current num is {nums[i+1]}')
            # print(f'previous sur is {sur[i+1]}')
            sur[i] = sur[i+1]*nums[i+1]
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = sur[i]*pre[i]
        return ans
        

nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))