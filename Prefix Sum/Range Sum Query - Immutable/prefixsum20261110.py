class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.res = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                self.res[i] = nums[i]
            else:
                self.res[i] = self.res[i-1]+self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.res[right]-self.res[left-1]
        else:
            return self.res[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)