class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums)==0:
            return [-1, -1]
        ind = self.binary_search(nums, target)
        if ind==-1:
            return [-1, -1]
        left, right = ind, ind
        while left>0 and nums[left-1]==nums[left]:
            left-=1
        while right<len(nums)-1 and nums[right+1]==nums[right]:
            right+=1
        return [left, right]

    def binary_search(self, nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
