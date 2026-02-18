class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = float('-inf')
        cnt = defaultdict(int)
        for right, ch in enumerate(s):
            cnt[ch]+=1
            while cnt[ch]>1:
                cnt[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans