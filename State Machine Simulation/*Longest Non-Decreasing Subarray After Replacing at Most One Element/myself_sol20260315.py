# 1. left是以i为结尾的左边的连续非递减子序列的长度，right是以i为开头的右边的连续非递减连续子序列的长度，对于每个i获取left和right
# 2. 如果nums[i-1]<=nums[i+1]，那么将nums[i]取为这两个数中间的数即可：ans = max(ans, right[i-1]+left[i+1]+1)
# 3. 如果nums[i-1]>nums[i+1]，那么可以将nums[i]和左边的部分拼接在一起（left[i-1]+1）或者和右边的部分拼接在一起（right[i+1]+1）
class Solution:
    def longestSubarray(self, nums) -> int:
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i-1]<=nums[i]:
                left[i] = left[i-1]+1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<=nums[i+1]:
                right[i] = right[i+1]+1
        print(left)
        print(right)
        ans = 0
        for i in range(1, len(nums)-1):
            if nums[i-1]<=nums[i+1]:
                ans = max(ans, right[i+1]+left[i-1]+1)
            elif nums[i-1]>nums[i+1]:
                ans = max(ans, right[i+1]+1, left[i-1]+1)
            elif i==0:
                ans = max(ans, right[1]+1)
            elif i==len(nums)-1:
                ans = max(ans, left[len(nums)-2]+1)
        return ans
        
sol = Solution()
nums = [1, 2, 3, 1, 2]
res = sol.longestSubarray(nums)
print(res)