# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        s_new = list(s.split())
        left, right = 0, len(s_new)-1
        while left<right:
            s_new[left], s_new[right] = s_new[right], s_new[left]
            left+=1
            right-=1
        return " ".join(s_new[:])
