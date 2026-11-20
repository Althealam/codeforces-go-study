# 性质：由于数组已经排序，因此距离x最近的k个元素一定构成一个连续子数组 -> 找到一个长度为k的最优窗口
# 目的：寻找最优窗口的左边界
# 假设窗口左边界为mid，那么当前窗口为arr[mid:mid+k]
# 只需要比较x-arr[mid]和arr[mid+k]-x即可判断窗口往哪边移动
# 1. x-arr[mid]>arr[mid+k]-x => 右边新增的元素比左边移除的元素更加接近x，则向右移动 => left=mid+1
# 2. x-arr[mid]<=arr[mid+k]-x => 左边的元素更加合适 => right=mid

# 技巧：将寻找K个最近的元素，转换为对长度固定为K的窗口左边界进行二分查找
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n-k
        while left<right:
            mid = (left+right)//2
            if x-arr[mid]>arr[mid+k]-x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]