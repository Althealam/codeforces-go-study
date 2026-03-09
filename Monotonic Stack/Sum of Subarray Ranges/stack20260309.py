# sum(largest-smallest) = sum(largest)-sum(smallest)

# example: 
# element = 1 
# largest = [1] 
# smallest = [1], [1, 2], [1, 2, 3]

# element = 2
# largest = [2], [1, 2]
# smallest = [2], [2, 3]

# 3, 2, 3, 2, 4, 5 ==> [2], k = 3, left = 2, right = 4 ==> [left+1, k] is valid interval, and [k, right-1] is valid interval ==> (k-left)*(right-k)

# 3, 2, 3, 2, 4, 5 ==> [2], k = 3, left = 1, right = None ==> [left+1, k] is valid interval, and [k, right] is valid interval ==> (k-left)*(right-k)

# sum(ranges) = nums[i]*(k-left_max)*(right_max-k) - nums[i]*(k-left_min)*(right_min-k)


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        pre_smaller = [-1]*len(nums)
        pre_larger = [-1]*len(nums)
        nxt_smaller = [len(nums)]*len(nums)
        nxt_larger = [len(nums)]*len(nums)

        # find the next smaller 
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]<nums[stack[-1]]:
                nxt_smaller[stack.pop()] = i
            stack.append(i)
        
        # find the next larger
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]>nums[stack[-1]]:
                nxt_larger[stack.pop()] = i
            stack.append(i)
        
        # find the previous smaller
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]<nums[stack[-1]]:
                stack.pop()
            pre_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # find the previous larger
        stack = []
        for i in range(len(nums)):
            while len(stack)!=0 and nums[i]>nums[stack[-1]]:
                stack.pop()
            pre_larger[i] = stack[-1] if stack else -1
            stack.append(i)
    
        count = 0
        for i in range(len(nums)):
            count+=nums[i]*(i-pre_larger[i])*(nxt_larger[i]-i)-nums[i]*(i-pre_smaller[i])*(nxt_smaller[i]-i)
        return count


