#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30404
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
# 滑动窗口+哈希表
# 关键特征
# 1. 寻找连续子串
# 2. 子串长度固定，如果要和p构成字母异位词，长度必须等于len(p)
# 思路：
# 1. 统计p的字符频率
# 2. 移动右指针，每次遍历一个字符，将其加入到窗口中
# 3. 计算左指针位置（固定长度窗口）
# 4. 判断窗口是否合法，如果合法的话则更新答案值
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        counter_p = Counter(p)
        counter_s = Counter()
        ans = []
        for right, c in enumerate(s):
            counter_s[c]+=1 
            left = right-len(p)+1
            if left<0:
                continue
            if counter_s==counter_p:
                ans.append(left)
            counter_s[s[left]]-=1
        return ans


# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

