class Solution:
    def longestSubarray(self, nums):
        n = len(nums)

        left = [0]*n
        right = [0]*n

        for i in range(n):
            if nums[i]==1:
                left[i] = (left[i-1] if i>0 else 0)+1

        for i in range(n-1,-1,-1):
            if nums[i]==1:
                right[i] = (right[i+1] if i<n-1 else 0)+1

        ans = 0

        for i in range(n):
            l = left[i-1] if i>0 else 0
            r = right[i+1] if i<n-1 else 0
            ans = max(ans, l+r)

        return min(ans,n-1)