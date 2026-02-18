# 最多有一对相同的重复子串
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        count = 0
        for right in range(len(s)):
            if right>0 and s[right]==s[right-1]:
                count+=1
            while count>1:
                if s[left]==s[left+1]:
                    count-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans