#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30404
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()
        left = 0
        max_len = 0
        for right, st in enumerate(s):
            counter[st]+=1
            while counter[st]>1:
                counter[s[left]]-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len

        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

