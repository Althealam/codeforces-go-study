# 时间复杂度：O(logn)
# 假设数组长度为n，每次经过循环，二分查找都会排除一半的元素（n/2）
# 假设执行了k次后，只剩下一个元素，因此n/2^k=1 ==> k=log2n
# 因此while循环最多执行大约log2n次

# 空间复杂度：都是常数，因此是O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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