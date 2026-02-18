# [1, 3, 2, 3, 3] left = 0 right = 3==> [1, 3, 2, 3]
# left = 2 this is the minimal index which can let the subarray valid(the number of max_nums at least k times)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        count = 0
        left = 0
        max_nums = max(nums)
        for right in range(len(nums)):
            if nums[right]==max_nums: # update the number of max_nums in the subarray
                count+=1
            while count==k: # we have already find the shortest subarray for left and the number of max_nums is k
                if nums[left]==max_nums:
                    count-=1
                left+=1 # the minimal index for keeping the count<k
            ans += left # the number of subarray which make subarray for right valid
        return ans