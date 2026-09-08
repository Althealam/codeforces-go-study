# 时间复杂度：O(n) left和right最多会移动n次
# 空间复杂度：O(n) 创建了长度为n的结果数组
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        ind = len(nums)-1
        left, right = 0, len(nums)-1
        while left<=right:
            if nums[left]*nums[left]>=nums[right]*nums[right]:
                res[ind] = nums[left]*nums[left]
                left+=1
            else:
                res[ind] = nums[right]*nums[right]
                right-=1
            ind-=1
        return res