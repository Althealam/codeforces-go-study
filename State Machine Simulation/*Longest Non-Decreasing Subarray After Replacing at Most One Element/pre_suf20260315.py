class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        right = [1]*len(nums)
        left = [1]*len(nums)

        # right[i]是以i开始的最长non-decreasing subarray长度
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<=nums[i+1]:
                right[i] = right[i+1]+1

        # left[i]是以i结尾的最长non-decreasing subarray长度
        for i in range(1, len(nums)):
            if nums[i]>=nums[i-1]:
                left[i] = left[i-1]+1
        
        ans = max(left) # 不做修改
        for i in range(len(nums)):
            # 修改中间
            if 0<i<len(nums)-1: # 因为i-1>0, i+1<len(nums)-1
                if nums[i-1]<=nums[i+1]: # 直接修改中间的元素
                    ans = max(ans, left[i-1]+1+right[i+1])
                else: # 将中间的元素和前面或者后面的元素拼接在一起
                    ans = max(ans, left[i-1]+1, right[i+1]+1)
            # 修改第一个
            elif i==0:
                ans = max(ans, 1+right[1])
            # 修改最后一个
            else:
                ans = max(ans, left[len(nums)-2]+1)
        return ans
