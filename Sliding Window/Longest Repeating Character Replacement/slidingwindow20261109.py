# 替换：窗口长度-窗口最高字符频率<=k
# 思路：
# 1. 右指针扩大窗口
# 2. 窗口不合法时收缩
# 3. 更新最长的长度

# 最多替换k个字符后能够变成相同字符的最长连续子串 -> 滑动窗口
# 对于任意一个窗口，最少替换次数=窗口长度-窗口内出现频率最多的字符的频率
# 如果替换次数超过k，则缩小窗口；否则更新最长的合法窗口长度
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        counter = Counter()
        for right in range(len(s)):
            counter[s[right]]+=1
            while (right-left+1)-max(counter.values())>k:
                counter[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans
