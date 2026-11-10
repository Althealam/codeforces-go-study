# 滑动窗口：
# 1. 寻找连续子串
# 2. 每个子串的长度固定为10
# 统计字符串频率：定义一个哈希表，统计每个字符串出现的频率
# 加入答案的时机：当该字符串已经出现在哈希表中一次了，第二次就要加入答案，第三次则跳过
# 如何获取窗口内的字符串：left=right-10+1=right-9 -> s[left:right+1]
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = {}
        ans = []
        for right in range(len(s)):
            left = right-10+1
            if left<0:
                continue
            else:
                cur_st = s[left:right+1]
                if cur_st in res and res[cur_st]==1:
                    ans.append(cur_st)
                    res[cur_st]+=1
                elif cur_st not in res:
                    res[cur_st]=1
                else:
                    res[cur_st]+=1
        return ans

                