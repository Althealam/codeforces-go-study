class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i] = -1
        pre = 0
        cnt = {}
        cnt[0] = -1
        ans = 0
        for i in range(len(nums)):
            pre+=nums[i]
            target = pre
            if target in cnt:
                ans = max(ans, i-cnt[target])
            if pre not in cnt:
                cnt[pre] = i
        return ans