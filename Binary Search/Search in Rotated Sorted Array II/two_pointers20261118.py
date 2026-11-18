# 这道题 相比 搜索旋转排序数组 这道题多的条件是：数组中有重复元素
# 导致的问题是，可能会出现如下数组：
# [1, 0, 1, 1, 1] target=0时
# nums[left]=nums[mid]=nums[right]=1 此时nums[mid]>=nums[left]为True，但是左半部分是[1, 0]，也就不符合有序数组

# 解决重复元素的问题：当三个位置的元素相等时，先缩小左右边界

# 时间复杂度：
# - 平均情况为O(logn)，即数组的重复元素没有阻碍二分判断时为logn，每次都能排除一半的元素
# - 最坏情况为O(n)，比如nums=[1,1,1,1,1],target=2，那么每次都会遇到nums[mid]=nums[left]=nums[right]
# 空间复杂度：O(1) 只用了常数空间
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]==nums[right]:
                left+=1
                right-=1
            elif nums[mid]>=nums[left]: # 左半部分有序
                if nums[left]<=target<nums[mid]: # target在有序数组中
                    right = mid-1
                else: # target在右侧
                    left = mid+1
            else: # 右半部分有序
                if nums[mid]<target<=nums[right]: # target在有序数组中
                    left = mid+1
                else: # target在左侧
                    right = mid-1
        return False