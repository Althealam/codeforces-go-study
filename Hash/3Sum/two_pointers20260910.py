# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # O(nlogn)
        ans = []
        for i in range(len(nums)): # O(n)
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right: # O(n)
                if nums[i]+nums[left]+nums[right]==0:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 去掉重复的
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    # 找到了答案后才移动指针
                    left+=1
                    right-=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
        return ans