# 时间复杂度：O(n) 因为fast指针会一直移动到末尾
# 空间复杂度：O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast<len(nums):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow