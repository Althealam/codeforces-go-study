from sys import prefix


class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0]*len(nums)
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        for i in range(len(self.nums)):
            if i==0:
                self.prefix_sum[i] = self.nums[i]
            else:
                self.prefix_sum[i] = self.prefix_sum[i-1]+self.nums[i]
        print(self.prefix_sum)
        if left==0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right]-self.prefix_sum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# nums[0]+nums[1]+nums[2]
# prefix_sum[2] = nums[0]+nums[1]+nums[2]
# prefix_sum[0] = nums[0]
# prefix_sum[5] = nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+nums[5]
nums = [-2, 0, 3, -5, 2, -1]
left, right = [2, 5]
obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)