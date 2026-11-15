# 思路：每次比较相邻的两个元素，如果左边比右边的大，就交换他们的位置。
def bubble_sort(nums):
    n = len(nums)
    for i in range(n): # 表示当前正在进行第几轮冒泡，每完成一轮，未排序部分的最大值就会移动到末尾
        swapped = False
        for j in range(n-i-1): # -1是因为要比较j和j+1;-i是因为每完成一轮，末尾就多一个已经排序好的元素
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped: # 如果这一整轮都没有发生交换，说明所有的相邻元素都满足nums[j]<=nums[j+1]
            break
    return nums

# 选择排序：selection sort
# 思路：每轮从未排序部分找到最小元素，与当前位置交换
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j]<nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# 插入排序 insertion sort
# 思路：维护一个已经排好序的前缀，每次将新的元素插入到合适的位置
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums

# 快速排序 Quick Sort
# 思路：每次选择一个基准值pivot，把小于它的元素放在左边，大于它的放在右边，再递归排序
import random
def quick_sort(nums):
    if len(nums)<=1:
        return nums
    pivot = random.choice(nums)
    left = [x for x in nums if x<pivot]
    right = [x for x in nums if x>pivot]
    mid = [x for x in nums if x==pivot]
    return quick_sort(left)+mid+quick_sort(right)
# 时间复杂度：
# 1. 每一层的时间复杂度为O(n)：假设当前有n个元素，划分操作为O(n)
# 2. 总共有O(logn)层，原因是第0层为n，第1层为n/2，第2层为n/4，第3层为n/8个元素，因此n/2^h=1==>h=log2n
# 3. 总时间复杂度：总时间=每层工作量*递归层数 =O(nlogn)
# 最坏情况：每次选择的pivot都是当前数组的最大值或者最小值，导致划分不均匀，因此递归深度为logn变成了n

# 空间复杂度：原地排序不需要额外创建空间，因此空间复杂度来自递归调用栈
# 划分均匀的情况下，每次将数组分为两半，递归深度为O(logn)，总复杂度为O(logn)
# 划分不均匀的情况下，递归深度为O(n)，总复杂度为O(n)