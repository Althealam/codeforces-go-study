class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        ans = 0
        path_product = 1 # the product in the subarray
        left = 0
        for right in range(len(nums)):
            path_product*=nums[right]
            while path_product>=k: # remove the subarray
                path_product/=nums[left]
                left+=1
            ans+=right-left+1
        return ans
