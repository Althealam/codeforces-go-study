# mid = (left+right)//2
# 1. nums[mid]>=nums[left]: 左半部分有序
# - nums[left] < target < nums[mid]: target在[left, mid]中间 -> right=mid-1
# - target > nums[mid]: target在右侧，即left=mid+1
# 2. nums[mid]<nums[left]: 左半部分不有序，那么右半部分有序
# - nums[mid] < target < nums[right]: target在[mid, right]中间 -> left=mid+1
# - target < nums[mid]: target在左侧，即right=mid-1
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]: 
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1

# 需要同步检查nums[left]和nums[right]两端
# 时间复杂度：O(logn)，每次循环都将搜索范围缩小一半
# 空间复杂度：O(1)，只用left, right, mid常数变量