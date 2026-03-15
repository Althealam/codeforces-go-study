# left[i]表示以nums[i]为结尾的最长等差连续子数组的长度
# right[i]表示以nums[i]为开头的最长等差连续子数组的长度
# 1. 求left[i]：如果nums[i]-nums[i-1]==nums[i-1]-nums[i-2]，说明nums[i-2], nums[i-1], nums[i]这三个数可以保持一个公差，因此可以将前面的等差段延长==>L[i] = L[i-1]+1，否则L[i] = 2（表示从最近的两个数开始）
# 2. 求right[i]：如果nums[i+1]-nums[i]==nums[i+2]-nums[i+1]，说明从i开始可以和右边保持一样的公差，因此R[i] = R[i+1]+1，否则R[i] = 2
# 3. 枚举所有的可以修改点i
# - 只往左边延长：L[i-1]+1
# - 只往右边延长：R[i+1]+1
# - 将左右两边拼接在一起：nums[i-1], new_val, nums[i+1]
# new_val = (nums[i-1]+nums[i+1])/2 ==> (nums[i+1]-nums[i-1])%2==0 此时的公差为d=(nums[i+1]-nums[i-1])//2

class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # L[i]: 以i为结尾的最长连续等差子数组的长度
        L = [1] * n
        L[1] = 2 # 表示第一个元素和第二个元素为一个等差子数组
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                L[i] = L[i - 1] + 1
            else:
                L[i] = 2

        # R[i]: 以i为开头的最长连续等差子数组的长度
        R = [1] * n
        R[n - 2] = 2 # 表示倒数第一个元素和倒数第二个元素为一个等差子数组
        for i in range(n - 3, -1, -1):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                R[i] = R[i + 1] + 1
            else:
                R[i] = 2

        ans = max(L)  # 不修改任何元素

        # 改第一个或最后一个元素
        ans = max(ans, R[1] + 1, L[n - 2] + 1)

        for i in range(1, n - 1): # 遍历所有的可修改点
            # 只接左边 / 只接右边
            ans = max(ans, L[i - 1] + 1)
            ans = max(ans, R[i + 1] + 1)

            # 尝试把左右拼起来时，必须要保证(nums[i+1]-nums[i-1])%2==0，因为我们需要公差是整数
            if (nums[i + 1] - nums[i - 1]) % 2 == 0:
                d = (nums[i + 1] - nums[i - 1]) // 2

                left_len = 1
                if i >= 2 and nums[i - 1] - nums[i - 2] == d:
                    left_len = L[i - 1]

                right_len = 1
                if i + 2 < n and nums[i + 2] - nums[i + 1] == d:
                    right_len = R[i + 1]

                ans = max(ans, left_len + 1 + right_len)

        return min(ans, n)