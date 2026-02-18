class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0 # the length of the longest subarray 
        left = 0
        freq = {}
        for right in range(len(nums)):
            if nums[right] not in freq:
                freq[nums[right]]=1
            else:
                freq[nums[right]]+=1
            
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans
            
