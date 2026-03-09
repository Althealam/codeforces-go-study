# max(nums[i]*sum_)
# [1, 2, 3, 2]
# 1. nums[i]=1, subarray = [1, 2, 3, 2]
# 2. nums[i]=2(i=1), subarray = [2, 3]

# iterate nums[i]
# left, right of the subarray
# - previous_smaller
# - next_smaller
# subarray: [previous_smaller+1, next_smaller-1]

# max(nums[i]*sum_[previous_smaller+1, next_smaller-1])

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        previous_smaller = [-1]*len(nums)
        next_smaller = [len(nums)]*len(nums)

        # find the next smaller
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]<nums[stack[-1]]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        # find the previous smaller
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]<nums[stack[-1]]:
                stack.pop()
            previous_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        
        sum_ = [0]*len(nums)
        # [1, 2, 3, 2] ==> [0, 1, 3, 6, 8]
        for i in range(len(nums)):
            if i==0:
                sum_[0] = nums[0]
            else:
                sum_[i] = sum_[i-1]+nums[i]
        max_val = float('-inf')
        for i in range(len(nums)):
            left = previous_smaller[i]+1
            right = next_smaller[i]-1
            if left==0:
                sub_sum = sum_[right]
            else:
                sub_sum = sum_[right]-sum_[left-1]
            max_val = max(max_val,nums[i]*sub_sum)
        return max_val%(10**9+7)

        