# 单调递增栈会筛选出递增的元素序列，也就是说每加入一个新元素x，就会弹出栈顶大于x的其他元素，直到栈顶小于x为止
# 单调递减栈会筛选出递减的元素序列，也就是说每加入一个新元素x，就会弹出栈顶小于x的其他元素，直到栈顶元素大于x为止

# 如果正序遍历nums，维护一个递增栈，那么弹出的元素就是乱序的元素
# 如果反向遍历nums，维护一个递减栈，那么弹出的元素就是乱序的元素

# 思路：找到最左边乱序的位置和最右边乱序的位置
# 1. 从左到右维护单调递增栈，如果发现nums[i]<nums[stack[-1]]，说明出现了逆序，因此此时栈顶的位置需要进行排序，它可能就是逆序区间的最左边界left
# 2. 从右到左维护单调递减栈，我们还需要找到right，所以维护单调递减栈，如果发现nums[i]>nums[stack[-1]]，说明出现了逆序

# 核心思路：对于一个有序数组来说，每个元素应该大于或者等于目前见到过的最大元素，因此我们可以通过比较当前元素和目前见到过的最大元素来判断是不是遇到了乱序数组的左边界
# 同理，如果我们要找一个右边界，每个元素应该大于或者等于目前见到过的最大元素

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = float('inf')
        right = float('-inf')
        # 递增栈，存储元素索引
        increasing_stack = []
        for i in range(n):
            # 如果当前元素大于栈顶元素，说明栈顶是乱序区间的left
            while len(increasing_stack)!=0 and nums[increasing_stack[-1]]>nums[i]:
                # 弹出的元素都是乱序元素，其中最小的索引就是乱序子数组的左边
                left = min(left, increasing_stack.pop())
            increasing_stack.append(i)
        
        # 递减栈，存储元素索引
        decreasing_stack = []
        for i in range(n-1, -1, -1):
            while len(decreasing_stack)!=0 and nums[decreasing_stack[-1]]<nums[i]:
                # 弹出的元素都是乱序元素，其中最大的索引就是乱序子数组的右边界
                right = max(right, decreasing_stack.pop())
            decreasing_stack.append(i)
        if left==float('inf') and right==float('-inf'):
            return 0 # 单调栈没有弹出任何元素，因此nums本来就是有序的
        return right-left+1        